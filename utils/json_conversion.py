import json
import os
import time
from datetime import datetime

import pandas as pd
from loguru import logger
from tqdm import tqdm

from utils.decorator import timer


@timer
def extraction_groupInfo(time_date):
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
    for folder_name in tqdm(os.listdir(root_path)):
        if not folder_name.endswith(time_date):
            continue
        for file_name in os.listdir(f'{root_path}/{folder_name}'):
            if not file_name.endswith('.json'):
                continue
            with open(f'{root_path}/{folder_name}/{file_name}', 'r', encoding='utf8') as json_file:
                data = json.load(json_file)
            for group in data:
                temp = group['relay_rendering_strategy']['view_model']['primary_snippet_text_with_entities'][
                    'text'].split(' · ')
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

                # logger.info(f'{temp}---{group_name}---{group_url}')
    x_data = pd.DataFrame(json_temp)
    x_data = x_data.drop_duplicates(subset=['group_url'])
    print(len(x_data))

    os.makedirs(f'{root_path}/00group_csv', exist_ok=True)
    x_data.to_csv(f'{root_path}/00group_csv/group_info_{time_date}.csv', index=False)


@timer
def extraction_userIdInfo(user_id, time_date=None):
    root_path = '../facebook_group/group_memberId'
    json_temp_data = {
        'user_id': set(),
        'message_url': set(),
    }
    for folder_name in tqdm(os.listdir(f'{root_path}')):
        if time_date is not None:
            if not folder_name.endswith(time_date):
                continue
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
def extraction_userIdInfo_from_userFans(time_date=None):
    root_path = '../tiktok_fans'
    userId_set = set()
    for folder_name in tqdm(os.listdir(f'{root_path}/userFans')):
        if time_date is not None:
            if folder_name.endswith(time_date):
                continue
        for file_name in os.listdir(f'{root_path}/userFans/{folder_name}'):
            if file_name.endswith('.json'):
                with open(f'{root_path}/userFans/{folder_name}/{file_name}', 'r', encoding='utf8') as f:
                    temp_json = json.load(f)
                    for userId in temp_json:
                        userId_set.add(userId['user']['uniqueId'] + '\n')
    os.makedirs(f'{root_path}/00userId_txt', exist_ok=True)
    with open(f'{root_path}/00userId_txt/user_info-{time_date}.txt', 'w', encoding='utf8') as f:
        f.writelines(list(userId_set))


@timer
def concat_csv(csv_path, output_file):
    # 初始化一个空的DataFrame来存储所有CSV文件的内容
    frames = []

    # 遍历目录下的所有文件
    for filename in tqdm(os.listdir(csv_path)):
        if filename.endswith(".csv"):
            file_path = os.path.join(csv_path, filename)
            # 读取CSV文件并将内容添加到DataFrame列表中
            data = pd.read_csv(file_path)
            frames.append(data)

    # 合并所有DataFrame对象
    df = pd.concat(frames, ignore_index=True)

    # 删除所有重复数据，不保留任何重复记录
    df.drop_duplicates(keep=False, inplace=True, subset=['message_url'])
    print(len(df))

    # 将合并后的DataFrame保存为新的CSV文件
    df.to_csv(f'{csv_path}/{output_file}', index=False)


def concat_csv11():
    data = pd.read_csv('../facebook_group/group_memberId/00userId_csv/user_info_current-123.csv', encoding='utf8')

    data.drop_duplicates(keep=False, inplace=True, subset=['user_id'])
    print(len(data))

    data.to_csv('aaa.csv', index=False)


def extraction_self_comment(time_date):
    root_path = f'../tiktok_comment/comment_2024-{time_date}'
    comment_count = 0

    for filename in tqdm(os.listdir(root_path)):
        if filename.endswith('.json'):
            with open(f'{root_path}/{filename}', 'r', encoding='utf8') as f:
                temp_json = json.load(f)
            for userId in temp_json:
                if time.time() - float(userId['create_time']) > 60 * 60 * 15:
                    break
                if '$19' in userId['comment']['comment']['text']:
                    comment_count += 1
    print(comment_count)


