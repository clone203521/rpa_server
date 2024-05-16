import math
import random
import threading
import time
from typing import Union

import pyotp
from DrissionPage._functions.keys import Keys
from DrissionPage._pages.chromium_page import ChromiumPage
from DrissionPage._pages.chromium_tab import ChromiumTab
from DrissionPage._units.actions import Actions
from loguru import logger

from utils.decorator import monitor_function

ROOT_PATH = 'browserDownload'


def click_button(page_click, locator):
    # 触发点击事件 失败后重试三次
    for index in range(3):
        try:
            page_click.ele(locator, timeout=5).ele('tag:i').click()
            break
        except:
            if index == 2:
                return False
            page_click.wait(2, 5)
            continue
    return True


# 刷短视频
def brushReel(page_brushReel: Union[ChromiumPage, ChromiumTab], brush_user_id):
    """刷短视频"""
    page_brushReel.wait(3, 5)
    start_reel_time = time.time()
    cycle_time = random.uniform(3, 5) * 60
    feel_like_count = 0
    feel_count = 0
    while True:
        page_brushReel.wait(3, 6)
        feel_count += 1
        # 点赞
        if 0.3 < random.random() < 0.4:
            like_loc = 'tag:div@aria-label=赞'
            if not click_button(page_brushReel, like_loc):
                logger.info(f'{brush_user_id}点赞失败，请检查错误原因')
            feel_like_count += 1
            logger.info(f'{brush_user_id}正在feel页面点赞，目前已点{feel_like_count}个赞')
        page_brushReel.wait(3, 4)

        running_time = time.time() - start_reel_time
        if running_time - cycle_time > 0:
            logger.info(f'{brush_user_id}短视频观看时间结束,正在结束流程，开始统计数据')
            logger.info(f'{brush_user_id}一共观看了{feel_count}个短视频，完成{feel_like_count}次点赞,'
                        f'耗时{math.floor(running_time / 60)}分{math.ceil(running_time / 60)}秒')
            return True, feel_count

        next_button = 'tag:div@aria-label=下一条快拍'
        if not click_button(page_brushReel, next_button):
            logger.info(f'{brush_user_id}目前一共刷了{feel_count}条短视频,完成{feel_like_count}次点赞')
            logger.info(f'{brush_user_id}进入下一个短视频失败，准备返回')
            return False, feel_count


# 当前小组链接
# https://www.facebook.com/groups/433276105788114/?ref=share_group_link
# 加入指定小组
def joinAGroup(page_joinAGroup: Union[ChromiumPage, ChromiumTab], joinGroup_user_id, group_url):
    """加入指定小组"""
    ac = Actions(page_joinAGroup)
    page_joinAGroup.get(group_url)
    page_joinAGroup.wait(2, 3)

    join_box = page_joinAGroup.ele('tag:div@aria-label=加入小组', timeout=10).ele('tag:span@dir=auto')
    if join_box:
        ac.move_to(join_box).click()
        logger.info(f'{joinGroup_user_id}正在加入指定小组')
    else:
        logger.error(f'{joinGroup_user_id}出现未知错误，加入小组按钮不存在')
    page_joinAGroup.wait(3, 5)

    # 返回主页
    back_box = page_joinAGroup.ele('tag:a@aria-label=Facebook', timeout=5)
    if back_box:
        ac.move_to(back_box).click()
        page_joinAGroup.wait(3, 5)
        logger.info(f'{joinGroup_user_id}正在返回主页')
    else:
        logger.error(f'{joinGroup_user_id}出现未知错误，主页按钮不存在，准备跳转主页')
        return False
    return True


