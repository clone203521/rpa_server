import base64
import datetime
import json
import msvcrt
import os
import random
import shutil
import time
from io import BytesIO

import cv2
import ddddocr
import pandas as pd
import requests
from DownloadKit import DownloadKit
from DrissionPage._elements.chromium_element import ChromiumElement
from PIL import Image
from loguru import logger
from requests_toolbelt import MultipartEncoder

t1 = datetime.datetime.now()
ROOT_PATH = '../browserDownload'


# PIL图片保存为base64编码
def PIL_base64(img, coding='utf-8'):
    img_format = img.format
    if img_format == None:
        img_format = 'JPEG'

    format_str = 'JPEG'
    if 'png' == img_format.lower():
        format_str = 'PNG'
    if 'gif' == img_format.lower():
        format_str = 'gif'

    if img.mode == "P":
        img = img.convert('RGB')
    if img.mode == "RGBA":
        format_str = 'PNG'
        img_format = 'PNG'

    output_buffer = BytesIO()
    # img.save(output_buffer, format=format_str)
    img.save(output_buffer, quality=100, format=format_str)
    byte_data = output_buffer.getvalue()
    base64_str = 'data:image/' + img_format.lower() + ';base64,' + base64.b64encode(byte_data).decode(coding)

    return base64_str


def rotate_image_f(outer: ChromiumElement, rotate_user_id):
    url1 = outer.attr('src')
    # print(url1)
    inner_url = outer.next('tag:img').attr('src')
    # print(inner_url)

    down_err_flag = download_img(url1, inner_url, f'{ROOT_PATH}/{rotate_user_id}', 'outer.jpeg', 'inner.jpeg')
    if not down_err_flag:
        logger.error(f'{rotate_user_id}进行旋转图片验证时出现错误，请及时处理')
        return -100

    # discern('./publicPicture/inner.jpeg','./publicPicture/outer.jpeg',isSingle=True)

    # 加载外圈大图
    img1 = Image.open(f'{ROOT_PATH}/{rotate_user_id}/outer.jpeg')
    # 图片转base64
    img1_base64 = PIL_base64(img1)
    # 加载内圈小图
    img2 = Image.open(f'{ROOT_PATH}/{rotate_user_id}/inner.jpeg')
    # 图片转base64
    img2_base64 = PIL_base64(img2)

    # 验证码识别接口
    url = "http://www.detayun.cn/openapi/verify_code_identify/"
    data = {
        # 用户的key
        "key": "Mke2XwTi0JAdZGygvXPw",
        # 验证码类型
        "verify_idf_id": "37",
        # 外圈大图
        "img1": img1_base64,
        # 内圈小图
        "img2": img2_base64,
    }
    header = {"Content-Type": "application/json"}

    # 发送请求调用接口
    response = requests.post(url=url, json=data, headers=header)

    # 获取响应数据，识别结果
    result = response.json()
    logger.info(f'{rotate_user_id}调用旋转验证码接口，返回结果{result}')

    # length = 270 / 360 * result['data']['angle']
    # print(length)
    # print("耗时：", datetime.datetime.now() - t1)

    return result['data']['px_distance']


def download_img(url1, url2, download_user_id, name1, name2):
    def img_fileExists(imgExists_file_path, img_name1, img_name2):
        img_path1 = f'{imgExists_file_path}/{img_name1}'
        img_path2 = f'{imgExists_file_path}/{img_name2}'
        if os.path.exists(img_path1) and os.path.exists(img_path2):
            return True
        else:
            return False

    file_path = f'./{ROOT_PATH}/{download_user_id}'
    del_last_img(file_path, name1, name2)
    d = DownloadKit()

    m1 = d.add(url1, rename=name1, suffix='', goal_path=file_path, file_exists='o')
    m2 = d.add(url2, rename=name2, suffix='', goal_path=file_path, file_exists='o')
    timeout = 2

    func_start_time = time.time()
    while True:
        time.sleep(random.randint(3, 5))
        flag = img_fileExists(file_path, name1, name2)
        func_current_time = time.time()
        if flag:
            break
        if func_current_time - func_start_time > timeout * 60:
            logger.error(f'{download_user_id}图片验证码下载失败，请检查网络')
            return False

    # 读取图像
    img = cv2.imread(f'{file_path}/{name1}')
    img2 = cv2.imread(f'{file_path}/{name2}')

    # 保存图像为指定格式
    cv2.imwrite(f'{file_path}/{name1}', img)
    # 保存图像为指定格式
    cv2.imwrite(f'{file_path}/{name2}', img2)
    return True


