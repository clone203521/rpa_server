import os
from datetime import datetime
from typing import Union

from DrissionPage._pages.chromium_page import ChromiumPage
from DrissionPage._pages.chromium_tab import ChromiumTab
from DrissionPage._units.actions import Actions
from loguru import logger


def func_click_box(page_click, ele_path, timeout_time=10, by_mouse=None):
    click_box = page_click.ele(ele_path, timeout=timeout_time)
    if not click_box:
        return False
    if not by_mouse:
        click_box.click()
    else:
        ac = Actions(page_click)
        ac.move_to(click_box).click()
    return True


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

    page_group.get(group_url)
    logger.info(f'{user_id_getTel}正在跳转至链接{group_url}')
    page_group.wait(10)

    # 点击加入
    func_click_box(page_group,'#action-button')

    logger.info(f'{user_id_getTel}第一次点击加入按钮')
    page_group.wait(2, 3)

    # 点击使用web版
    func_click_box(page_group,'tag:a@href:https://web.whatsapp.com/accept')
    logger.info(f'{user_id_getTel}选择web版网页')

    # 再次点击加入
    temp_box = page_group.ele('tag:div@data-animate-modal-popup=true', timeout=12)
    page_group.wait(5, 5.1)

    div_x1 = page_group.ele('css:[data-animate-modal-body="true"]>div', timeout=10)
    div_x1_test = div_x1.inner_html.encode('utf8').decode('utf8')

    if '此邀请链接已重置' in div_x1_test or '无法加入' in div_x1_test:
        logger.warning(f'{user_id_getTel}当前链接已重置')
        page_group.ele('css:[data-animate-modal-body="true"] button', timeout=10).click()
        with open(save_path2, 'a') as file:
            file.write(group_url + '\n')
        return 0

    next_join = page_group.ele('css:[data-animate-modal-popup="true"] [aria-disabled="false"]', timeout=15)
    if not next_join:
        return False
    next_join_s = next_join.s_ele()
    join_text = next_join_s.text

    next_join.click()

    # 加入群组是否需要确认
    if '请求加入' in join_text:
        page_group.wait(3)
        logger.debug(f'{user_id_getTel}正在请求加入群组，具体加入时间未知')
        page_group.ele('tag:button@@text():关闭', timeout=5).click()
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

    logger.info(f'{user_id_getTel}再次点击加入按钮')
    page_group.wait(5, 5.1)

    # 获取title属性
    title_box = page_group.ele('css:#main [title^="+"]', timeout=10)
    if not title_box:
        return False
    ac.move_to(title_box).click()
    page_group.wait(5, 7)
    title_main = title_box.attr('title')

    tel_list = title_main.split('、')[:-1]
    if len(tel_list) > 10:
        logger.success(f'{user_id_getTel}当前获取到号码{len(tel_list)}个')
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
    main_size = main_box.size

    page_group.scroll.down(main_size[1])
    ac.move_to(main_box).scroll(0, main_size[1])
    page_group.wait(1)

    func_click_box(page_group, 'tag:span@@text()=离开群组')
    func_click_box(page_group, 'tag:div@@text()=退出群组')
    func_click_box(page_group, 'tag:span@@text()=删除群组')
    func_click_box(page_group, 'tag:div@@text()=删除群组')

    return len(tel_list)
