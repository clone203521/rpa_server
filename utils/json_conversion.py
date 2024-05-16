import json
import os
import re
import time
from datetime import datetime

import pandas as pd
import requests
from loguru import logger
from tqdm import tqdm

from utils.decorator import timer


@timer
def extraction_groupInfo(time_date):
    def filter_qualified_group(filter_csv_path):
        df = pd.read_csv(filter_csv_path)

        drop_index = []
        # filtered_strings = []
        # 选择成员大于5000的字符串
        for index in df.index:
            # 提取成员数量
            temp_str = df['group_members'][index]
            member_count_str = re.match(r'^[0-9,.]*', temp_str).group(0)
            # print(member_count_str)
            if not member_count_str:
                continue
            if '万' in temp_str:
                if float(member_count_str) < 1.5:
                    drop_index.append(index)
            elif ',' in temp_str:
                drop_index.append(index)
            elif member_count_str:
                if float(member_count_str) < 15000:
                    drop_index.append(index)

        df.drop(drop_index, axis=0, inplace=True)
        print(f'符合条件的小组个数{len(df)}')

        df.to_csv(f'{filter_csv_path[:-4]}_filter.csv', index=False)

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
                try:
                    temp = group['relay_rendering_strategy']['view_model']['primary_snippet_text_with_entities'][
                        'text'].split(' · ')
                except KeyError:
                    continue
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
    print(f'筛选前小组个数:{len(x_data)}')

    save_path = f'../facebook_group/group_csv'
    os.makedirs(save_path, exist_ok=True)
    x_data.to_csv(f'{save_path}/group_info_{time_date}.csv', index=False)
    filter_qualified_group(f'{save_path}/group_info_{time_date}.csv')


@timer
def extraction_userIdInfo(time_date):
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
    os.makedirs(f'../facebook_group/message_userId_csv', exist_ok=True)
    temp_data.to_csv(f'../facebook_group/message_userId_csv/output_{time_date}.csv', index=False)


@timer
def extraction_userIdInfo_to_sendGroup(time_date):
    root_path = '../facebook_group/group_memberId'
    json_temp_data = {
        'user_id': [],
    }
    user_id_set = set()
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
                                    temp_user_id = userId['node']['url'].split('www.facebook.com/')[1]
                                    if '?id=' not in userId['node']['url'] and temp_user_id not in user_id_set:
                                        user_id_set.add(temp_user_id)
                                        json_temp_data['user_id'].append(f'{temp_user_id}')
                        except KeyError:
                            continue
    json_temp_data['user_id'] = list(json_temp_data['user_id'])

    temp_data = pd.DataFrame(json_temp_data)

    save_path = f'../facebook_group/send_group'
    os.makedirs(save_path, exist_ok=True)
    temp_data.to_csv(f'{save_path}/output_{time_date}.csv', index=False)

    concat_csv(save_path, f'output_{current_time}.csv', 'user_id', time_date)


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
def concat_csv(csv_path_con, output_file, column_name, current_time_con=None):
    original_time_con = datetime.now()
    if current_time_con is None:
        current_time_con = f'{original_time_con.strftime("%m-%d")}'
    origin_csv = pd.read_csv(f'{csv_path_con}/output_{current_time_con}.csv')
    origin_user_set = set(origin_csv[column_name].to_list())
    print(f'去重前:{len(origin_user_set)}')

    # 初始化一个空的DataFrame来存储所有CSV文件的内容
    frames = []

    # 遍历目录下的所有文件
    for filename in tqdm(os.listdir(csv_path_con)):
        if filename.endswith(".csv") and not filename.endswith(f'{current_time_con}.csv'):
            file_path = os.path.join(csv_path_con, filename)
            # 读取CSV文件并将内容添加到DataFrame列表中
            data = pd.read_csv(file_path)
            frames.append(data)

    # 合并所有DataFrame对象
    df = pd.concat(frames, ignore_index=True)
    before_user_set = set(df[column_name].to_list())

    after_user_set = origin_user_set - before_user_set

    after_json = {column_name: list(after_user_set)}
    after_df = pd.DataFrame(after_json)

    # 删除所有重复数据，不保留任何重复记录
    # df.drop_duplicates(keep=False, inplace=True, subset=['message_url'])
    print(f'去重后:{len(after_user_set)}')

    save_file_path = f'{csv_path_con}/{output_file}'
    # if os.path.exists(save_file_path):
    #     time_now = datetime.now()
    #     no_repeat_str = time_now.strftime("%H_%M_%S")
    #     save_file_path = f'{save_file_path[:-4]}_{no_repeat_str}.csv'

    after_df.to_csv(save_file_path, index=False)
    # 将合并后的DataFrame保存为新的CSV文件