def img_valid(user_id):
    det = ddddocr.DdddOcr(det=False, ocr=False, show_ad=False)

    with open(f'./{ROOT_PATH}/{user_id}/puzzle.png', 'rb') as f:
        target_bytes = f.read()

    with open(f'./{ROOT_PATH}/{user_id}/origin.jpeg', 'rb') as f:
        background_bytes = f.read()

    logger.info(f'./{ROOT_PATH}/{user_id}/puzzle.png')

    back_img = Image.open(f'./{ROOT_PATH}/{user_id}/origin.jpeg')

    res = det.slide_match(target_bytes, background_bytes)

    logger.info(res)
    return res['target'][0], back_img.width


def saveCompleteId(user_id_save):
    # 打开文件并获取锁
    with open('tiktok_complete_id.txt', 'a') as file:
        msvcrt.locking(file.fileno(), msvcrt.LK_LOCK, 1)  # 获取锁
        file.write(f"{user_id_save}\n")
        msvcrt.locking(file.fileno(), msvcrt.LK_UNLCK, 1)  # 释放锁


def del_last_img(del_path, del_name1, del_name2):
    try:
        os.remove(f'{del_path}/{del_name1}')
        os.remove(f'{del_path}/{del_name2}')
        logger.info(f'{del_path.split("/")[-1]}删除成功')
    except FileNotFoundError:
        logger.error(f"{del_path}文件不存在，无法删除")


def slideVerif(page_slide, origin_img: ChromiumElement, user_id_temp, model_type):
    logger.info(origin_img.attr('src'))
    puzzle = origin_img.next('tag:img')
    logger.info(puzzle.attr('src'))

    if model_type == 'slide':
        logger.info(f'{user_id_temp}正在进行平移滑块验证')

        flag = download_img(origin_img.attr('src'), puzzle.attr('src'), user_id_temp, 'origin.jpeg', 'puzzle.png')
        if not flag:
            logger.error(f'{user_id_temp}进行图片验证时出现错误，请检查错误原因')
            return False

        # 滑块与空白处的距离
        sliding_length, origin_length = img_valid(user_id_temp)
        # 变换系数
        transformCoefficient = 340 / origin_length
        # pu_transformCoefficient=puzzle_weight/
        fin_drag_length = round(transformCoefficient * sliding_length, 0)
        logger.info(fin_drag_length)
        # return

        # 拖动滑块
        dragBox = page_slide.ele('tag:div@class:secsdk-captcha-drag-icon')
        dragBox.drag(fin_drag_length, 0, 1)
    elif model_type == 'rotate':
        logger.info(f'{user_id_temp}正在进行旋转滑块验证')
        fin_drag_length = rotate_image_f(origin_img, user_id_temp)
        if fin_drag_length < 0:
            logger.error(f'{user_id_temp}进行图片验证时出现错误，请检查错误原因')
            return False

        dragBox = page_slide.ele('tag:div@class:secsdk-captcha-drag-icon')
        dragBox.drag(fin_drag_length, 0, 1.5)
    return True


def validation(page_validation, user_id_validation):
    page_validation.set.NoneElement_value(None)
    start_time = time.time()
    while True:
        counter_flag = 0
        err_flag = True
        # 滑块验证码
        origin_img = page_validation.ele('tag:img@id=captcha-verify-image')
        outer_img = page_validation.ele('tag:img@data-testid=whirl-outer-img')
        if origin_img:
            err_flag = slideVerif(page_validation, origin_img, user_id_validation, 'slide')
        else:
            counter_flag += 1
        if outer_img:
            err_flag = slideVerif(page_validation, outer_img, user_id_validation, 'rotate')
        else:
            counter_flag += 1
        if not err_flag:
            return False
        if counter_flag == 2:
            break
        end_time = time.time()
        if end_time - start_time > 3.5 * 60:
            return False
        time.sleep(10)
    return True


# 视频初始化
def reset_video():
    video_list = os.listdir('../videos')
    folder_list = [name for name in os.listdir(ROOT_PATH) if os.path.isdir(os.path.join(ROOT_PATH, name))]

    for folder, video in zip(folder_list, video_list):
        shutil.move(f'videos/{video}', f'{ROOT_PATH}/{folder}/video_1.mp4')


