import json
import msvcrt
import random
import time

import requests
from DrissionPage.common import from_selenium
from loguru import logger
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


class Run:
    def __init__(self):
        self.finger_headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }
        self.finger_url = 'http://local.adspower.com:50325'

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
        page.wait(0.5)
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
def operate_facebook_listener(browser_id_op, model, temp_index, add_index, op_platformType, op_length):
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


def open_browser(browser_id_op):
    selenium_webdriver, selenium_address, user_id = None, None, None
    for _ in range(3):
        try:
            selenium_webdriver, selenium_address, user_id = r.start_userID(user_id=browser_id_op)
            logger.info(f'{selenium_webdriver}----{selenium_address}----{user_id}')
        except:
            time.sleep(random.uniform(2, 4))
            continue
        break
    if selenium_webdriver is None:
        logger.error(f'{browser_id_op}连接失败，请检查adspower是否打开')
    return False
