import math
import threading
import time
from typing import Union

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
            if 'user_id' in arg:
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
    logger.info(f'{temp_user_id}开始监听事件，当前监听事件为: 监听自动化验证')
    while not stop_event.is_set():
        temp_tab = monitor_page.get_tab(url='check')
        if temp_tab:
            ac = Actions(temp_tab)
            close_box = monitor_page.ele('aria-label=关闭', timeout=5)
            if close_box:
                ac.move_to(close_box).click()
                for _ in range(10):
                    if temp_tab.url.find('check') == -1:
                        break
                    ac.click()
                    temp_tab.wait(1, 2)
        monitor_page.wait(5, 10)


if __name__ == '__main__':
    pass
