from datetime import datetime

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class AccessRecord(db.Model):
    __tablename__ = 'access_record'
    id = db.Column(db.Integer, primary_key=True)
    ip_address = db.Column(db.String(100), nullable=False)
    access_date = db.Column(db.Date, nullable=False)
    count = db.Column(db.Integer, default=1)

    def __repr__(self):
        return (f"<AccessRecord(id={self.id}, ip_address={self.ip_address}, "
                f"access_date={self.access_date}, count={self.count})>")


class AdsBrowser(db.Model):
    __tablename__ = 'browser'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, comment='浏览器id_数据库')
    index = db.Column(db.Integer, nullable=False, comment='浏览器编号')
    browser_name = db.Column(db.String(10), nullable=False, comment='唯一标识')
    group = db.Column(db.String(50), comment='分组')
    remarks = db.Column(db.Text, comment='备注')
    tags = db.Column(db.Text, comment='标签')  # 已删除
    status = db.Column(db.String(20), default='idle', comment='状态')
    last_update = db.Column(db.String(50), comment='上一次使用时间')
    ip_address = db.Column(db.String(100), comment='IP地址')
    current_operation = db.Column(db.String(50), default='暂无操作', comment='当前操作')


class BrowserTag(db.Model):
    __tablename__ = 'tag'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, comment='标签id_数据库')
    tag_name = db.Column(db.String(50), nullable=False, comment='标签名称')
    create_time = db.Column(db.DateTime, nullable=False, default=datetime.now)
    type_name = db.Column(db.String(50), default='primary', nullable=False, comment='标签类型')
    is_delete = db.Column(db.Integer, default=0, nullable=False, comment='状态 1删除，0正常')

    # 关系已被定义在 AdsBrowser 类中，此处无需重复定义
    # browsers = relationship("AdsBrowser", backref="tags")  # 无效，且重复定义


class Operation(db.Model):
    __tablename__ = 'operation'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, comment='操作id')
    operate_name = db.Column(db.String(50), nullable=False, comment='操作名称')
    create_time = db.Column(db.DateTime, nullable=False, default=datetime.now)
    function_name = db.Column(db.String(50), unique=True, nullable=False, comment='方法名称')
    type = db.Column(db.String(50), nullable=False, default="其他操作", comment='操作类型')
    is_delete = db.Column(db.Integer, default=0, nullable=False, comment='是否弃用 1删除，0正常')


if __name__ == '__main__':
    data = [
        {'label': '打开选中浏览器', 'value': 'open_browser', 'type': '其他操作'},
        {'label': 'Tiktok养号', 'value': 'tk_brushVideo', 'type': 'Tiktok'},
        {'label': 'Tiktok上传视频', 'value': 'tk_uploadVideo', 'type': 'Tiktok'},
        {'label': 'Tiktok评论', 'value': 'tk_comment', 'type': 'Tiktok'},
        {'label': 'Facebook养号', 'value': 'fb_brushPost', 'type': 'Facebook'},
        {'label': 'Fb监控小组评论', 'value': 'listen_fb_comment', 'type': 'Facebook'},
        {'label': 'Fb获取小组新人', 'value': 'get_fb_newMember', 'type': 'Facebook'},
        {'label': 'Fb获取小组信息', 'value': 'get_fb_groupInfo', 'type': 'Facebook'}
    ]

    # 使用列表推导式转换数据格式
    result = [
        {
            'label': key,
            'options': [{'value': item['value'], 'label': item['label']} for item in data if item['type'] == key]
        }
        for key in set(item['type'] for item in data)
    ]

    print(result)
