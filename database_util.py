from datetime import datetime

from models import db, AdsBrowser, BrowserTag, Operation, FbAccount

dbs = db.session


def to_dict(model_list: list):
    temp_list = []
    for model in model_list:
        temp = model.__dict__
        del temp['_sa_instance_state']
        temp_list.append(temp)
    return temp_list


def add_browser(acc_id, name, group, tags, ip, country):
    browser = AdsBrowser(index=acc_id, browser_name=name, group=group, tags=tags, ip_address=f'{ip}--{country}'
                         , last_update=f'{datetime.now():%Y-%m-%d %H:%M:%S}')
    dbs.add(browser)
    dbs.commit()


def select_browserList(pageNum: int, pageSize: int, tags_list: set, sendNoTagList: set):
    # 构建查询条件
    query = dbs.query(AdsBrowser)
    skip = (pageNum - 1) * pageSize
    if len(sendNoTagList) == 0 and len(tags_list) == 0:
        browser_list = query.all()
    else:
        if len(tags_list) != 0:
            # 为每个标签创建 OR 条件
            conditions = [AdsBrowser.tags.contains(tag) for tag in tags_list]
            query = query.filter(db.or_(*conditions))  # 使用 OR 组合条件
            browser_list = [
                browser for browser in query
                if set(browser.tags.split(',')).intersection(tags_list) and not
                set(browser.tags.split(',')).intersection(sendNoTagList)
            ]
        else:
            browser_list = [
                browser for browser in query
                if not set(browser.tags.split(',')).intersection(sendNoTagList)
            ]

    # 分页
    total = len(browser_list)
    data = browser_list[skip: pageNum * pageSize]

    # 返回结果
    return to_dict(data), total


def select_browserList12(pageNum: int, pageSize: int, sendTagList: list):
    # 计算偏移量
    skip = (pageNum - 1) * pageSize
    # 查询数据
    browsers = dbs.query(AdsBrowser).offset(skip).limit(pageSize).all()
    # 计算总数
    total = dbs.query(AdsBrowser).count()

    return to_dict(browsers), total


def select_tagsList():
    tags = dbs.query(BrowserTag).filter(BrowserTag.is_delete == 0).all()
    return tags


def select_operateList():
    operates = dbs.query(Operation).filter(Operation.is_delete == 0).all()
    return operates


def update_browser_status(browser_name: str, status: int):
    dbs.query(AdsBrowser).filter(AdsBrowser.browser_name == browser_name).update(
        {'last_update': f'{datetime.now():%Y-%m-%d %H:%M:%S}', 'status': status})
    dbs.commit()


def edit_browser_tag(browser_name: str, tag: str):
    browser = dbs.query(AdsBrowser).filter(AdsBrowser.browser_name == browser_name).first()
    if browser is not None:
        browser.tags = tag
        dbs.commit()
    return True


def add_fbAccount(acc_id: str, acc_email: str, acc_password: str, acc_fa2: str):
    temp_acc = FbAccount(fb_id=acc_id, email=acc_email, fa_2=acc_fa2, password=acc_password)
    dbs.add(temp_acc)
    dbs.commit()
    return True


def select_fbAccountPwd(acc_id: str):
    acc = dbs.query(FbAccount).filter(FbAccount.fb_id == acc_id).first()
    if acc is not None:
        return acc.password
    return False


if __name__ == '__main__':
    a = {'之前能发评论', 'facebook'}
    b = {'facebook'}
    c = {'12'}

    print(a.intersection(b))
    print(a.intersection(c))