def brushVideo(page_brushVideo: Union[ChromiumPage, ChromiumTab], video_user_id):
    """刷长视频
    :return: flag:运行是否成功，all_like_count:视频点赞次数
    """
    page_brushVideo.set.scroll.smooth()
    page_brushVideo.wait(10, 15)
    ac = Actions(page_brushVideo)
    all_like_count = 0

    # 当前视频页面类型
    if page_brushVideo.url.find('watch?v=') != -1:
        # 长视频页主页面 此页面有多个视频，类似主页，下滑刷新
        start_time_video = time.time()
        cycle_time = random.uniform(4, 7) * 60
        video_count = 0

        logger.info(f'{video_user_id}正在给主视频点赞')
        video_main_box = page_brushVideo.ele('tag:div@data-pagelet=WatchPermalinkVideo')
        like_box = video_main_box.next().ele('tag:div@aria-label=赞')
        if like_box:
            ac.move_to(like_box).click()
            logger.info(f'{video_user_id}主视频点赞成功')
        else:
            logger.error(f'{video_user_id}点赞失败，页面加载可能未完成')
            page_brushVideo.wait(10, 15)

        while True:
            video_count += 1
            page_brushVideo.wait(8, 13)
            main_Feed = page_brushVideo.ele('tag:div@data-pagelet=MainFeed', timeout=10)
            logger.info(f'{video_user_id}正在刷视频，当前是第{video_count}个视频')

            video_box = main_Feed.ele('._6x84', index=video_count)
            if not video_box:
                ac.scroll(0, 300)
                video_box = main_Feed.ele('._6x84', index=math.floor(video_count / 2))
                if not video_box:
                    running_time = time.time() - start_time_video
                    logger.info(f'{video_user_id}获取下一个视频元素失败，准备返回首页')
                    logger.info(f'{video_user_id}观看视频时间结束,正在结束流程，开始统计数据')
                    logger.info(f'{video_user_id}一共观看了{video_count}个视频，完成{all_like_count}次点赞,'
                                f'耗时{math.floor(running_time / 60)}分{math.ceil(running_time / 60)}秒')
                    return False, all_like_count
            page_brushVideo.scroll.to_see(video_box)

            if 0.5 < random.random() < 0.8:
                page_brushVideo.wait(2, 4)
                like_box = video_box.ele('tag:div@aria-label=赞')
                if like_box:
                    ac.move_to(like_box).click()
                    all_like_count += 1
                    ac.move(120, -100, duration=2)
                    logger.info(f'{video_user_id}正在点赞,已经完成{all_like_count}次点赞')
                    page_brushVideo.wait(2, 4)
                else:
                    logger.error(f'{video_user_id}点赞失败，请检查原因')
                    page_brushVideo.wait(4, 10)

            running_time = time.time() - start_time_video
            if running_time - cycle_time > 0:
                logger.info(f'{video_user_id}观看视频时间结束,正在结束流程，开始统计数据')
                logger.info(f'{video_user_id}一共观看了{video_count}个视频，完成{all_like_count}次点赞,'
                            f'耗时{math.floor(running_time / 60)}分{math.ceil(running_time / 60)}秒')
                return True, all_like_count

    elif page_brushVideo.url.find('www.facebook.com/reel/') != -1:
        # 短视频页面 类似tiktok的短视频页面，可以前往上一个或者下一个视频
        # 不刷短视频，直接返回上一页
        page_brushVideo.wait(3, 5)
        logger.info(f'{video_user_id}当前视频为短视频，直接返回主页')
    else:
        # 视频聚焦页面 此页面只有一个视频，不能前往下一个或者上一个视频
        if 0.1 < random.random() < 0.2:
            like_box = 'tag:div@aria-label=赞'
            if not click_button(page_brushVideo, like_box):
                logger.info(f'{video_user_id}点赞失败，请检查原因')
            all_like_count += 1
        # 退出视频页

    return all_like_count


