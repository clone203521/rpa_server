import json
import math
import os
import re
import time

import pandas as pd
from loguru import logger
from tqdm import tqdm

import my_utils
from utils.decorator import timer


@timer
def extraction_groupInfo():
    def determine_post_type(post_str: str):
        if 'post' in post_str and 'day' in post_str:
            return post_str
        elif '日' in post_str:
            return post_str
        return None

    root_path = '../facebook_group/group_info'
    json_temp = {
        'group_name': [],
        'group_url': [],
        'group_members': [],
        'group_day_post': []
    }
    count = 1
    for folder_name in os.listdir(root_path):
        for file_name in os.listdir(f'{root_path}/{folder_name}'):
            if not file_name.endswith('.json'):
                continue
            with open(f'{root_path}/{folder_name}/{file_name}', 'r', encoding='utf8') as json_file:
                data = json.load(json_file)
            for group in data:
                temp = group['relay_rendering_strategy']['view_model']['primary_snippet_text_with_entities'][
                    'text'].split(
                    ' · ')
                if not (temp[0] == '公开' or temp[0] == 'Public'):
                    continue
                info_temp = group['relay_rendering_strategy']['view_model']['loggedProfile']
                group_name = info_temp['name']
                group_url = info_temp['url']
                # logger.info(f'{temp}---{group_name}---{group_url}')

                try:
                    if '10' not in temp[2]:
                        continue
                except IndexError:
                    continue
                if group_name in json_temp['group_url']:
                    continue
                if 'K' in temp[1]:
                    # logger.info(temp)
                    temp_number = float(temp[1].split('K')[0]) / 10
                    temp[1] = f'{round(temp_number, 1)}万位成员'
                try:
                    temp_post = determine_post_type(temp[2])
                    if temp_post is None:
                        continue
                    json_temp['group_day_post'].append(temp_post)
                    json_temp['group_name'].append(group_name)
                    json_temp['group_url'].append(group_url)
                    json_temp['group_members'].append(temp[1])
                except Exception as e:
                    logger.warning(e)
                    continue

                logger.info(f'{temp}---{group_name}---{group_url}')
    x_data = pd.DataFrame(json_temp)
    x_data = x_data.drop_duplicates(subset=['group_url'])
    print(x_data)

    os.makedirs(f'{root_path}/00group_csv', exist_ok=True)
    x_data.to_csv(f'{root_path}/00group_csv/group_info_all_norepeat.csv', index=False)


@timer
def extraction_userIdInfo(user_id):
    root_path = '../facebook_group/group_memberId'
    json_temp_data = {
        'user_id': set(),
        'message_url': set(),
    }
    for folder_name in tqdm(os.listdir(f'{root_path}')):
        for file_name in os.listdir(f'{root_path}/{folder_name}'):
            # logger.info(f'{root_path}/{folder_name}/{file_name}')
            if file_name.endswith('.json'):
                with open(f'{root_path}/{folder_name}/{file_name}', 'r', encoding='utf8') as f:
                    temp_json = json.load(f)
                    try:
                        userId_list = temp_json['data']['node']['new_members']['edges']
                    except KeyError as e:
                        continue
                    for userId in userId_list:
                        try:
                            if userId['node']['user_type_renderer'] is not None and \
                                    userId['node']['user_type_renderer']['__typename'] == 'FacebookUserRenderer':
                                if userId['node']['user_type_renderer']['user']['friendship_status'] == 'CAN_REQUEST':
                                    json_temp_data['user_id'].add(userId['node']['id'])
                                    json_temp_data['message_url'].add(
                                        f"https://www.facebook.com/messages/t/{userId['node']['id']}")
                        except KeyError:
                            continue
    json_temp_data['user_id'] = list(json_temp_data['user_id'])
    json_temp_data['message_url'] = list(json_temp_data['message_url'])
    temp_data = pd.DataFrame(json_temp_data)
    os.makedirs(f'{root_path}/00userId_csv', exist_ok=True)
    temp_data.to_csv(f'{root_path}/00userId_csv/user_info_current-{user_id}.csv', index=False)
    # my_utils.upload_to_feishu(f'{root_path}/userId_csv', 'user_info.csv', user_id)


@timer
def extraction_userIdInfo_from_userFans(user_id):
    root_path = '../tiktok_fans'
    userId_set = set()
    for folder_name in os.listdir(f'{root_path}/userFans'):
        for file_name in os.listdir(f'{root_path}/userFans/{folder_name}'):
            if file_name.endswith('.json'):
                with open(f'{root_path}/userFans/{folder_name}/{file_name}', 'r', encoding='utf8') as f:
                    temp_json = json.load(f)
                    for userId in temp_json:
                        userId_set.add(userId['user']['uniqueId'] + '\n')
    os.makedirs(f'{root_path}/00userId_txt')
    with open(f'{root_path}/00userId_txt/user_info.txt', 'w', encoding='utf8') as f:
        f.writelines(list(userId_set))


@timer
def concat_csv(csv_path, output_file):
    # 初始化一个空的DataFrame来存储所有CSV文件的内容
    frames = []

    # 遍历目录下的所有文件
    for filename in os.listdir(csv_path):
        if filename.endswith(".csv"):
            file_path = os.path.join(csv_path, filename)
            # 读取CSV文件并将内容添加到DataFrame列表中
            data = pd.read_csv(file_path)
            frames.append(data)

    # 合并所有DataFrame对象
    df = pd.concat(frames, ignore_index=True)

    # 删除所有重复数据，不保留任何重复记录
    df.drop_duplicates(keep=False, inplace=True, subset=['user_id'])
    print(len(df))

    # 将合并后的DataFrame保存为新的CSV文件
    df.to_csv(output_file, index=False)


if __name__ == '__main__':
    # extraction_userIdInfo_from_userFans(2)
    extraction_userIdInfo('123456')
    csv_path = '../facebook_group/group_memberId/00userId_csv'
    concat_csv(csv_path, 'output.csv')
    # extraction_groupInfo()

