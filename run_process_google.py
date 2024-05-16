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

import caption_google as cap_google
from utils.decorator import reset_file

ROOT_PATH = 'browserDownload'
LOG_PATH = f'./logs/more_process'

# 设置日志文件名和格式 日志文件按不同日期分别存放
formatted_time = datetime.datetime.now().strftime("%Y-%m-%d---%H_%M_%S")
current_data = datetime.datetime.now().strftime("%Y-%m-%d")
os.makedirs(f'{LOG_PATH}/{current_data}', exist_ok=True)
logger.add(f'{LOG_PATH}/{current_data}/{formatted_time}.log', format="{time} {level} {message}", level="INFO")

account_list = pd.read_csv('utils/facebook_10.csv', encoding='utf8')


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
        url = f'{self.finger_url}/api/v1/browser/start?user_id={user_id}'
        data = {'user_id': user_id}
        res = requests.get(url, headers=self.finger_headers)
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

        time.sleep(2)
        # # 获取所有窗口句柄
        # window_handles = driver.window_handles
        # # 切换到最后一个标签页
        # # 遍历除最后一个句柄之外的所有句柄
        # for handle in window_handles[:-1]:
        #     # 关闭当前标签页
        #     driver.switch_to.window(window_handles[-1])
        #     driver.close()

        # driver.maximize_window()
        page = from_selenium(driver)

        page.set.window.max()
        page.set.window.mini()
        # tab_count = page_count.tabs_count
        while page.tabs_count != 1:
            tab = page.get_tab(id_or_num=2)
            tab.close()

        # os.makedirs(f'./{ROOT_PATH}/{user_id}', exist_ok=True)

        return page


r = Run()


def saveCompleteId(user_id_save, save_platformType):
    # 打开文件并获取锁
    with open(f'txt_path/{save_platformType}_complete_id.txt', 'a') as file:
        msvcrt.locking(file.fileno(), msvcrt.LK_LOCK, 1)  # 获取锁
        file.write(f"{user_id_save}\n")
        msvcrt.locking(file.fileno(), msvcrt.LK_UNLCK, 1)  # 释放锁


site_urls = ["https://www.facebook.com",
             "https://www.instagram.com",
             "https://telegram.org",
             "https://line.me",
             "https://www.snapchat.com",
             "https://www.tumblr.com",
             "https://www.pinterest.com",
             'https://www.linkedin.com',
             'https://vk.com',
             'https://twitter.com/',
             'https://www.skype.com',
             'https://www.viber.com',
             'https://www.imo.in',
             'https://www.crunchbase.com']


# 将user_id存入任务队列中
def operate_google(browser_id_op, model, temp_index, op_platformType):
    selenium_webdriver, selenium_address, user_id = None, None, None
    for _ in range(3):
        try:
            selenium_webdriver, selenium_address, user_id = r.start_userID(user_id=browser_id_op)
            logger.info(f'{selenium_webdriver}----{selenium_address}----{user_id}')
        except Exception as e:
            logger.error(e)
            time.sleep(random.uniform(2, 4))
            continue
        break
    if selenium_webdriver is None:
        logger.error(f'{browser_id_op}连接失败，请检查adspower是否打开')
        return False
    logger.debug(f'{user_id}当前是第{temp_index}台浏览器')
    page = r.start_selenium(selenium_webdriver, selenium_address, user_id)
    logger.info(f'{browser_id_op}   {model}')
    with open('static/keyword/search_keyword.txt', 'r') as file:
        keywords = file.read().splitlines()
    if model == 'search_tel':
        cap_google.search_tel(page, browser_id_op, site_urls[temp_index - 1], random.choice(keywords))

    page.quit()


def start_many_process(browsers, model, start_platformType):
    # 启动多个进程来操作多个浏览器

    processes = []
    count = 1
    for browsers_id in browsers:
        process = multiprocessing.Process(target=operate_google,
                                          args=(browsers_id, model, count, start_platformType))
        processes.append(process)
        process.start()
        count += 1
        time.sleep(5)

    # 等待所有进程完成
    for process in processes:
        process.join()


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
    model_list = ['search_tel', 'search_tel', 'search_tel', 'search_tel']
    operate_index_run = op_i

    # 最大进程数
    # run_maxProcesses = 16
    with open(f'txt_path/{platformType_run}_browser_id.txt', 'r', encoding='utf8') as f_1:
        origin_browser_id_set = set(f_1.read().splitlines())
    try:
        with open(f'txt_path/{platformType_run}_complete_id.txt', 'r', encoding='utf8') as f_2:
            complete_browser_id_set = set(f_2.read().splitlines())
    except FileNotFoundError:
        with open(f'txt_path/{platformType_run}_complete_id.txt', 'w', encoding='utf8') as f_2:
            complete_browser_id_set = set()
        logger.info(f'txt_path/{platformType_run}_complete_id.txt 文件已创建')

    # 去除已完成操作的浏览器
    browser_id_set = origin_browser_id_set - complete_browser_id_set

    numberCycles = math.ceil(len(browser_id_set) / maxProcesses)

    # for count_i in range(numberCycles):
    #     # 随机选取N个浏览器 N = numberOfProcesses
    #     try:
    #         current_browser_id_list = random.sample(list(browser_id_set), k=maxProcesses)
    #     except ValueError:
    #         current_browser_id_list = list(browser_id_set)
    #     start_many_process(current_browser_id_list, model_list[operate_index_run],
    #                        platformType_run)
    #     for repeat_i in current_browser_id_list:
    #         browser_id_set.remove(repeat_i)
    start_many_process(list(origin_browser_id_set), model_list[operate_index_run],
                       platformType_run)

    logger.info('操作已全部完成')
    # reset_complete_txt(platformType_run)


if __name__ == "__main__":
    # 选择浏览器id文件
    platformType = 'google_search'
    start_index = 0
    run(0, platformType_run=platformType, maxProcesses=14)

    # 0 -> 发视频，评论，刷视频; 2 -> 评论，刷视频; 4 -> 刷视频
    # run_loop(start_index, loop_platformType=platformType, reset_video=True)
