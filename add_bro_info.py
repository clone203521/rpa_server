import re

import pandas as pd
import requests


def add_account_info():
    data = pd.read_csv('utils/fb_acc2.csv')
    for _, row in data.iterrows():
        x = re.search(r"(\d+)", row['fb_id']).group(1)
        # print(x)
        send_data = {
            'email': row.email,
            'password': row['password'],
            'fb_id': x,
            'fa_2': row['2fa']
        }
        # print(send_data)
        response = requests.post('http://127.0.0.1:12144/add_FbAccount', json=send_data)
        print(response.json()['msg'])


def get_pwd(acc_id_g):
    send_data = {
        'id': acc_id_g
    }
    response = requests.post('http://127.0.0.1:12144/get_FbPwd', json=send_data)
    print(response.json()['msg'])
    # print(response.json()['msg'])


def add_account_info_txt():
    with open('utils/a11.txt', 'r', encoding='utf8') as f:
        data = f.read().split('\n')
    for row in data:
        # x = re.search(r"(\d+)", row['fb_id']).group(1)
        # print(x)
        send_data = {
            'email': row.split('邮箱：')[1].split('---')[0],
            'password': row.split('密码：')[1].split('---')[0],
            'fb_id': row.split('ID：')[1].split('---')[0],
            'fa_2': row.split('密钥：')[1].split('---')[0],
        }
        # print(send_data)
        response = requests.post('http://127.0.0.1:12144/add_FbAccount', json=send_data)
        print(response.json()['msg'], end=' ')
        send_data = {
            'id': row.split('ID：')[1].split('---')[0]
        }
        response = requests.post('http://127.0.0.1:12144/get_FbPwd', json=send_data)
        print(response.json()['msg'])


def no_repeat():
    with open('00temp.log', 'r', encoding='utf8') as f:
        data = set(f.read().split('\n'))
    with open('00temp.log', 'w', encoding='utf8') as f:
        for i in data:
            f.write(i + '\n')


def add_tag():
    with open('00temp.log', 'r', encoding='utf8') as f:
        data = set(f.read().split('\n'))
        for i in data:
            data = {
                'bro_name': i,
                'tag': '代理中断'
            }
            requests.post('http://fbmessage.v7.idcfengye.com/addTag', json=data)


def gen_csv():
    with open('00temp.log', 'r', encoding='utf8') as f:
        data = f.read().split('\n')
    df = pd.DataFrame({'group_url': data})
    df.to_csv('00temp.csv', index=False)
    print('----------------')


if __name__ == '__main__':
    # gen_csv()
    x = 'Howzit! LV: does it look legit?'
    x1 = x[:20]
    x2 = x[20:]
    print(x1)
    print()

    print(x2)
    # no_repeat()
    # add_tag()
    # add_account_info_txt()
    # acc_id = '61557217004604'
    # get_pwd(acc_id)