def rename_video():
    folder_list = [name for name in os.listdir(ROOT_PATH) if os.path.isdir(os.path.join(ROOT_PATH, name))]
    for folder in folder_list:
        video_list = os.listdir(f'{ROOT_PATH}/{folder}')
        for video in video_list:
            if video.find('mp4') != -1:
                os.rename(f'{ROOT_PATH}/{folder}/{video}', f'{ROOT_PATH}/{folder}/video_1.mp4')


def folder_reset():
    temp_dataframe = pd.read_excel('user_list2024-03-27.xlsx')
    with open('../txt_path/upload_video_browser_id.txt_browser_id_1.txt', 'w') as f:
        for i in temp_dataframe['id'][:10]:
            f.write(i + '\n')

    id_json = {}
    for bro_id, index in zip(temp_dataframe['id'][::-1], temp_dataframe['acc_id'][::-1]):
        id_json.update({bro_id: index})
    #
    # with open('browser_id.json', 'w') as f:
    #     json.dump(id_json, f, ensure_ascii=False, indent=4)
    for browser_id in temp_dataframe['id']:
        os.makedirs(f'{ROOT_PATH}/{browser_id}', exist_ok=True)


def move_video():
    def is_folder_empty(folder_path):
        return not os.listdir(folder_path)

    video_list = os.listdir('../videos')
    count = 0
    with open('../txt_path/tiktok_browser_id.txt', 'r') as f:
        browser_ids = [line.strip() for line in f.readlines()]
    for browser_id in browser_ids:
        os.makedirs(f'{ROOT_PATH}/{browser_id}', exist_ok=True)
        shutil.move(f'../videos/{video_list[count]}', f'{ROOT_PATH}/{browser_id}/video_1.mp4')
        count += 1


def run():
    print(121)


def extractData_from_userIdJson():
    userID_jsonNamelist = os.listdir('../listener_data/tiktok_fans/irene93871')
    userId_set = set()

    for userID_jsonName in userID_jsonNamelist:
        with open(f'../listener_data/tiktok_fans/irene93871/{userID_jsonName}', 'r', encoding='utf8') as f:
            origin_data = json.load(f)
            userID_list = origin_data['userList']
        for userID in userID_list:
            temp = f"{userID['user']['uniqueId']}\n"
            if temp not in userId_set:
                userId_set.add(temp)
    with open('../name_data_origin/name.txt', 'w', encoding='utf8') as f:
        f.writelines(userId_set)


def extractData_from_face_txt():
    with open('./facebook_10.txt', 'r', encoding='utf8') as f:
        origin_data = f.readlines()
    origin_json = {
        'id': [],
        'password': [],
        '2fa': [],
        'tel': [],
        'email': [],
        'email_pwd': [],
        'ip_address': []
    }
    for origin in origin_data:
        for line, data_once in zip(origin.split('---'), origin_json):
            origin_json[data_once].append(line.split('：')[1])

    csv_temp = pd.DataFrame(origin_json)
    csv_temp.to_csv('facebook_10.csv', index=False, encoding='utf-8')


def generateImportFile():
    print(1)


def retry_click(origin_ele, click_path) -> bool:
    """重试三次点击
    :param origin_ele: 上级元素
    :param click_path: 点击按钮路径
    :return: 点击事件是否完成
    """
    if isinstance(click_path, list):
        for _temp in range(3):
            pass
    elif isinstance(click_path, str):
        pass

    return True


def gen_fold():
    with open('../txt_path/upload_video_browser_id.txt', 'r') as f:
        id_list = f.readlines()

    for id in id_list:
        os.makedirs(f'{ROOT_PATH}/{id.strip()}', exist_ok=True)


def move_video_txt(txt_name):
    with open(f'./txt_path/{txt_name}_browser_id.txt', 'r') as f:
        id_list = f.readlines()

    count = 1
    video_list = os.listdir('./videos/')
    for b_id in id_list:
        os.makedirs(f'./browserDownload/{b_id.strip()}', exist_ok=True)
        if os.path.exists(f'./browserDownload/{b_id.strip()}/video_1.mp4'):
            continue
        try:
            shutil.move(f'./videos/{video_list[count - 1]}', f'./browserDownload/{b_id.strip()}/video_1.mp4')
        except IndexError:
            logger.error(f'视频消耗完毕，请进行补充')
        count += 1