def extraction_self_userCommentCount(time_date):
    """统计指定时间段的评论数量"""
    temp_input = input('请输入左右界限: ')
    left_time, right_time = float(temp_input.split(' ')[0]), float(temp_input.split(' ')[1])
    root_path = f'../tiktok_comment/comment_2024-{time_date}'
    comment_count = 0
    user_set = set()
    user_count_dict = {}

    for filename in tqdm(os.listdir(root_path)):
        if filename.endswith('.json'):
            with open(f'{root_path}/{filename}', 'r', encoding='utf8') as f:
                temp_json = json.load(f)

            for userId in temp_json:
                continue_flag = 60 * 60 * left_time < time.time() - float(userId['create_time']) <= 60 * 60 * right_time
                if not continue_flag:
                    continue

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

    def no_repeat_ins_fans(current_time_norepeat):
        csv_path_ins_fans = '../ins_data/user_fans_csv'
        original_time_con = datetime.now()
        current_time_all = original_time_con.strftime("%Y-%m-%d")
        df_current = pd.read_csv(f'{csv_path_ins_fans}/{current_time_all}.csv')

        frames = []

        for filename_re in os.listdir(csv_path_ins_fans):
            if filename_re.endswith(f'{current_time_norepeat}.csv'):
                continue
            file_path = os.path.join(csv_path_ins_fans, filename_re)
            # 读取CSV文件并将内容添加到DataFrame列表中
            data = pd.read_csv(file_path)
            frames.append(data)

        # 合并所有DataFrame对象
        df_no_ins = pd.concat(frames, ignore_index=True)
        before_fans_set = set(df_no_ins['user'].to_list())
        current_fans_set = set(df_current['user'].to_list())

        after_fans_set = current_fans_set - before_fans_set
        df_temp_json = {
            'user': list(after_fans_set),
        }
        print(len(current_fans_set))
        print(len(after_fans_set))

        df_temp = pd.DataFrame(df_temp_json)
        df_temp.to_csv(f'{csv_path_ins_fans}/{current_time_all}.csv', index=False)

    root_path = '../ins_data/user_fans'
    if data_time is None or 1 == 1:
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
                if 'stories/' in key_1:
                    temp_name = key_1.split('stories/')[1].split('/')[0]
                elif key_1.endswith('/'):
                    temp_name = key_1.split('/')[1]
                if temp_name not in fans_set and temp_name is not None and len(temp_name) > 1:
                    fans_set.add(temp_name)
                    fans_list.append(temp_name)
    df_before = {
        'user': fans_list
    }
    df = pd.DataFrame(df_before)
    os.makedirs('../ins_data/user_fans_csv', exist_ok=True)
    df.to_csv(f'../ins_data/user_fans_csv/{data_time}.csv', index=False, encoding='utf-8')

    no_repeat_ins_fans(current_time_norepeat=data_time)


def extraction_ws_tel(current_time_ws_tel=None):
    print(current_time_ws_tel)
    current_tel_set = set()
    all_tel_set = set()

    for filename in os.listdir(f'../ws_tel/{current_time_ws_tel}'):
        if filename.endswith('.txt'):
            with open(f'../ws_tel/{current_time_ws_tel}/{filename}', 'r', encoding='utf8') as f:
                current_tel_set.update(set(f.read().splitlines()))

    for folder_name in tqdm(os.listdir(f'../ws_tel')):
        if folder_name.endswith(current_time_ws_tel) or '-' not in folder_name:
            continue
        for filename in os.listdir(f'../ws_tel/{folder_name}'):
            if filename.endswith('.txt'):
                with open(f'../ws_tel/{folder_name}/{filename}', 'r', encoding='utf8') as f:
                    temp_tel = f.read().splitlines()
                    all_tel_set.update(set(temp_tel))
    result_set = current_tel_set - all_tel_set

    logger.debug(f'当日共获取电话{len(current_tel_set)}条，往日共获取{len(all_tel_set)}条')

    logger.success(f'当日获取新电话{len(result_set)}个')

    os.makedirs('../ws_tel/ws_tel_txt', exist_ok=True)
    with open(f'../ws_tel/ws_tel_txt/{datetime.now().year}-{current_time_ws_tel}.txt', 'w', encoding='utf8') as f:
        f.write('\n'.join(result_set))