@monitor_function
def brushPost(page_brushPost: Union[ChromiumPage, ChromiumTab], post_user_id, valid_event: threading.Event):
    """主页刷帖"""
    page_brushPost.set.scroll.smooth()
    ac = Actions(page_brushPost)
    # 定位到第一个帖子
    current_index = 1

    # 定义刷帖时间
    port_start_time = time.time()
    cycle_time = random.uniform(15, 20) * 60
    # cycle_time = 60 * 10
    all_like_count = 0
    return_flag = True
    try:
        while True:
            # 滚动到帖子可见
            current_post = page_brushPost.ele(f'tag:div@role=article', index=current_index)
            logger.info(f'{post_user_id}正在主页观看文章，当前观看了{current_index}篇文章')
            page_brushPost.scroll.to_see(current_post, center=True)
            ac.move_to(current_post)

            # 获取当前元素的静态版本，提升效率
            s_current_ele = current_post.s_ele()
            page_brushPost.wait(3, 5)

            like_box_flag = s_current_ele.ele('tag:div@aria-label=赞')

            # states.is_alive
            # 判断元素是否可用 True为可用

            # 点赞时间触发概率
            if 0.2 < random.random() < 0.22:
                if like_box_flag:
                    like_box = current_post.ele('tag:div@aria-label=赞')
                    ac.move_to(like_box).click()
                    page_brushPost.wait(2, 4)
                    all_like_count += 1
                    logger.info(f'{post_user_id}点赞成功，当前已点赞{all_like_count}次')
            # 确认当前帖子类型
            if s_current_ele.ele('tag:div@data-pagelet=Reels'):
                # 短视频
                pass
            elif s_current_ele.ele('tag:a@aria-label=Reels'):
                # 短视频或Reels
                pass
            elif s_current_ele.ele('tag:video'):
                # 视频
                if 0.1 < random.random() < 0.3:
                    ac.move_to(current_post, duration=3.5).click()
                    try:
                        flag, temp_count = brushVideo(page_brushPost, post_user_id)
                        all_like_count += temp_count
                    except:
                        logger.info(f'{post_user_id}视频页发生错误，正在回到上一页')
                        ac.key_down(Keys.ESCAPE)
                        page_brushPost.wait(3, 5)
                        return_flag = False
                        break
                    logger.info(f'{post_user_id}视频观看完成，正在返回主页')
                    ac.key_down(Keys.ESCAPE)
                    page_brushPost.wait(3, 5)
                    break
            elif s_current_ele.ele('tag:div@aria-label=为你推荐'):
                # 推荐小组
                if 0.1 < random.random() < 0.2:
                    group_length = len(current_post.eles('tag:li'))
                    for _temp in range(1, group_length - 1):
                        page_brushPost.wait(2, 3)
                        if 0.2 < random.random() < 0.3:
                            if _temp == 1:
                                next_box = current_post.ele('tag:div@aria-label=向右箭头').ele('tag:i')
                                ac.move_to(next_box).click()
                            else:
                                ac.click()
                            logger.info(f'{post_user_id}正在进行小组翻页')
                            page_brushPost.wait(2, 3)
                        elif 0.2 < random.random() < 0.22:
                            logger.info(f'{post_user_id}准备加入小组')
                            public_flag = current_post.ele('tag:li', index=_temp).ele('公开小组')
                            if not public_flag:
                                logger.info(f'{post_user_id}该小组不是公开小组，进入下一次循环')
                                continue
                            add_group_box = current_post.ele('tag:div@aria-label=加入小组', index=_temp)
                            if add_group_box:
                                ac.move_to(add_group_box).click()
                                logger.info(f'{post_user_id}正在点击加入小组按钮')
                                page_brushPost.wait(5, 8)
                                break
                            else:
                                logger.error(f'{post_user_id}已经加入该小组，无法重复加入')
                            break
                        # 概率不加小组直接退出
                        elif 0.3 < random.random() < 0.8:
                            logger.info(f'{post_user_id}选择不加入小组，继续下一步操作')
                            break

            running_time = time.time() - port_start_time
            if running_time > cycle_time:
                logger.info(f'{post_user_id}时间结束,正在结束流程，开始统计数据')
                logger.info(f'{post_user_id}一共观看了{current_index}个文章，完成{all_like_count}次点赞,'
                            f'耗时{math.floor(running_time / 60)}分{math.ceil(running_time % 60)}秒')
                break
            current_index += 1
    except Exception as e:
        logger.error(e)

    time.sleep(random.randint(30, 40))
    valid_event.set()
    return return_flag


