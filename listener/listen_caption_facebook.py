import threading
import time
from typing import Union

from DrissionPage._pages.chromium_page import ChromiumPage
from DrissionPage._pages.chromium_tab import ChromiumTab

import facebook_caption
import listener_All
from utils.decorator import monitor_function


@monitor_function
def get_group_info(page_get_groupId: Union[ChromiumPage, ChromiumTab], getGroup_userId, keyword,
                   valid_event: threading.Event):
    functions = [facebook_caption.collecting_groupId, listener_All.listen_group_info]
    threads = []
    # 导入线程函数后创建一个事件对象
    stop_event = threading.Event()

    # 使用循环创建线程，并传递参数
    for function in functions:
        thread = threading.Thread(target=function, args=(page_get_groupId, getGroup_userId, keyword, stop_event,))
        thread.start()
        threads.append(thread)

    # 使用 threading.Timer 定时器设置超时
    timer = threading.Timer(60 * 10, stop_event.set)
    timer.start()

    # 等待所有线程完成
    for thread in threads:
        thread.join()

    valid_event.set()

    return True


@monitor_function
def get_group_userId(page_get_groupUserId, getGroupUser_userId, group_id, valid_event: threading.Event):
    functions = [facebook_caption.collecting_group_userId, listener_All.listen_group_member]
    threads = []

    # 创建事件对象
    stop_event = threading.Event()

    # 创建线程并启动
    for function in functions:
        thread = threading.Thread(target=function,
                                  args=(page_get_groupUserId, getGroupUser_userId, group_id, stop_event, valid_event,))
        thread.start()
        threads.append(thread)

    # 使用 threading.Timer 定时器设置超时
    timer = threading.Timer(60 * 20, stop_event.set)
    timer.start()

    # 等待所有线程完成
    for thread in threads:
        thread.join()

    valid_event.set()

    return True


@monitor_function
def monitoring_Team_Comments(page_get_groupUserId: Union[ChromiumPage, ChromiumTab], getGroupUser_userId,
                             group_url: str, valid_event: threading.Event):
    # page_get_groupUserId.get(group_url)
    functions = [facebook_caption.scroll_group_comment, listener_All.listen_group_comment]
    threads = []
    # 创建事件对象
    stop_event = threading.Event()

    # 创建线程并启动
    for function in functions:
        thread = threading.Thread(target=function,
                                  args=(page_get_groupUserId, getGroupUser_userId, group_url, stop_event, valid_event,))
        thread.start()
        threads.append(thread)

    hour = 0.25
    listener_time = 60 * 60 * hour
    # 使用 threading.Timer 定时器设置超时
    timer = threading.Timer(listener_time, stop_event.set)
    timer.start()

    # 等待所有线程完成
    for thread in threads:
        thread.join()

    valid_event.set()

    return True


def test():
    def test_1(stop_event1: threading.Event):
        for i in range(5):
            print(i)
            time.sleep(1)
        stop_event1.set()

    def test_2(stop_event2: threading.Event):
        while not stop_event2.is_set():
            time.sleep(0.5)
            print('---------------')

    functions = [test_1, test_2]
    threads = []
    # 导入线程函数后创建一个事件对象
    stop_event = threading.Event()

    # 使用循环创建线程，并传递参数
    for function in functions:
        thread = threading.Thread(target=function,
                                  args=(stop_event,))
        thread.start()
        threads.append(thread)

    # 等待所有线程完成
    for thread in threads:
        thread.join()

    return True


if __name__ == '__main__':
    test()
