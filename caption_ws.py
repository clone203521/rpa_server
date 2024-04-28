import os
from datetime import datetime
from typing import Union

from DrissionPage._pages.chromium_page import ChromiumPage
from DrissionPage._pages.chromium_tab import ChromiumTab
from DrissionPage._units.actions import Actions
from loguru import logger


def getGroupTel_all(page_group_tel: Union[ChromiumPage, ChromiumTab], group_url_list, user_id_getTel_all):
    min_len = len('https://chat.whatsapp.com/')
    count = 1
    tel_count = 0
    for group_url_temp in group_url_list[1:]:
        if len(group_url_temp) <= min_len or 'https://chat.whatsapp.com/' not in group_url_temp:
            continue
        temp_count = getGroupMembers_one(page_group_tel, group_url_temp, user_id_getTel_all)
        if temp_count == 0:
            continue
        tel_count += temp_count
        logger.debug(f'{user_id_getTel_all}当前已保存{count}个小组共{tel_count}条电话')
        page_group_tel.wait(1, 2)
        count += 1
    return True


def getGroupMembers_one(page_group: Union[ChromiumPage, ChromiumTab], group_url, user_id_getTel):
    save_path2 = f'ws_tel/ready_group/{user_id_getTel}-group.txt'
    if not os.path.exists(save_path2):
        with open(save_path2, 'w') as file:
            file.write('')

    ac = Actions(page_group)
    # group_url = 'https://chat.whatsapp.com/invite/15uYwQNsyx0046lrLEyb0U'
    page_group.get(group_url)
    logger.info(f'{user_id_getTel}正在跳转至链接{group_url}')
    page_group.wait(2, 3)

    # 点击加入
    join_box = page_group.ele('#action-button', timeout=10)
    title_name_box = join_box.prev('tag:h3')
    if not title_name_box:
        logger.warning(f'{user_id_getTel}当前链接已重置')
        with open(save_path2, 'a') as file:
            file.write(group_url + '\n')
        return 0
    join_box.click()
    logger.info(f'{user_id_getTel}第一次点击加入按钮')
    page_group.wait(2, 3)

    # 点击使用web版
    use_web = page_group.ele('tag:a@href:https://web.whatsapp.com/accept', timeout=10)
    use_web.click()
    logger.info(f'{user_id_getTel}选择web版网页')
    page_group.wait(3, 5)

    # 再次点击加入
    temp_box = page_group.ele('tag:div@data-animate-modal-popup=true', timeout=10)

    next_join = page_group.ele('css:[data-animate-modal-popup="true"] [aria-disabled="false"]', timeout=15)
    next_join.click()
    if '请求加入' in next_join.text:
        logger.debug(f'{user_id_getTel}正在请求加入群组，具体加入时间未知')
        group_name = temp_box.ele('tag:span', index=1).text
        save_path = f'ws_tel/loading_group/{user_id_getTel}--loading.txt'
        os.makedirs('ws_tel/loading_group', exist_ok=True)
        if not os.path.exists(save_path):
            with open(save_path, 'w') as f:
                f.write('')
        with open(save_path, 'a') as f:
            f.write(f'{group_name} {group_url}\n')
        with open(save_path2, 'a') as file:
            file.write(group_url + '\n')
        return 0
    # print(next_join.inner_html)
    ac.move_to(next_join).click()
    logger.info(f'{user_id_getTel}再次点击加入按钮')
    page_group.wait(3, 5)
    #

    # 获取title属性
    title_box = page_group.ele('css:#main [title^="+"]', timeout=10)
    ac.move_to(title_box).click()
    page_group.wait(5, 7)
    title_main = title_box.attr('title')

    tel_list = title_main.split('、')[:-1]
    logger.success(f'{user_id_getTel}当前获取到号码{len(tel_list)}个')
    # print(tel_list)
    original_time = datetime.now()
    current_time = f'{original_time.strftime("%m-%d")}'
    save_path = f'ws_tel/{current_time}'
    os.makedirs(save_path, exist_ok=True)

    with open(f'{save_path}/{user_id_getTel}-{original_time.strftime("%H_%M_%S")}.txt', 'w') as file:
        file.write('\n'.join(tel_list))
    os.makedirs(f'ws_tel/ready_group', exist_ok=True)

    with open(save_path2, 'a') as file:
        file.write(group_url + '\n')
    main_box = page_group.ele('tag:section', timeout=10)
    ac.move_to(main_box).scroll(0, 1000)
    ac.scroll(0, 1000)

    leave_group_box = page_group.ele('tag:span@@text()=离开群组', timeout=10)
    leave_group_box.click()

    leave_group_box = page_group.ele('tag:div@@text()=退出群组', timeout=10)
    leave_group_box.click()

    leave_group_box = page_group.ele('tag:span@@text()=删除群组', timeout=10)
    leave_group_box.click()

    leave_group_box = page_group.ele('tag:div@@text()=删除群组', timeout=10)
    leave_group_box.click()

    return len(tel_list)