def face_init(page_init: Union[ChromiumPage, ChromiumTab], email_init, pwd_init, fa_two_init, user_id_init):
    """Facebook登陆账号"""

    def get_faTwo_code(fa_2):
        """返回2FA验证码
        :param fa_2: 2FA序列号
        :return: 6位验证码
        """
        # 创建一个TOTP对象
        totp = pyotp.TOTP(fa_2)
        # 生成当前时间的验证码
        return totp.now()

    logger.info(f'{user_id_init}开始登陆')
    page_init.wait(20, 30)
    # page_init.scroll.to_bottom()
    # flag = page_init.ele('tag:button@@text()=Allow all cookies')
    # if flag:
    #     flag.click()
    if page_init.url.find('https://mbasic.facebook.com/login.php') == -1:
        page_init.get('https://mbasic.facebook.com/login.php')
    # 输入邮箱和密码
    page_init.ele('#m_login_email').input(email_init)
    page_init.ele('tag:input@name=pass').input(pwd_init)
    logger.info(f'{user_id_init}正在输入邮箱和密码')
    # 点击登录
    page_init.ele('tag:input@name=login').click()
    fa_2_code = get_faTwo_code(fa_two_init)
    fa2_code_box = page_init.wait.ele_loaded('#approvals_code', timeout=10)
    if fa2_code_box:
        fa2_code_box.input(fa_2_code)
        logger.info(f'{user_id_init}正在输入2fa验证码')
    else:
        logger.error(f'{user_id_init}2fa验证码获取失败')
        return False
    # 提交验证码
    page_init.ele('#checkpointSubmitButton-actual-button', timeout=5).click()
    # 继续
    page_init.ele('#checkpointSubmitButton-actual-button', timeout=5).click()
    # 前往首页
    while True:
        page_init.wait(5, 10)
        try:
            jinxu = page_init.wait.ele_loaded('tag:a@@text()=继续', timeout=10)
            if jinxu:
                jinxu.click()
            else:
                break
        except:
            continue
    page_init.wait.doc_loaded(timeout=10)
    page_init.wait(5, 7)
    ac_init = Actions(page_init)
    ac_init.move_to((300, 20)).click()

    # 进入新版facebook主页
    page_init.get('https:www.facebook.com')
    page_init.wait(3, 5)
    ac_init = Actions(page_init)

    # 确认记住密码
    confirmSavePassword = page_init.ele('css:[role="button"]>[role="none"]>[role="none"]', index=1, timeout=10)
    ac_init.move_to(confirmSavePassword).click()

    return True


def send_message(page_send: Union[ChromiumPage, ChromiumTab], user_id_send):
    """发送私信"""
    logger.info(f'{user_id_send}进入私信页面')
    send_test = '61556571823159'
    ac = Actions(page_send)
    send_txt = 1
    send_url = f'https://www.facebook.com/messages/t/{send_test}'

    page_send.get(send_url)

    send_box = page_send.ele('tag:div@aria-label=发消息')
    ac.move_to(send_box).click().type(Keys.CTRL_V)

    send_box.input('这是一条测试消息')
    logger.info(f'{user_id_send}正在发送消息')


# 随机加推荐好友
def Random_add_friends(page_addFri: Union[ChromiumPage, ChromiumTab], user_id_addFri):
    """添加2-3个推荐好友"""
    logger.info(f'{user_id_addFri}准备开始添加好友')
    ac = Actions(page_addFri)

    suggest_fri_url = 'https://www.facebook.com/friends/suggestions'
    page_addFri.get(suggest_fri_url)

    fri_list = page_addFri.eles('tag:div@aria-label=加为好友')
    rand_fri_id = random.sample(range(1, len(fri_list) + 1), 3)

    for fri_box_id in rand_fri_id:
        ac.move_to(fri_list[fri_box_id]).click()
        page_addFri.wait(3, 5)


# 随机添加推荐小组
def addGroupsRandomly(page_addGroup: Union[ChromiumPage, ChromiumTab], user_id_addGroup):
    """添加2-3个推荐小组"""
    sug_group_url = ''
    page_addGroup.get(sug_group_url)
    pass


# 添加指定好友
def addSpecifieFri(page_addGroup: Union[ChromiumPage, ChromiumTab], user_id_addGroup):
    """添加指定好友"""
    origin_url = 'https://www.facebook.com/profile.php?id='
    fri_id = '61556571823159'
    ac = Actions(page_addGroup)

    fri_url = origin_url + fri_id
    page_addGroup.get(fri_url)
    page_addGroup.wait(3, 5)

    fri_box = page_addGroup.ele('tag:div@aria-label=添加好友')
    if not fri_box:
        logger.error(f'{user_id_addGroup}获取添加好友按钮失败，准备返回主页')
        return False
    ac.move_to(fri_box).click()
    logger.info(f'{user_id_addGroup}正在添加好友，id:{fri_id}')

    bace_box = page_addGroup.ele('tag:a@aria-label=Facebook')
    if not bace_box:
        logger.error(f'{user_id_addGroup}获取返回主页按钮失败，即将跳转主页链接')
        return False
    ac.move_to(bace_box).click()
    logger.info(f'{user_id_addGroup}添加好友成功，正在回到主页')
    return True


