import math
import re
import threading
import time
from typing import Union

import requests
from DrissionPage._pages.chromium_page import ChromiumPage
from DrissionPage._pages.chromium_tab import ChromiumTab
from DrissionPage._units.actions import Actions
from loguru import logger


def reset_file(func):
    def wrapper(*args, **kwargs):
        platformType = None
        for arg in kwargs:
            if 'platformType' in arg:
                platformType = kwargs[arg]
        if platformType is not None:
            xx = input("是否重置文件 Y/N：")
            if xx == 'Y' or xx == 'y':
                with open(f'txt_path/{platformType}_complete_id.txt', 'w') as f:
                    f.write('')
        return func(*args, **kwargs)

    return wrapper


def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        run_time = end_time - start_time
        if run_time < 60:
            logger.info(f'耗时{run_time}秒')
        else:
            logger.info(f'耗时{math.floor(run_time / 60)}分{math.ceil(run_time % 60)}秒')
        return result

    return wrapper


def monitor_function(func):
    def wrapper(*args, **kwargs):
        # Extract the monitor_arg from kwargs
        temp_page = None
        temp_user_id = ''
        for arg in kwargs:
            if 'page' in arg:
                temp_page = kwargs[arg]
            if 'user_id' in arg or 'userId' in arg:
                temp_user_id = kwargs[arg]
        stop_event = kwargs['valid_event']

        # Create a thread to monitor the function execution
        monitor_thread = threading.Thread(target=monitor_thread_function, args=(temp_page, stop_event, temp_user_id,))
        monitor_thread.start()

        result = func(*args, **kwargs)
        monitor_thread.join()

        return result

    return wrapper


def monitor_thread_function(monitor_page: Union[ChromiumPage, ChromiumTab],
                            stop_event: threading.Event, temp_user_id: str):
    logger.success(f'{temp_user_id}开始监听事件，当前监听事件为: 监听自动化验证')
    while not stop_event.is_set():
        temp_tab = monitor_page.get_tab(url='check')
        login_tab = monitor_page.get_tab(url='login')
        # logger.warning(f'{temp_user_id}---监听事件正在运行')
        if temp_tab:
            logger.success(f'{temp_user_id}进入自动化验证界面')
            ac = Actions(temp_tab)
            close_box = monitor_page.ele('tag:div@aria-label=关闭', timeout=10)
            if close_box:
                ac.move_to(close_box).click()
                for _ in range(10):
                    if temp_tab.url.find('check') == -1:
                        break
                    ac.click()
                    temp_tab.wait(1, 2)
                continue
            complaint_box = monitor_page.ele('@aria-label=申诉', timeout=5)
            locked_box = monitor_page.ele('tag:span@@text():你的帐户已锁定', timeout=5)

            if complaint_box or locked_box:
                logger.error(f'{temp_user_id}---账号进入申诉阶段')
                data = {
                    'bro_name': temp_user_id,
                    'tag': 'fb身份证验证'
                }
                requests.post('http://fbmessage.v7.idcfengye.com/addTag', json=data)
                stop_event.set()
        if login_tab:
            logger.warning(f'{temp_user_id}退出登陆状态')
            login_tab.get('https://mbasic.facebook.com/login.php')
            login_box = login_tab.ele('tag:input@type=image', timeout=5)
            ac = Actions(login_tab)
            if login_box:
                ac.move_to(login_box).click()
                login_tab.wait(3, 5)
            if 'password' in login_tab.url:
                match = re.search(r'uid=(\d+)', login_tab.url)
                input_box = login_tab.ele('tag:input@type=password', timeout=5)
                password = requests.get(url='http://127.0.0.1:12144/get_FbPwd', json={'id': match.group(1)}).json()
                input_box.input(password['msg'])
                logger.warning(f'{temp_user_id}正在输入密码')

                login_button = login_tab.ele('tag:input@type=submit', timeout=5)
                login_button.click()
                logger.warning(f'{temp_user_id}正在尝试重新登陆')
                login_tab.wait(3, 5)
            login_tab.get('https://www.facebook.com/')
            login_tab.wait(3, 5)
            if login_tab.url == 'https://www.facebook.com/':
                logger.success(f'{temp_user_id}登陆成功，重新回到主页')
                stop_event.set()

        monitor_page.wait(5, 10)
    logger.success(f'{temp_user_id}---监听事件结束')


if __name__ == '__main__':
    x = 5 < 6
    print(x)
