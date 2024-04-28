import datetime
import json
import math
import msvcrt
import multiprocessing
import os
import random
import time

import pandas as pd
import requests
from DrissionPage.common import from_selenium
from loguru import logger
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

from listener import listen_caption_ins as listen_ins
from utils.decorator import reset_file

ROOT_PATH = 'browserDownload'
LOG_PATH = f'./logs/listener_facebook'

# 设置日志文件名和格式 日志文件按不同日期分别存放
formatted_time = datetime.datetime.now().strftime("%Y-%m-%d---%H_%M_%S")
current_data = datetime.datetime.now().strftime("%Y-%m-%d")
os.makedirs(f'{LOG_PATH}/{current_data}', exist_ok=True)
logger.add(f'{LOG_PATH}/{current_data}/{formatted_time}.log', format="{time} {level} {message}", level="INFO")

df_test = pd.read_csv('ins_data/user_data_csv/2024-04-26.csv', encoding='utf8')
user_fans_list = df_test['user'].tolist()


class Run:
    def __init__(self):
        self.finger_headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }
        self.finger_url = 'http://127.0.0.1:50325'

    # 根据对应user_id打开对应窗口
    def start_userID(self, user_id):
        url = f'{self.finger_url}/api/v1/browser/start'
        data = {'user_id': user_id}
        res = requests.get(url, headers=self.finger_headers, params=data)
        if res.status_code == 200:
            res_result = json.loads(res.text)
            if res_result["msg"] == "Success" or res_result["msg"] == "success":
                # 注意：下面两个参数必须传给selenium才能 启动指纹浏览器
                selenium_webdriver = res_result["data"]["webdriver"]
                selenium_address = res_result["data"]["ws"]["selenium"]
                logger.info(res_result)
                return selenium_webdriver, selenium_address, user_id
        else:
            logger.info(f'启动对应user_id指纹浏览器失败, 状态码:{res.status_code}')

    def start_selenium(self, selenium_webdriver, selenium_address, user_id):
        logger.info(f'当前执行窗口--{user_id}')
        chrome_option = Options()
        service = Service(selenium_webdriver)
        chrome_option.add_experimental_option("debuggerAddress", selenium_address)  # 这行命令必须加上，才能启动指纹浏览器

        driver = webdriver.Chrome(service=service, options=chrome_option)
        # driver.maximize_window()
        page = from_selenium(driver)
        close_tab = page.get_tab(url='https://start.adspower.net/')
        if close_tab:
            close_tab.close()
        page.set.window.max()
        page.set.window.mini()

        # os.makedirs(f'./{ROOT_PATH}/{user_id}', exist_ok=True)

        return page


r = Run()


def saveCompleteId(user_id_save, save_platformType):
    # 打开文件并获取锁
    with open(f'txt_path/{save_platformType}_complete_id.txt', 'a') as file:
        msvcrt.locking(file.fileno(), msvcrt.LK_LOCK, 1)  # 获取锁
        file.write(f"{user_id_save}\n")
        msvcrt.locking(file.fileno(), msvcrt.LK_UNLCK, 1)  # 释放锁


def saveCurrentBrower(user_id_save):
    # 打开文件并获取锁
    with open(f'txt_path/group_count.txt', 'a') as file:
        msvcrt.locking(file.fileno(), msvcrt.LK_LOCK, 1)  # 获取锁
        file.write(f"{user_id_save}\n")
        msvcrt.locking(file.fileno(), msvcrt.LK_UNLCK, 1)  # 释放锁


# 将user_id存入任务队列中
def operate_facebook_listener(browser_id_op, model, temp_index, add_index, op_platformType, user_start_index):
    selenium_webdriver, selenium_address, user_id = None, None, None
    for _ in range(3):
        try:
            # time.sleep(random.uniform(0.1, 5))
            selenium_webdriver, selenium_address, user_id = r.start_userID(user_id=browser_id_op)
            logger.info(f'{selenium_webdriver}----{selenium_address}----{user_id}')
        except:
            time.sleep(random.uniform(2, 4))
            continue
        break
    if selenium_webdriver is None:
        logger.error(f'{browser_id_op}连接失败，请检查adspower是否打开')
        return False
    page = r.start_selenium(selenium_webdriver, selenium_address, user_id)
    logger.info(f'{browser_id_op}   {model}')
    temp_index += add_index

    #
    logger.info(f'当前是第{temp_index}台浏览器')

    # logger.info(page_count.url)
    flag = False
    if len(page.url) > len('https://www.instagram.com/'):
        page.get('https://www.instagram.com/')
        page.wait(10, 20)

    if model == 'get_user_info':
        pass
    elif model == 'get_user_fans':
        flag=listen_ins.get_user_fans(page, user_id, user_fans_list[user_start_index])

    if flag:
        saveCompleteId(browser_id_op, op_platformType)
        logger.info(f'{browser_id_op}已完成操作')
    else:
        logger.error(f'{browser_id_op}有异常情况，发生中断')
    page.quit()