def addFriendsInAGroup(page_add_FriInGp: Union[ChromiumPage, ChromiumTab], user_id_add_FriInGp):
    """在小组中添加好友"""
    ac = Actions(page_add_FriInGp)
    main_box = page_add_FriInGp.ele('tag:div@role=feed')
    current_child = main_box.child('tag:div').next('tag:div')

    add_upperLimit = random.randint(2, 3)
    add_count = 0
    while True:
        page_add_FriInGp.scroll.to_see(current_child, center=True)
        if 0.2 < random.random() < 0.4:
            name_box = current_child.ele('tag:h3').ele('tag:a')
            ac.move_to(name_box)

            page_add_FriInGp.wait.ele_loaded('tag:div@aria-label=链接预览', timeout=10)
            add_user = page_add_FriInGp.ele('tag:div@aria-label=添加好友')
            ac.move_to(add_user).click()
            add_count += 1
            logger.info(f'{user_id_add_FriInGp}正在小组内添加好友，目前添加个数为{add_count}')
            page_add_FriInGp.wait(2, 3)
        if add_count == add_upperLimit:
            logger.info(f'{user_id_add_FriInGp}好友添加达到本次上限，小组内加好友执行结束')
            break
            pass
    return True


def collecting_groupId(page_collect: Union[ChromiumPage, ChromiumTab], searchGroup_user_id, group_key,
                       stop_event: threading.Event):
    page_collect.get('https://www.facebook.com/groups/feed/')
    page_collect.wait(10, 15)
    group_input_box = page_collect.ele('tag:input@aria-autocomplete=list', index=2, timeout=10)
    if not group_input_box:
        page_collect.wait(15, 20)
        logger.debug(f'{searchGroup_user_id}没有找到输入框，请检查原因')
        return False
    group_input_box.input((f'{group_key}', Keys.ENTER))
    logger.info(f'{searchGroup_user_id}正在搜索小组')
    page_collect.wait(10, 15)
    logger.info(f'{searchGroup_user_id}开始滚动屏幕')

    count = 1
    while not stop_event.is_set():
        page_collect.scroll.down(800)
        page_collect.wait(2, 4)
        count += 1
        logger.info(f'{searchGroup_user_id}滚动第{count}次')

    pass


def collecting_group_userId(page_getUserId: Union[ChromiumPage, ChromiumTab], coll_groupUser_user_id,
                            group_url, stop_event: threading.Event, valid_event: threading.Event):
    page_getUserId.get(f'{group_url}members')
    page_getUserId.wait(10, 15)
    logger.info(f'{coll_groupUser_user_id}开始滚动屏幕')
    count = 1

    while not stop_event.is_set():
        page_getUserId.scroll.down(300)
        page_getUserId.wait(3)
        logger.info(f'{coll_groupUser_user_id}滚动第{count}次')
        count += 1
        # if run_count == 180:
        #     stop_event.set()
        #     break
    # if stop_event.is_set():
    #     logger.warning(f'{coll_groupUser_user_id}提前结束')
    #     time.sleep(60)
    stop_event.set()
    logger.info(f'{coll_groupUser_user_id}获取小组成员id完成')
    pass


def scroll_group_comment(page_comment: Union[ChromiumPage, ChromiumTab], comment_user_id, group_url,
                         stop_event: threading.Event, valid_event: threading.Event):
    if 'login' in page_comment.url:
        page_comment.wait(30, 45)
    else:
        page_comment.get(group_url)
        page_comment.wait(10, 15)
    current_tab = page_comment.get_tab(url='groups/')
    if not current_tab:
        logger.error(f'{comment_user_id}获取小组tab失败，准备返回主页')
        stop_event.set()
        return False
    logger.info(f'{comment_user_id}开始滚动屏幕')

    temp_time = time.time()
    while not stop_event.is_set():
        current_tab.scroll.down(600)
        current_tab.wait(1, 3)
        if time.time() - temp_time > 60 * 6:
            temp_time = time.time()
            current_tab.refresh()
            current_tab.wait(20)


# check

def fa2_test():
    def get_faTwo_code(fa_2):
        """返回2FA验证码
        :param fa_2: 2FA序列号
        :return: 6位验证码
        """
        # 创建一个TOTP对象
        totp = pyotp.TOTP(fa_2)
        # 生成当前时间的验证码
        return totp.now()

    while True:
        fa2_code = input("请输入2FA验证码: ")
        fa_2 = get_faTwo_code(fa2_code.replace(' ', ''))
        print(fa_2)


def xxxx():
    x = 1 + 1
    logger.info('飒飒飞机卡号法律框架撒娇了')


if __name__ == '__main__':
    xxxx()

    fa2_test()
