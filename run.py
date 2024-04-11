import inspect
import os
import random
import threading

import pandas as pd
from flask import Flask, render_template, request
from flask_cors import CORS
from loguru import logger

import database_util as dbu
import listener_facebook_process as listen_face
import open_broswer as open_b
from models import AccessRecord, db

app = Flask(__name__, template_folder='templates')
app.config.from_object('config.Config')
db.init_app(app)
dbs = db.session
local_url = 'http://fbmessage.v7.idcfengye.com'

CORS(app)  # 启用 CORS 支持

# 创建应用上下文
with app.app_context():
    # 在应用上下文中执行数据库操作
    db.create_all()


@app.route('/')
def hello():
    # return f"<span id='id_test' style='font-size:100px;'><strong>当前已访问{count-1}个浏览器"
    # 查询数据库以获取访问记录总数
    total_access_count = AccessRecord.query.with_entities(db.func.sum(AccessRecord.count)).scalar() + 1931
    data = {
        'count': total_access_count,
        'les_count': len(os.listdir('user_id_txt')) - total_access_count,
    }

    return render_template('index.html', data=data)


@app.route('/add_info', methods=['GET', 'POST'])
def add_info():
    # ip_address = request.remote_addr
    bro_list = pd.read_excel('./bro_list.xlsx')

    for bro in range(len(bro_list)):
        print(bro_list['tags'][bro])
        try:
            tags = bro_list['tags'][bro].replace('"', '')
        except AttributeError:
            tags = None
        dbu.add_browser(bro_list["acc_id"][bro], bro_list['id'][bro], bro_list['group'][bro],
                        tags, bro_list['ip'][bro], bro_list['countrycode'][bro])

    return {'msg': '添加成功', 'status_code': 'success'}


@app.route('/update_table', methods=['GET', 'POST'])
def update_table():
    db.create_all()
    return {'msg': '更新成功', 'statu_code': 'success'}


@app.route('/execution_method', methods=['GET', 'POST'])
def execution_method():
    model_list_face_run = ['get_group_info', 'get_group_userId', 'listen_group_comment']

    def long_running_task(_browser_list):
        with app.app_context():
            # # 模拟一个耗时的函数
            import time
            for browser in _browser_list:
                dbu.update_browser_status(browser, random.randint(1, 2))
                time.sleep(random.randint(3, 5))
        logger.info("耗时函数执行完成")

    def open_browser_task(_browser_list):
        with app.app_context():
            for browser in _browser_list:
                open_b.open_browser(browser)

    def listen_fb_comment(_browser_list, _maxProcesses):
        with app.app_context():
            # write_list=
            current_function = inspect.stack()[1].function
            with open(f'txt_path/{current_function}_browser_id.txt', 'w') as f:
                f.write('\n'.join(_browser_list))
            listen_face.run(2, current_function, _maxProcesses, 0)

    data = request.get_json()['data']
    logger.info(data)
    if 'send_func_value' not in data or data['send_func_value'] == '':
        return {'msg': '请选择操作方法', 'statu_code': 'warning'}
    method = data['send_func_value']
    browser_list = data['sendBroList']
    maxProcesses = int(data['send_maxProcesses'])
    if len(browser_list) == 1 and browser_list[0] == '':
        return {'msg': '请选择浏览器', 'statu_code': 'warning'}

    logger.info(method)
    logger.info(browser_list)
    if method == 'test1':
        threading.Thread(target=long_running_task, args=(browser_list,)).start()
        msg = '随机修改状态任务已提交'
    elif method == 'open_browser':
        threading.Thread(target=open_browser_task, args=(browser_list,)).start()
        msg = '打开浏览器'
    elif method == 'tk_brushVideo':
        threading.Thread(target=open_browser_task, args=(browser_list,)).start()
        msg = 'Tiktok养号'
    elif method == 'tk_uploadVideo':
        threading.Thread(target=open_browser_task, args=(browser_list,)).start()
        msg = 'Tiktok上传视频'
    elif method == 'tk_comment':
        threading.Thread(target=open_browser_task, args=(browser_list,)).start()
        msg = 'Tiktok评论'
    elif method == 'fb_brushPost':
        threading.Thread(target=open_browser_task, args=(browser_list,)).start()
        msg = 'Facebook养号'
    elif method == 'listen_fb_comment':
        threading.Thread(target=listen_fb_comment, args=(browser_list,maxProcesses)).start()
        msg = 'Facebook监控小组评论'
    elif method == 'get_fb_newMember':
        threading.Thread(target=open_browser_task, args=(browser_list, maxProcesses,)).start()
        msg = 'Fb获取小组新人'
    elif method == 'get_fb_groupInfo':
        threading.Thread(target=open_browser_task, args=(browser_list,)).start()
        msg = 'Fb获取小组信息'
    else:
        return {'msg': 'error', 'statu_code': 'error'}

    return {'msg': f'{msg}任务已提交', 'statu_code': 'success'}


@app.route('/delete_tags', methods=['GET', 'POST'])
def delete_tags():
    request_id = request.args.get('id')
    print(request_id)
    return {'msg': '删除成功', 'status_code': 'success'}


def get_dates():
    return sorted(set(record.access_date for record in AccessRecord.query.all()))


def get_ips():
    return sorted(set(record.ip_address for record in AccessRecord.query.all()))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9777, debug=True)