def start_many_process(browsers, model, cycle_index, complete_browser_length, start_platformType):
    # 启动多个进程来操作多个浏览器
    processes = []
    count = 0
    with open('utils/keyword/ins_fans_start.txt', 'r') as f:
        start_index = int(f.read())
    if start_index + len(browsers) > len(user_fans_list):
        start_index = 1
    for browsers_id in browsers:
        temp = (cycle_index - 1) * len(browsers) + count + 1
        start_index = start_index + count - 1
        process = multiprocessing.Process(target=operate_facebook_listener,
                                          args=(browsers_id, model, temp, complete_browser_length,
                                                start_platformType, start_index,))
        processes.append(process)
        process.start()
        count += 1
        time.sleep(5)

    # 等待所有进程完成
    for process in processes:
        process.join()

    with open('utils/keyword/ins_fans_start.txt', 'w') as f:
        f.write(f'{start_index}')


def reset_complete_txt(del_platformType_run):
    with open(f'./txt_path/{del_platformType_run}_browser_id.txt', 'r', encoding='utf8') as f:
        origin_browser_id_set = set(line.strip() for line in f.readlines())
    with open(f'./txt_path/{del_platformType_run}_complete_id.txt', 'r', encoding='utf8') as f:
        complete_browser_id_set = set(line.strip() for line in f.readlines())
    if origin_browser_id_set == complete_browser_id_set:
        with open(f'./txt_path/{del_platformType_run}_complete_id.txt', 'w', encoding='utf8') as f:
            f.write('')
        logger.info('complete文件已重置，可以进行新的操作')


# 导出未完成的浏览器序号
def exportIncompleteBrowserNumber():
    with open('txt_path/tiktok_browser_id.txt', 'r', encoding='utf8') as f:
        origin_browser_id_set = set(line.strip() for line in f.readlines())
    with open('txt_path/tiktok_complete_id.txt', 'r', encoding='utf8') as f:
        complete_browser_id_set = set(line.strip() for line in f.readlines())
    # 去除已完成操作的浏览器
    browser_id_set = origin_browser_id_set - complete_browser_id_set

    # 读取编号转id的json文件
    with open('other/temp_js.json/video/browser_id.json', 'r', encoding='utf8') as f:
        tran_json = json.load(f)
    # print(tran_json)
    no_complete_browser_list = [tran_json[b_id] for b_id in complete_browser_id_set]
    print(no_complete_browser_list)


@reset_file
def run(op_i, platformType_run, maxProcesses):
    model_list_run = ['get_user_info', 'get_user_fans']

    # 最大进程数
    # run_maxProcesses = 16
    with open(f'txt_path/{platformType_run}_browser_id.txt', 'r', encoding='utf8') as f_1:
        origin_browser_id_set = set(line.strip() for line in f_1.readlines())
    try:
        with open(f'txt_path/{platformType_run}_complete_id.txt', 'r', encoding='utf8') as f_2:
            complete_browser_id_set = set(line.strip() for line in f_2.readlines())
    except FileNotFoundError:
        with open(f'txt_path/{platformType_run}_complete_id.txt', 'w', encoding='utf8') as f_2:
            complete_browser_id_set = set()
        logger.info(f'txt_path/{platformType_run}_complete_id.txt 文件已创建')

    # 去除已完成操作的浏览器
    browser_id_set = origin_browser_id_set - complete_browser_id_set
    complete_browser_length = len(complete_browser_id_set)

    numberCycles = math.ceil(len(browser_id_set) / maxProcesses)

    cycle_count = 1
    for count_i in range(numberCycles):
        # 随机选取N个浏览器 N = numberOfProcesses
        try:
            current_browser_id_list = random.sample(browser_id_set, maxProcesses)
        except ValueError:
            current_browser_id_list = list(browser_id_set)
        start_many_process(current_browser_id_list, model_list_run[op_i], cycle_count,
                           complete_browser_length, platformType_run)
        cycle_count += 1
        for repeat_i in current_browser_id_list:
            browser_id_set.remove(repeat_i)
    # 线程池
    # with multiprocessing.Pool(processes=run_maxProcesses) as pool:  # 创建一个包含maxProcesses个进程的进程池
    #     for browser in browser_id_set:
    #         time.sleep(random.uniform(2, 5))  # 暂停2秒
    #         pool.apply_async(operate_tiktok, args=(browser, model_list_run[operate_index_run],cycle_count, complete_browser_length,
    #                        platformType_run))  # 使用进程池处理浏览器自动化操作
    #     pool.close()
    #     pool.join()

    logger.info('操作已全部完成')
    reset_complete_txt(platformType_run)


if __name__ == "__main__":
    model_list = ['get_user_info', 'get_user_fans']
    # 选择浏览器id文件
    platformType = 'ins_all'

    run(0, platformType_run=platformType, maxProcesses=10)

    # while temp_add < len(group_list):
    #     run(1, loop_platformType, 29, temp_add)
    #     with open(f'txt_path/{loop_platformType}_complete_id.txt', 'w') as f:
    #         f.write('')
    #     temp_add += bro_length
    # for i in range(1, 100):
    #     if i % 2 == 0:
    #         with open(f'./txt_path/{loop_platformType}_complete_id.txt', 'w', encoding='utf8') as f:
    #             f.write('')
    #     run(2, loop_platformType, 12)