def save_userId_toTxt(temp_dict: dict, group_id, user_id):
    """保存小组成员ID"""
    current_time = datetime.datetime.now().strftime('%Y-%m-%d')
    detail_time = datetime.datetime.now().strftime('%Y-%m-%d---%H_%M_%S_%f')
    save_path = f'facebook_group/group_memberId/{group_id.split("/groups/")[1][:-1]}_{current_time}'
    os.makedirs(save_path, exist_ok=True)
    logger.info(save_path)
    with open(f'{save_path}/{user_id}--{detail_time}.json', 'w', encoding='utf8') as f:
        json.dump(temp_dict, f, ensure_ascii=False, indent=4)


def save_groupInfo_toJson(temp_dict: dict, key, user_id):
    """保存小组信息"""
    current_time = datetime.datetime.now().strftime('%Y-%m-%d')
    detail_time = datetime.datetime.now().strftime('%Y-%m-%d---%H_%M_%S_%f')
    save_path = f'facebook_group/group_info/{key}_{current_time}'
    os.makedirs(save_path, exist_ok=True)
    # logger.info(save_path)
    with open(f'{save_path}/{user_id}---{detail_time}.json', 'w', encoding='utf8') as f:
        json.dump(temp_dict, f, ensure_ascii=False, indent=4)


def upload_to_feishu(file_path: str, file_name: str, upload_user_id):
    def get_token():
        url_token = 'https://open.feishu.cn/open-apis/auth/v3/app_access_token/internal'
        headers_token = {'Content-Type': 'application/json; charset=utf-8'}
        data_token = {
            "app_id": "cli_a68d3f21d57a1013",
            "app_secret": "daAf9wa7D2FKkzTQcbRohgjhZvZE2CEk"
        }
        response_token = requests.request(method='POST', url=url_token, headers=headers_token, data=data_token)
        logger.info(response_token.json())
        return response_token.json()['tenant_access_token']

    with open(f'{file_path}/{file_name}', 'rb') as f:
        file_data = f.read()
    upload_url = 'https://open.feishu.cn/open-apis/drive/v1/files/upload_all'

    headers = {
        'Authorization': f'Bearer {get_token()}'
    }
    data = {
        'file_name': file_name,
        'parent_type': 'explorer',
        'parent_node': 'PdWBfIHuylMtkodkIJPchKQInMc',
        'size': str(len(file_data)),
        'file': file_data
    }
    multi_form = MultipartEncoder(data)
    headers['Content-Type'] = multi_form.content_type
    response = requests.request('POST', upload_url, headers=headers, data=multi_form)

    try:
        if response.json()['msg'] == 'success':
            logger.info(f'{upload_user_id}文件上传成功')
            return True
    except Exception as e:
        logger.error(e)
    logger.error(f'{upload_user_id}发送失败')
    logger.info(response.json())


def save_userFans_toJson(temp_dict: dict, user_name, user_id_fans):
    current_time = datetime.datetime.now().strftime('%Y-%m-%d')
    detail_time = datetime.datetime.now().strftime('%Y-%m-%d---%H_%M_%S_%f')
    save_path = f'tiktok_fans/userFans/{user_name}_{current_time}'
    os.makedirs(save_path, exist_ok=True)
    # logger.info(save_path)
    with open(f'{save_path}/{user_id_fans}---{detail_time}.json', 'w', encoding='utf8') as f:
        json.dump(temp_dict, f, ensure_ascii=False, indent=4)


def gen_csv():
    x = ["https://www.tiktok.com/@nvnciv",
         "https://www.tiktok.com/@ponhuluxuries",
         "https://www.tiktok.com/@sellierluxurybags",
         "https://www.tiktok.com/@bagista.uk",
         "https://www.tiktok.com/@lux_mommy",
         "https://www.tiktok.com/@luxe_cheshire",
         "https://www.tiktok.com/@minhcdealrz",
         "https://www.tiktok.com/@melissalovesbags",
         "https://www.tiktok.com/@iitsninaaaaa",
         "https://www.tiktok.com/@norascollection1", ]
    data = {
        'user_url': x
    }
    df = pd.DataFrame(data)
    df.to_csv('test.csv', index=False)


