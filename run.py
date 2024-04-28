import os
import random
import threading
import time

import pandas as pd
import requests
from flask import Flask, render_template, request
from flask_cors import CORS
from loguru import logger

import database_util as dbu
import listener_facebook_process as listen_face
import listener_tiktok_process as listen_tiktok
import open_broswer as open_b
import run_peocess_ins as run_ins
import run_process as run_tk
import run_process_face as run_face
import run_process_ws as run_ws
from models import AccessRecord, db
from utils import my_utils

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
    # return f"<span id='id_test' style='font-size:100px;'><strong>当前已访问{run_count-1}个浏览器"
    # 查询数据库以获取访问记录总数
    total_access_count = AccessRecord.query.with_entities(db.func.sum(AccessRecord.count)).scalar() + 1931
    data = {
        'run_count': total_access_count,
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
        dbu.add_browser(bro_list["acc_id_g"][bro], bro_list['id'][bro], bro_list['group'][bro],
                        tags, bro_list['ip'][bro], bro_list['countrycode'][bro])

    return {'msg': '添加成功', 'status_code': 'success'}


@app.route('/update_table', methods=['GET', 'POST'])
def update_table():
    db.create_all()
    return {'msg': '更新成功', 'statu_code': 'success'}


@app.route('/execution_method', methods=['GET', 'POST'])
def execution_method():
    def change_status(func):
        def wrapper(*args, **kwargs):
            _browser_list = None
            for arg in kwargs:
                if 'browser_list' in arg:
                    _browser_list = kwargs[arg]
            func_name_temp = kwargs['run_method']
            with open(f'txt_path/{func_name_temp.__name__}_browser_id.txt', 'w') as f:
                f.write('\n'.join(_browser_list))
            with open(f'txt_path/{func_name_temp.__name__}_complete_id.txt', 'w') as f:
                f.write('')
            if browser_list is not None:
                send_data = {
                    'run_browser_list': _browser_list,
                    'tag': 'wait'
                }
                requests.post(url=f'http://fbmessage.v7.idcfengye.com/changeTag', json=send_data)
            return func(*args, **kwargs)

        return wrapper

    model_list_face_run = ['get_group_info', 'get_group_userId', 'listen_group_comment']

    def long_running_task(_browser_list, _maxProcesses):
        # # 模拟一个耗时的函数
        import time
        for browser in _browser_list:
            dbu.update_browser_status(browser, random.randint(1, 2))
            time.sleep(random.randint(3, 5))

        logger.info("耗时函数执行完成")

    def open_browser(_browser_list):
        """打开选中浏览器"""
        for browser in _browser_list:
            open_b.open_browser(browser)
            time.sleep(random.randint(1, 3))

    def open_b_processes(_browser_list):
        threading.Thread(target=open_browser, args=(_browser_list,)).start()

    def listen_fb_comment(_browser_list, _maxProcesses, _current_function):
        """Fb监控小组评论"""
        listen_face.run(2, _current_function, _maxProcesses, 0)

    def tk_brushVideo(_browser_list=None, _maxProcesses=None, _current_function=None):
        """Tiktok养号"""
        run_tk.run(2, _current_function, _maxProcesses)
        print("Tiktok养号")

    def tk_uploadVideo(_browser_list=None, _maxProcesses=None, _current_function=None):
        """Tiktok上传视频"""
        my_utils.move_video_txt(_current_function)
        run_tk.run(1, _current_function, _maxProcesses)
        print("Tiktok上传视频")

    def tk_comment(_browser_list=None, _maxProcesses=None, _current_function=None):
        """Tiktok评论"""
        run_tk.run(3, _current_function, _maxProcesses)
        print("Tiktok评论")

    def get_tk_fans(_browser_list=None, _maxProcesses=None, _current_function=None):
        """采集Tiktok用户粉丝"""
        listen_tiktok.run(0, _current_function, _maxProcesses)

    def fb_brushPost(_browser_list=None, _maxProcesses=None, _current_function=None):
        """Facebook养号"""
        run_face.run2(1, _current_function, _maxProcesses)
        print("Facebook养号")

    def get_fb_newMember(_browser_list=None, _maxProcesses=None, _current_function=None):
        """Fb获取小组新人"""
        listen_face.run(1, _current_function, _maxProcesses)
        print("Fb获取小组新人")

    def get_fb_groupInfo(_browser_list=None, _maxProcesses=None, _current_function=None):
        """Fb获取小组信息"""
        listen_face.run(0, _current_function, _maxProcesses)
        print("Fb获取小组信息")

    def get_groupTel_all(_browser_list=None, _maxProcesses=None, _current_function=None):
        """获取ws群组电话"""
        run_ws.run(0, _current_function, _maxProcesses)

    def ins_get_user_fans(_browser_list=None, _maxProcesses=None, _current_function=None):
        """Ins获取用户粉丝"""
        run_ins.run(1, _current_function, _maxProcesses)

    @change_status
    def run_with_args(run_method, run_browser_list: list, max_processes: int, func_value: str = None):
        """
        此函数接受函数名、参数并将其在单独的线程中运行。
        """
        send_data = {
            'run_browser_list': run_browser_list,
            'tag': 'wait',
            'func_value': func_value,
        }
        requests.post(url=f'http://fbmessage.v7.idcfengye.com/changeTag', json=send_data)

        threading.Thread(target=run_method, args=(run_browser_list, max_processes, run_method.__name__)).start()

    functions = {
        "test1": long_running_task,
        "tk_brushVideo": tk_brushVideo,
        "tk_uploadVideo": tk_uploadVideo,
        "tk_comment": tk_comment,
        "fb_brushPost": fb_brushPost,
        "listen_fb_comment": listen_fb_comment,
        "get_fb_newMember": get_fb_newMember,
        "get_fb_groupInfo": get_fb_groupInfo,
        'get_tk_fans': get_tk_fans,
        'ws_get_groupTel': get_groupTel_all,
        'ins_get_user_fans': ins_get_user_fans,
    }
    data = request.get_json()['data']
    logger.info(data)
    if 'send_func_value' not in data or data['send_func_value'] == '':
        return {'msg': '请选择操作方法', 'statu_code': 'warning'}
    browser_list = data['sendBroList']
    if len(browser_list) == 1 and browser_list[0] == '':
        return {'msg': '请选择浏览器', 'statu_code': 'warning'}

    method = data['send_func_value']
    browser_list = data['sendBroList']
    max_maxProcesses = int(data['send_maxProcesses'])
    func_name = data['send_func_name']
    if method in functions:
        with app.app_context():
            run_with_args(run_method=functions[method], max_processes=max_maxProcesses,
                          run_browser_list=browser_list,
                          func_value=func_name)
    elif method == 'open_browser':
        with app.app_context():
            open_b_processes(browser_list)
    else:
        return {'msg': 'error', 'statu_code': 'error'}

    return {'msg': f'{func_name}任务已提交', 'statu_code': 'success'}


@app.route('/delete_tags', methods=['GET', 'POST'])
def delete_tags():
    request_id = request.args.get('id')
    print(request_id)
    return {'msg': '删除成功', 'status_code': 'success'}


@app.route('/delete_user', methods=['GET', 'POST'])
def delete_user():
    return requests.post(url=f'http://fbmessage.v7.idcfengye.com/changeTag', json=request.get_json()['data']).json()


@app.route('/add_FbAccount', methods=['GET', 'POST'])
def add_FbAccount():
    data = request.get_json()
    acc = dbu.FbAccount(**data)
    msg = acc.save()

    return {'msg': msg}


@app.route('/get_FbPwd', methods=['GET', 'POST'])
def get_FbPwd():
    data = request.get_json()
    pwd = dbu.select_fbAccountPwd(data['id'])
    if not pwd:
        return {'msg': False}
    return {'msg': pwd}


def get_dates():
    return sorted(set(record.access_date for record in AccessRecord.query.all()))


def get_ips():
    return sorted(set(record.ip_address for record in AccessRecord.query.all()))


if __name__ == '__main__':
    app.run(host='0.0.0.0:12144', port=12144, debug=False)