def extraction_self_userCommentCount(time_date, left_time, right_time):
    """统计指定时间段的评论数量"""
    root_path = f'../tiktok_comment/comment_2024-{time_date}'
    comment_count = 0
    user_set = set()
    user_count_dict = {}

    for filename in tqdm(os.listdir(root_path)):
        if filename.endswith('.json'):
            with open(f'{root_path}/{filename}', 'r', encoding='utf8') as f:
                temp_json = json.load(f)
            # print(temp_json[-1]['create_time'])
            for userId in temp_json:
                # print(userId['create_time'])
                continue_flag = 60 * 60 * left_time < time.time() - float(userId['create_time']) <= 60 * 60 * right_time
                # print(continue_flag)
                if not continue_flag:
                    continue
                # print(userId['comment']['comment']['text'])
                if '$19' in userId['comment']['comment']['text'] or 1 == 1:
                    comment_count += 1
                    user_uniqueid = userId['comment']['comment']['user']['unique_id']
                    if user_uniqueid not in user_set:
                        user_set.add(user_uniqueid)
                        user_count_dict.update({user_uniqueid: 1})
                    else:
                        user_count_dict[user_uniqueid] += 1

    for k, v in user_count_dict.items():
        print(k, v)
        # pass
    time.sleep(0.5)
    logger.info(f'共有{len(user_set)}个账号发出{comment_count}条评论')


def extraction_ins_user():
    """提取ins用户，用户分析采集。默认提取当日数据"""

    root_path = '../ins_data/user_data'
    original_time = datetime.now()
    current_time = f'{original_time.strftime("%Y-%m-%d")}'

    user_set = set()
    for filename in os.listdir(f'{root_path}/{current_time}'):
        if filename.endswith('.json'):
            with open(f'{root_path}/{current_time}/{filename}', 'r', encoding='utf8') as f:
                temp_json = json.load(f)
            for user_info in temp_json['users']:
                has_aaa_key = any(key == 'user' for key in user_info.keys())
                if not has_aaa_key:
                    continue
                if user_info['user']['search_social_context'] is None:
                    # print(user_info['user']['username'])
                    user_name = user_info['user']['username']
                    user_set.add(user_name)
    df_before = {
        'user': list(user_set),
    }
    df = pd.DataFrame(df_before)
    os.makedirs('../ins_data/user_data_csv', exist_ok=True)
    df.to_csv(f'../ins_data/user_data_csv/{current_time}.csv', index=False, encoding='utf-8')


def extraction_ins_fans(data_time=None):
    """提取ins粉丝。默认提取当日数据"""

    root_path = '../ins_data/user_fans'
    if data_time is None:
        original_time_fans = datetime.now()
        data_time = f'{original_time_fans.strftime("%Y-%m-%d")}'

    fans_set = set()
    fans_list = []
    x_count = 0
    for filename in tqdm(os.listdir(f'{root_path}/{data_time}')):
        if filename.endswith('.json'):
            with open(f'{root_path}/{data_time}/{filename}', 'r', encoding='utf8') as f:
                json_temp = json.load(f)
            temp_keys = json_temp['payload']['payloads'].keys()
            for key_1 in temp_keys:
                if filename.split('---')[0] in key_1:
                    break
                temp_name = None
                x_count += 1
                if 'stories' in key_1:
                    temp_name = key_1.split('stories/')[1].split('/')[0]
                elif key_1.endswith('/'):
                    temp_name = key_1.split('/')[1]
                print(temp_name)
                if temp_name not in fans_set and temp_name is not None and len(temp_name) > 1:
                    fans_set.add(temp_name)
                    fans_list.append(temp_name)
    df_before = {
        'user': fans_list
    }
    df = pd.DataFrame(df_before)
    print(len(df))
    print(x_count)
    os.makedirs('../ins_data/user_fans_csv', exist_ok=True)
    df.to_csv(f'../ins_data/user_fans_csv/{data_time}.csv', index=False, encoding='utf-8')


if __name__ == '__main__':
    # 截止2024-04-28---17:14  评论显示824

    # 获取当前日期，只显示月、日 格式为 04-21
    original_time = datetime.now()
    current_time = f'{original_time.strftime("%m-%d")}'

    # 提取ins粉丝数据
    # extraction_ins_fans('2024-04-26')

    # extraction_self_userCommentCount(current_time, 10.5, 15)
    # 46---141
    # 54---158

    # 11833
    # concat_csv11()
    # extraction_userIdInfo_from_userFans(current_time)

    # 同时当日采集的小组成员 只显示新数据

    extraction_userIdInfo(user_id='123', time_date=current_time)
    csv_path = '../facebook_group/group_memberId/00userId_csv'
    concat_csv(csv_path, f'output_{current_time}.csv')
    # extraction_groupInfo('4-17')
