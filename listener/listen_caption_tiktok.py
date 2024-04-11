import threading
import time

import listener_All
import facebook_caption
import tiktok_caption


def get_userFans(page_get_userFans, getGroup_userId, user_url):
    functions = [tiktok_caption.collecting_userFans, listener_All.listen_fans_tiktok]
    threads = []
    # 导入线程函数后创建一个事件对象
    stop_event = threading.Event()

    # 使用循环创建线程，并传递参数
    for function in functions:
        thread = threading.Thread(target=function, args=(page_get_userFans, getGroup_userId, user_url, stop_event,))
        thread.start()
        threads.append(thread)

    # 等待所有线程完成
    for thread in threads:
        thread.join()

    return True


def get_group_userId(page_get_groupUserId, getGroupUser_userId, group_id):
    functions = [facebook_caption.collecting_group_userId, listener_All.listen_group_member]
    threads = []
    # 导入线程函数后创建一个事件对象
    stop_event = threading.Event()

    # 使用循环创建线程，并传递参数
    for function in functions:
        thread = threading.Thread(target=function,
                                  args=(page_get_groupUserId, getGroupUser_userId, group_id, stop_event,))
        thread.start()
        threads.append(thread)

    # 等待所有线程完成
    for thread in threads:
        thread.join()

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
