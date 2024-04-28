import threading
import time

import caption_ins as cap_ins


def get_user_fans(page_get_user, get_user_id, user_name_get):
    functions = [cap_ins.listen_user_fans, cap_ins.collect_user_fans]
    threads = []
    # 导入线程函数后创建一个事件对象
    stop_event = threading.Event()

    # 使用循环创建线程，并传递参数
    for function in functions:
        thread = threading.Thread(target=function, args=(page_get_user, get_user_id, user_name_get, stop_event,))
        thread.start()
        threads.append(thread)
        time.sleep(2)

    # 使用 threading.Timer 定时器设置超时
    timer = threading.Timer(60 * 60 * 1, stop_event.set)
    timer.start()

    # 等待所有线程完成
    for thread in threads:
        thread.join()

    return True


def get_user_data(page_get_user, get_user_id, get_keyword):
    functions = [cap_ins.listen_user_data, cap_ins.collect_user_data]
    threads = []
    # 导入线程函数后创建一个事件对象
    stop_event = threading.Event()

    # 使用循环创建线程，并传递参数
    for function in functions:
        thread = threading.Thread(target=function, args=(page_get_user, get_user_id, get_keyword,))
        thread.start()
        threads.append(thread)
        time.sleep(2)

    # 使用 threading.Timer 定时器设置超时
    timer = threading.Timer(60 * 1, stop_event.set)
    timer.start()

    # 等待所有线程完成
    for thread in threads:
        thread.join()

    return True
