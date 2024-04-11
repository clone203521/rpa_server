import json
import os
import threading
from datetime import datetime
from typing import Union

from DrissionPage._pages.chromium_page import ChromiumPage
from DrissionPage._pages.chromium_tab import ChromiumTab
from loguru import logger

from utils import my_utils

ROOT_PATH = 'listener_data'
formatted_time = datetime.now().strftime("%Y-%m-%d---%H_%M_%S")
logger.add(f'{ROOT_PATH}/logs/{formatted_time}.log', format="{time} {level} {message}", level="INFO")


def save_to_json(origin_json, function_name, user_name):
    # 设置json数据包存储位置，按照采集用户名存储
    save_current_time = datetime.now().strftime("%Y-%m-%d---%H_%M_%S")

    fin_path = f'./{ROOT_PATH}/{function_name}/{user_name}'
    os.makedirs(fin_path, exist_ok=True)
    with open(f'{fin_path}/{function_name}---{save_current_time}.json', 'w', encoding='utf8') as f:
        json.dump(origin_json, f, ensure_ascii=False, indent=4)


def listener_tiktok_fans(tiktok_fans_page):
    tiktok_fans_page.listen.start('www.tiktok.com/api/user/list/?WebIdLastTime')  # 开始监听，指定获取包含该文本的数据包

    logger.info('开始监听')
    username = tiktok_fans_page.url.split('@')[-1]
    count = 1
    for packet in tiktok_fans_page.listen.steps():
        temp_json = packet.response.body
        try:
            temp = temp_json['userList'][0]
            save_to_json(temp_json, 'tiktok_fans', username)
            logger.info(f'监听到第{count}个数据包')
            count += 1
        except Exception as e:
            logger.error(f'当前数据包没有用户列表')
            pass


def listen_group_member(page_add_friInGp: Union[ChromiumPage, ChromiumTab], user_id_add_FriInGp, listen_group_id,
                        stop_event: threading.Event):
    """监听小组成员"""

    # page_add_FriInGp.get(group_url)
    page_add_friInGp.listen.start('graphql/')  # 开始监听，指定获取包含该文本的数据包
    logger.info(f'{user_id_add_FriInGp}监听开始')
    count = 1
    page_add_friInGp.wait(3)
    for packet in page_add_friInGp.listen.steps(timeout=30):
        if stop_event.is_set():
            break
        logger.info(f'{user_id_add_FriInGp}============={count}')
        try:
            has_aaa_key = any("node" in key for key in packet.response.body['data'].keys())
        except (KeyError, TypeError):
            has_aaa_key = False
        if has_aaa_key:
            logger.info(f'{user_id_add_FriInGp}监听到第{count}个数据包')
            count += 1
            my_utils.save_userId_toTxt(packet.response.body, listen_group_id, user_id_add_FriInGp)
            if count == 20:
                stop_event.set()
                break
    if not stop_event.is_set():
        stop_event.set()
        logger.info(f'{user_id_add_FriInGp}监听结束')
    return True


def listen_group_info(page_listen_gpInfo: Union[ChromiumPage, ChromiumTab], user_id_add_FriInGp, group_key,
                      stop_event: threading.Event):
    """监听小组信息"""
    page_listen_gpInfo.listen.start('/api/graphql/')  # 开始监听，指定获取包含该文本的数据包

    logger.info(f'{user_id_add_FriInGp}监听开始')
    count = 1

    for packet in page_listen_gpInfo.listen.steps(timeout=30):
        if count == 100 or stop_event.is_set():
            break
        try:
            has_aaa_key = any("serpResponse" in key for key in packet.response.body['data'].keys())
        except (KeyError, TypeError):
            has_aaa_key = False
        if has_aaa_key:
            logger.info(f'{user_id_add_FriInGp}监听到第{count}个数据包')
            count += 1
            my_utils.save_groupInfo_toJson(packet.response.body['data']['serpResponse']['results']['edges'],
                                           group_key, user_id_add_FriInGp)
            if count == 9:
                stop_event.set()
                break

    return True


def listen_fans_tiktok(page_listen_tiktok_fans: Union[ChromiumPage, ChromiumTab], user_id_fans_tiktok,
                       user_url_fans_tiktok, stop_event: threading.Event):
    """监听用户粉丝"""
    page_listen_tiktok_fans.listen.start('user/list/?WebIdLastTime')  # 开始监听，指定获取包含该文本的数据包

    logger.info(f'{user_id_fans_tiktok}监听开始')
    username = user_url_fans_tiktok.split('@')[-1]
    count = 1

    for packet in page_listen_tiktok_fans.listen.steps(timeout=30):
        try:
            has_aaa_key = any("userList" in key for key in packet.response.body.keys())
        except (KeyError, TypeError):
            has_aaa_key = False
        if has_aaa_key:
            logger.info(f'{user_id_fans_tiktok}监听到第{count}个数据包')
            count += 1
            my_utils.save_userFans_toJson(packet.response.body['userList'],
                                          username, user_id_fans_tiktok)
            if count == 100 or stop_event.is_set():
                stop_event.set()
                break

    return True


def listen_group_comment(page_listen_comment: Union[ChromiumPage, ChromiumTab], user_id_comment, group_url,
                         stop_event: threading.Event):
    """监听小组评论"""
    page_listen_comment.listen.start('/api/graphql/')  # 开始监听，指定获取包含该文本的数据包
    logger.info(f'{user_id_comment}监听开始')
    count = 1

    for packet in page_listen_comment.listen.steps(timeout=60 * 4):
        try:
            user_list = my_utils.extract_comment(packet.response.body)
        except Exception as e:
            logger.error(e)
            continue
        if count > 3 or stop_event.is_set():
            break
        for user in user_list:
            new_tab = page_listen_comment.new_tab(f'https://www.facebook.com/messages/t/{user}')
            flag = send_message(new_tab, user_id_comment)
            if flag:
                logger.info(f'{user_id_comment}发送成功，当前共发送{count}条信息')
                count += 1
            else:
                logger.error(f'{user_id_comment}评论发送失败')
            new_tab.close()
    stop_event.set()
    return True


def send_message(page_send_message: Union[ChromiumPage, ChromiumTab], user_id_message):
    try:
        page_send_message.wait(3, 6)
        input_box = page_send_message.ele('@aria-label=发消息', timeout=10)
        input_box.input(
            '''🌸 Thank you for your interest! 🛍️ We're thrilled to announce our Mother's Day celebration with a fantastic 40% discount on all Gucci, LV, Chanel, Prada bags and more! 🎉 As a professional Chinese factory, we specialize in providing 1:1 quality replicas of these luxurious brands, with free shipping worldwide! 🌍✨ If you're interested in upgrading your collection or surprising a loved one, feel free to add me on WhatsApp at https://wa.me/message/3W5Z6CJOWV32L1 for more details and personalized assistance. 📲💼 Hurry, this offer won't last forever! 🎁 #MothersDaySale #LuxuryReplica''')
        page_send_message.ele('@aria-label=按 Enter 键发送').click()
    except Exception as e:
        logger.error(e)
        return False
    return True


if __name__ == '__main__':
    user_id = 'jfdfett'
    #
    # main_page = get_page(user_id)
    # current_tab = main_page.get_tab(url='messages/t')
    # print(current_tab.url)
    # send_message(current_tab, '1212')
    # listen_group_info(main_page, user_id, 'bag')
    # listen_group_member(main_page, user_id, 'https://www.facebook.com/groups/517149728952617/', threading.Event())