def add_new_tag():
    with open('../txt_path/tik_all_browser_id.txt', 'r', encoding='utf8') as f:
        all_tik_all_browser_id = f.read().splitlines()

    for tik_all_browser_id in all_tik_all_browser_id:
        send_data = {
            'bro_name': tik_all_browser_id,
            'tag': 'Tk正常账号'
        }
        requests.post(url=f'http://fbmessage.v7.idcfengye.com/addTag', json=send_data)


@timer
def extraction_userFri(time_date_fri=None):
    root_path_fri = '../facebook_group/group_memberId'
    json_temp_data = {
        'fri_url': set(),
    }
    for folder_name in tqdm(os.listdir(f'{root_path_fri}')):
        if time_date_fri is not None:
            if not folder_name.endswith(time_date_fri):
                continue
        for file_name in os.listdir(f'{root_path_fri}/{folder_name}'):
            if file_name.endswith('.json'):
                with open(f'{root_path_fri}/{folder_name}/{file_name}', 'r', encoding='utf8') as f:
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
                                    json_temp_data['fri_url'].add(userId['node']['url'])
                        except KeyError:
                            continue
    json_temp_data['fri_url'] = list(json_temp_data['fri_url'])
    temp_data = pd.DataFrame(json_temp_data)
    print(len(json_temp_data))

    save_path = f'../facebook_group/fri_url_csv'
    os.makedirs(save_path, exist_ok=True)
    temp_data.to_csv(f'{save_path}/output_{time_date_fri}.csv', index=False)

    concat_csv(save_path, f'output_{current_time}.csv', 'fri_url', time_date_fri)


def check_function(check_current_time):
    def ex_currentTime_group_members(current_time_ecgm):
        extraction_userIdInfo(time_date=current_time_ecgm)
        csv_path = '../facebook_group/message_userId_csv'
        concat_csv(csv_path, f'output_{current_time_ecgm}.csv', 'message_url', current_time_ecgm)

    funcs_json = [extraction_ws_tel, extraction_self_userCommentCount, ex_currentTime_group_members,
                  extraction_ins_fans, extraction_groupInfo, extraction_userIdInfo_to_sendGroup, extraction_userFri]
    while True:
        print('1.提取ws群组号码')
        print('2.提取Tk主号评论')
        print('3.提取Fb小组成员')
        print('4.提取Ins粉丝数据')
        print('5.提取Fb小组信息')
        print('6.提取Fb用户id 用于群发')
        print('7.提取Fb用户id 用于加好友')
        check_func_index = input('请输入函数编号:')
        if int(check_func_index) < 1:
            break
        funcs_json[int(check_func_index) - 1](check_current_time)

    # 截止2024-04-28---17:14  评论显示824
    # 截止2024-04-29---08:43  评论显示1143
    # 截止2024-04-30---08:42  评论显示358
    # 截止2024-05-05---08:42  评论显示1670
    # 截止2024-05-06---08:29  评论显示288
    # 截止2024-05-08---08:44  评论显示509
    # 截止2024-05-09---09:38  评论显示325
    # 截止2024-05-11---09:11  评论显示270


if __name__ == '__main__':
    # extraction_userFri()
    # add_new_tag()
    # 获取当前日期，只显示月、日 格式为 04-21
    original_time = datetime.now()
    current_time = f'{original_time.strftime("%m-%d")}'
    current_time = '05-14'
    check_function(current_time)
    # 提取ins粉丝数据
    # extraction_ins_fans('2024-04-26')

    # extraction_self_userCommentCount(current_time)
    # 46---141
    # 54---158

    # 11833
    # concat_csv11()
    # extraction_userIdInfo_from_userFans(current_time)

    # 同时当日采集的小组成员 只显示新数据

    # extraction_groupInfo('4-17')
