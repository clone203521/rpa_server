import datetime
import os
import time

import pandas as pd
from flask import Flask, render_template, redirect, url_for, request
from flask_cors import CORS
from loguru import logger

from models import AccessRecord, db

app = Flask(__name__, template_folder='templates')
app.config.from_object('config.Config')
db.init_app(app)

CORS(app)  # 启用 CORS 支持

# 创建应用上下文
with app.app_context():
    # 在应用上下文中执行数据库操作
    db.create_all()


# @before_first_request
# def run_on_startup():
#     # 在这里运行您希望在 Flask 服务器启动时执行的代码


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


@app.route('/get_me', methods=['GET', 'POST'])
def get_me1():
    # 获取访问者的IP地址
    ip_address = request.remote_addr

    # 获取今天的日期
    today = datetime.date.today()

    # 更新数据库中的访问记录
    record = AccessRecord.query.filter_by(ip_address=ip_address, access_date=today).first()
    if record:
        record.count += 1
    else:
        new_record = AccessRecord(ip_address=ip_address, access_date=today, count=1)
        db.session.add(new_record)
    db.session.commit()
    total_access_count = AccessRecord.query.with_entities(db.func.sum(AccessRecord.count)).scalar() + 1931

    with open(f'user_id_txt/split_{total_access_count + 1}.txt', 'r', encoding='utf8') as f:
        data = [line.strip() for line in f.readlines()]
    total_access_count += 1
    data.append('http://192.168.31.16:12475/')
    logger.info(f'{data}')

    return {'list': data}


def get_dates():
    return sorted(set(record.access_date for record in AccessRecord.query.all()))


def get_ips():
    return sorted(set(record.ip_address for record in AccessRecord.query.all()))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9777, debug=True)