def get_target_value(key, dic, tmp_list) -> list:
    """
    :param key: 目标key值
    :param dic: JSON数据
    :param tmp_list: 用于存储获取的数据
    :return: list
    """
    if not isinstance(dic, dict) or not isinstance(tmp_list, list):  # 对传入数据进行格式校验
        print('argv[1] not an dict or argv[-1] not an list ')
        return []

    if key in dic.keys():
        tmp_list.append(dic[key])  # 传入数据存在则存入tmp_list

    for value in dic.values():  # 传入数据不符合则对其value值进行遍历
        if isinstance(value, dict):
            get_target_value(key, value, tmp_list)  # 传入数据的value值是字典，则直接调用自身
        elif isinstance(value, (list, tuple)):
            _get_value(key, value, tmp_list)  # 传入数据的value值是列表或者元组，则调用_get_value

    return tmp_list


def _get_value(key, val, tmp_list):
    for val_ in val:
        if isinstance(val_, dict):
            get_target_value(key, val_, tmp_list)  # 传入数据的value值是字典，则调用get_target_value
        elif isinstance(val_, (list, tuple)):
            _get_value(key, val_, tmp_list)  # 传入数据的value值是列表或者元组，则调用自身


def extract_comment(origin_data):
    if not isinstance(origin_data, dict):
        origin_data = origin_data.split('\n')
        data = {
            'list': [json.loads(once) for once in origin_data if len(once) != 0]
        }
    else:
        data = origin_data
    result_list = get_target_value('interesting_top_level_comments', data, [])

    final_list = chouqu_test(result_list)
    return final_list


def json_test11():
    with open('a11.txt', 'r', encoding='utf8') as f:
        origin_data = f.read().split('\n')
    print(len(origin_data))

    data = {
        'list': [json.loads(once) for once in origin_data if len(once) != 0]
    }
    result_list = get_target_value('interesting_top_level_comments', data, [])
    # with open('a13.json', 'w', encoding='utf8') as f:
    #     json.dump(result_list, f, ensure_ascii=False, indent=4)
    # print(len(result_list))
    result_list = chouqu_test(result_list)
    return result_list


temp_set = set()
temp_user = set()

def chouqu_test(data=None):
    if data is None:
        with open('a13.json', 'r', encoding='utf8') as f:
            data = json.load(f)
    result_list = []
    with open('utils/face_keyword.txt', 'r', encoding='utf8') as f:
        keyword_set = set(f.read().split('\n'))
    current_time = time.time()
    for value in data:
        try:
            temp = value[0]
            text = get_target_value('body', temp, [])[0]['text']
        except (KeyError, IndexError, TypeError):
            continue
        user_id = temp['comment']['author']['id']
        create_time = get_target_value('created_time', temp, [])[0]
        _temp_data = f'{text}---{user_id}---{create_time}'
        if _temp_data not in temp_set:
            logger.info(f'评论: {text}')
        temp_set.add(_temp_data)
        if current_time - create_time < 60 * 60 * 2:
            logger.info(f'这是一条2小时内的评论数据: {text}')
        for keyword in keyword_set:
            if keyword in text.lower() and (current_time - create_time < 60 * 60 * 2) and user_id not in temp_user:
                temp_user.add(user_id)
                result_list.append(user_id)
                logger.info(f'{text}---{user_id}---{datetime.datetime.fromtimestamp(create_time):%Y-%m-%d %H:%M:%S}')
                break
        # if (text.lower() in keyword_set) and (current_time - create_time < 60 * 10):
        #     result_list.append(user_id)
        #     logger.info(f'{text}---{user_id}---{datetime.datetime.fromtimestamp(create_time):%Y-%m-%d %H:%M:%S}')
        # print(time.time() - create_time)
    return result_list


def excel_open_toCsv():
    _temp_excel = pd.read_excel('fb_account2.xlsx')
    print(_temp_excel)
    _temp_excel['2fa'] = [fa.split('/code/')[1] for fa in _temp_excel['2fa']]

    _temp_excel.to_csv('fb_account2.csv', index=False)


if __name__ == '__main__':
    excel_open_toCsv()
    # print(time.time())
    # if 2 == 2 and 3 == 3:
    #     print(125)
    # json_test11()
    # chouqu_test()

    # gen_csv()
    # upload_to_feishu('facebook_10.csv', 'facebook_10.csv', '124542')
    # move_video_txt('tik_all')
    # gen_fold()
    # rotate_image_f()
    # reset_video()

    # extractData_from_userIdJson()

    # rename_video()
    # folder_reset()
    # move_video()
    # extractData_from_userIdJson()
    # logger.info('121')
    # extractData_from_face_txt()
    # run()
