import math
import random
import re
import threading
import time
from typing import Union

from DrissionPage._functions.keys import Keys
from DrissionPage._pages.chromium_page import ChromiumPage
from DrissionPage._pages.chromium_tab import ChromiumTab
from DrissionPage._units.actions import Actions
from loguru import logger

from utils import my_utils

ROOT_PATH = 'browserDownload'


def upload_video(page_upload: Union[ChromiumPage, ChromiumTab], user_id):
    # page.set.window.full()
    # luxury bag #gucci #chanel #fyp #foryoupage  #tiktok
    # 点击上传按钮
    page_upload.get('https://www.tiktok.com/creator-center/upload?from=upload')
    page_upload.wait(4, 6)
    logger.info(f'{user_id}进入上传界面')

    # 上传文件

    video_path = f'./{ROOT_PATH}/{user_id}/video_1.mp4'
    file_upload_box = None
    for _ in range(3):
        try:
            file_upload_iframe = page_upload.wait.ele_loaded('tag:iframe', timeout=60, raise_err=True)
            file_upload_box = file_upload_iframe.eles('tag:button', timeout=10)[0]
            # logger.error(f'{user_id} iframe界面加载失败，正在重试')
        except:
            logger.error(f'{user_id} iframe界面加载失败，正在重试')
            page_upload.refresh()
            page_upload.wait(5, 7)
            continue
    if not file_upload_box:
        logger.error(f'{user_id}上传视频时出现问题,请检查网络')
        return False
    file_upload_box.wait(1, 3.2)
    file_upload_box.click.to_upload(video_path)

    logger.info(f'{user_id}文件上传中，请等待')
    file_upload_box.wait(1, 3.2)
    cancel = page_upload.wait.ele_loaded('tag:div@@text()=Cancel', timeout=20)
    delete_flag = page_upload.wait.ele_deleted(cancel, timeout=500)
    if delete_flag:
        logger.info(f'{user_id}文件上传完成')
    else:
        logger.error(f'{user_id}文件上传失败，请重试')
        return False

    # 输入视频标题
    title = page_upload.ele('tag:div@data-contents=true')
    # title.input(clear=True, vals='')

    logger.info(f'{user_id}正在输入视频标题')
    tag_set = {'gucci', 'chanel', 'fyp', 'foryoupage', 'tiktok', 'louis', 'vuitton', 'prada', 'bag', 'shoes'}
    tag_length = len(tag_set)

    temp_click = page_upload.ele('tag:span@@text()=Post a video to your account')
    # 创建ActionChains实例
    ac = Actions(page_upload)
    for_count = 0
    title.input('luxury bag ', clear=True)

    for _ in range(tag_length):
        tag = random.choice(list(tag_set))
        tag_set.remove(tag)
        title.input('#', clear=False)
        for char_i in tag[:-1]:
            title.input(char_i, clear=False)

        ac.move_to(temp_click).click()
        title.input(tag[-1], clear=False)

        while_count = 1
        for next_i in range(3):
            enter_flag = page_upload.wait.ele_loaded('tag:div@class=mentionSuggestions', timeout=2)
            if enter_flag:
                enter_box = enter_flag.child('tag:div').child('tag:div')
                try:
                    enter_box.click()
                    for_count += 1
                except:
                    while_count += 1
                    continue
                break
            else:
                ac.type((Keys.CTRL, 'z'))
                if next_i == 2:
                    ac.type((Keys.CTRL, 'z'))
                else:
                    title.input(tag[-1], clear=False)

        if for_count == 5:
            break

    page_upload.scroll.to_bottom()
    logger.info(f'{user_id}标题输入完成')
    page_upload.wait(15)

    # 点击上传按钮
    time.sleep(3)
    page_upload.ele('tag:div@class:btn-post').ele('tag:button').click()
    while True:
        manage = page_upload.wait.ele_loaded('tag:div@@text()=Manage your posts', timeout=3)
        if manage:
            break
        page_upload.ele('tag:div@class:btn-post').ele('tag:button').click()
    manage.click()
    logger.info(f'{user_id}视频发布完成')

    logger.info(f'{user_id}正在回到首页')
    page_upload.scroll.to_bottom()
    page_upload.wait(1)
    page_upload.ele('tag:span@@text()=Back to TikTok').click()

    page_upload.wait.doc_loaded(timeout=8)
    return True


def modify_personal_data(page_modify: Union[ChromiumPage, ChromiumTab], user_id_modify):
    # 点击进入个人主页
    try:
        page_modify.ele('tag:span@@text()=Profile').click()
    except:
        logger.info(f'{user_id_modify},账号登陆失败')
        page_modify.quit()

    # 滑块验证
    if not my_utils.validation(page_modify, user_id_modify):
        logger.error(f'{user_id_modify}滑块验证失败，请检查原因')

    # 点击刷新按钮
    refresh = page_modify.ele('tag:button@@text()=Refresh')
    if refresh:
        page_modify.refresh()

    logger.info(f'{user_id_modify}正在修改个人资料')
    # 修改个人资料
    for _ in range(3):
        try:
            page_modify.ele('tag:span@@text()=Edit profile', timeout=10).click()
            break
        except:
            page_modify.wait(2, 3)
            continue
    time.sleep(1)
    # 上传头像

    logger.info(f'{user_id_modify}正在上传头像')
    page_modify.ele('tag:div@aria-label=Profile photo').ele('tag:svg').click.to_upload('./publicPicture/avatar.jpg')
    apply = page_modify.wait.ele_loaded('tag:button@@text()=Apply', timeout=5)
    apply('tag:button@@text()=Apply').click()
    time.sleep(1)

    # 填写个人简介
    logger.info(f'{user_id_modify}正在修改个人简介')
    bio = page_modify.ele('@placeholder=Bio')
    bio.input('Step into Luxury with 1:1 Quality Gucci, LV, & Chanel!💼✨', clear=True)
    time.sleep(1)

    page_modify.ele('text=Save').click()

    time.sleep(7)

    if not my_utils.validation(page_modify, user_id_modify):
        logger.info(f'{user_id_modify}滑块验证失败，请检查原因')
    page_modify.refresh()
    page_modify.wait.ele_loaded('tag:span@@text()=Edit profile', timeout=10)

    page_modify.ele('tag:span@@text()=For You').click()
    logger.info(f'{user_id_modify}正在回到首页')
    page_modify.wait(1, 3.5)
    return True


def brushVideo(page_brush: Union[ChromiumPage, ChromiumTab], brush_user_id):
    def exploreOrRefulsh(page_brush_explore, or_user_id):
        explore_ac = Actions(page_brush_explore)
        temp_func_start_time = time.time()
        # 返回首页
        while True:
            try:
                page_brush_explore.ele('tag:button@aria-label=Close').ele('tag:svg').click()
                break
            except:
                current_endTime = time.time()
                if current_endTime - temp_func_start_time > 60 * 1.5:
                    page_brush_explore.get('https://www.tiktok.com')
                    break
                page_brush.wait(1, 2.1)
                continue
        if random.random() >= 0.5:
            # 前往explore界面刷视频
            explore_button = page_brush_explore.ele('tag:a@data-e2e=nav-explore', timeout=10).ele('tag:svg')
            explore_button.click()
            type_list = page_brush_explore.ele('tag:div@class:DivCategoryListWrapper', timeout=5).eles('tag:span')
            rand_type = random.randint(0, len(type_list) - 1)

            type_list[rand_type].click()
            # 随机点进一个视频
            video_list = (page_brush_explore.ele('tag:div@data-e2e=explore-item-list', timeout=10)
                          .eles('tag:div@data-e2e=explore-item', timeout=10))

            # 移动到视频并点击进入界面
            rand_video = random.randint(0, 7)
            explore_ac.scroll(on_ele=video_list[rand_video])
            explore_ac.move_to(ele_or_loc=video_list[rand_video])
            page_brush_explore.wait(3, 5)
            explore_ac.click()
        else:
            logger.info(f'{or_user_id}首页刷新，继续从首页刷视频')
            page_brush_explore.ele('tag:a@data-e2e=nav-foryou', timeout=5).ele('tag:svg').click()
            # 刷新首页视频
            page_brush_explore.refresh()
            page_brush.wait.ele_loaded('tag:span@data-e2e=comment-icon', timeout=10).click()
            page_brush.wait(3, 5)
        logger.info(f'{or_user_id}继续开始视频')

    # 进入视频界面
    logger.info(f'{brush_user_id}开始刷视频')
    start_flag = page_brush.ele('tag:span@data-e2e=comment-icon', index=1, timeout=10)
    if start_flag:
        start_flag.click()
    else:
        logger.error(f'{brush_user_id}网络出现波动，请稍后重试')
        return False

    func_start_time = time.time()
    # 每个帐号刷视频的时间
    cycle_time = random.uniform(60, 70) * 60
    # cycle_time = 600

    like_count = 1
    video_count = 1
    local_flag = False
    next_box_location = (0, 7)
    ac = Actions(page_brush)
    once_video = random.randint(5, 9)

    # 刷视频，循环退出条件为达到规定时间
    while True:
        page_brush.wait(2, 4)
        # 滑动验证
        if not my_utils.validation(page_brush, brush_user_id):
            logger.error(f'{brush_user_id}滑块验证失败，请检查原因')
            return False

        # 随机点赞 概率0.1
        if 0.4 < random.random() < 0.5:
            like_box = page_brush.ele('tag:span@data-e2e=browse-like-icon', timeout=10).ele('tag:svg')
            like_box.click()
            logger.info(f'{brush_user_id}正在点赞,已完成{like_count}个点赞')
            like_count += 1

        # 每个视频看10-15秒
        page_brush.wait(5, 8)
        current_endTime = time.time()
        new_list = ['jfuv0oh', 'jfuv0oj', 'jfuv0ok', 'jfuv0om', 'jfuv0oo', 'jfuv0op', 'jfuv0oq', 'jfuv0or', 'jfuv0os',
                    'jfuv0ot']
        # 随机@人
        if 0.1 < random.random() < 0.13 and random.random() > 10:
            if brush_user_id not in new_list:
                try:
                    commentAreaAt_low(page_brush, brush_user_id, random.randint(1, 50))
                except Exception as e:
                    logger.error(e)

        running_time = current_endTime - func_start_time
        if running_time > cycle_time:
            logger.info(f'{brush_user_id}时间结束,正在结束流程，开始统计数据')
            logger.info(f'{brush_user_id}一共观看了{video_count}个视频，完成{like_count}次点赞,'
                        f'耗时{math.floor(running_time / 60)}分{math.ceil(running_time % 60)}秒')
            break
        # 点击进入下一个视频
        logger.info(f'{brush_user_id}准备进入下一个视频，目前已经观看了{video_count}个视频')
        video_count += 1
        once_video -= 1

        if not local_flag:
            click_box = page_brush.ele('tag:button@data-e2e=arrow-right').ele('tag:path')
            click_location = click_box.rect.click_point
            next_box_location = (int(click_location[0]), int(click_location[1]))

            logger.info(click_location)
            logger.info(next_box_location)

            local_flag = True
        if once_video == 0:
            logger.info(f'{brush_user_id}当前页视频观看完成，进入explore也观看或刷新主页视频')
            exploreOrRefulsh(page_brush, brush_user_id)
            once_video = random.randint(5, 9)
            local_flag = False

        ac.move_to(next_box_location).click()

    # 回到首页
    page_brush.get('https://www.tiktok.com')
    logger.info(f'{brush_user_id}已经回到首页')
    return True


def commentAreaAt_low(page_comment: Union[ChromiumPage, ChromiumTab], comment_user_id, file_index):
    def get_string_between_tags(s):
        pattern = r'>(.*?)<'
        result = re.search(pattern, s)
        if result:
            return result.group(1)
        else:
            return '//////.......'

    videoUrl_list = ["https://www.tiktok.com/@wuhankgaudw/video/7352361561832377642",
                     "https://www.tiktok.com/@wuhankgaudw/video/7352141368271047978",
                     "https://www.tiktok.com/@wuhankgaudw/video/7327506954903948575",
                     "https://www.tiktok.com/@wuhankgaudw/video/7324876053237796127",
                     "https://www.tiktok.com/@wuhankgtaudw/video/7323011907542158622",
                     "https://www.tiktok.com/@wuhankgaudw/video/7322718720193776927",
                     "https://www.tiktok.com/@wuhankgaudw/video/7322635449321753887",
                     "https://www.tiktok.com/@wuhankgaudw/video/7320143431563611422",
                     "https://www.tiktok.com/@wuhankgaudw/video/7320055183377976618",
                     "https://www.tiktok.com/@wuhankgaudw/video/7320054669710052654",
                     "https://www.tiktok.com/@wuhankgaudw/video/7320053666763951406",
                     "https://www.tiktok.com/@wuhankgaudw/video/7320052976784215342",
                     "https://www.tiktok.com/@wuhankgaudw/video/7320052248829119786",
                     "https://www.tiktok.com/@wuhankgaudw/video/7319769114392743199",
                     "https://www.tiktok.com/@wuhankgaudw/video/7319683281941810462",
                     "https://www.tiktok.com/@wuhankgaudw/video/7319384733329198366",
                     "https://www.tiktok.com/@wuhankgaudw/video/7316784758216805663",
                     "https://www.tiktok.com/@wuhankgaudw/video/7316704487048006943",
                     "https://www.tiktok.com/@wuhankgaudw/video/7316418916568403230",
                     "https://www.tiktok.com/@wuhankgaudw/video/7316361612728814879",
                     "https://www.tiktok.com/@wuhankgaudw/video/7315673436993375519",
                     "https://www.tiktok.com/@wuhankgaudw/video/7315609906072046878",
                     "https://www.tiktok.com/@wuhankgaudw/video/7315227351170796830",
                     "https://www.tiktok.com/@wuhankgaudw/video/7314948490969304350",
                     "https://www.tiktok.com/@wuhankgaudw/video/7314491195365887262",
                     "https://www.tiktok.com/@wuhankgaudw/video/7314109903113587998",
                     "https://www.tiktok.com/@wuhankgaudw/video/7313829725103770910",
                     "https://www.tiktok.com/@wuhankgaudw/video/7313739269741317407",
                     "https://www.tiktok.com/@wuhankgaudw/video/7313105634357038367",
                     "https://www.tiktok.com/@wuhankgaudw/video/7313075519967284511",
                     "https://www.tiktok.com/@wuhankgaudw/video/7312998306626538783",
                     "https://www.tiktok.com/@wuhankgaudw/video/7312740410651184415",
                     "https://www.tiktok.com/@wuhankgaudw/video/7312727649032473887",
                     "https://www.tiktok.com/@wuhankgaudw/video/7312701521504800031",
                     "https://www.tiktok.com/@wuhankgaudw/video/7312372622275153183"]

    page_comment.get(random.choice(videoUrl_list))
    # page_comment.get('https://www.tiktok.com/@wuhankgaudw/video/7355304666814614827')

    # 滑块验证
    if not my_utils.validation(page_comment, comment_user_id):
        logger.error(f'{comment_user_id}滑块验证失败，请检查原因')
        return False

    title = page_comment.ele('tag:div@class=DraftEditor-root')

    file_path = f'./split/split_{random.randint(1, 150)}.txt'
    try:
        with open(file_path, 'r', encoding='utf8') as comment_f:
            temp_lines = [line.strip() for line in comment_f.readlines()]
    except:
        logger.error(f'{comment_user_id},用户id文件已用完，请添加新文件后再运行')
        return False
    # 从原始列表中抽取九个用户名
    lines = random.sample(temp_lines, 35)

    at_box = page_comment.ele('tag:div@data-e2e=comment-at-icon', timeout=10).ele('tag:svg')
    if at_box:
        page_comment.scroll.to_see(at_box)
    else:
        logger.error(f'{comment_user_id}可能出现网络问题，请检查错误原因')
        return False

    logger.info(f'{comment_user_id}开始输入评论')

    ac = Actions(page_comment)

    page_comment.wait(2, 3)
    temp_click_box_Coordinates = page_comment.ele('tag:div@class:DivCommentContainer').rect.screen_location
    if not temp_click_box_Coordinates:
        full_box = page_comment.ele('#ZoomIn_path-1-inside-1')
        if full_box:
            ac.move_to(full_box).click()
            page_comment.wait(2, 3)
        temp_click_box_Coordinates = page_comment.ele('tag:div@class:DivCommentContainer').rect.screen_location
    # click_loc = tuple(map(int, temp_click_box_Coordinates))
    comment_input_count = 1

    # 每次评论@多少人
    once_comment_people = 5
    # 一共评论多少次
    comment_number = random.randint(5, 5)
    # return
    for once_comment in [lines[i:i + once_comment_people] for i in range(0, len(lines), once_comment_people)][
                        :comment_number]:
        title = page_comment.ele('tag:div@class=DraftEditor-root')
        title.input('Gucci&LV&Chanel')

        # post_box = page_comment.ele('tag:div@data-e2e=comment-post')
        # ac.move_to(post_box).click()
        ac.type(' starting from $19')
        emoji_box = page_comment.ele('tag:div@data-e2e=comment-emoji-icon')
        ac.move_to(emoji_box).click().click().up(300)

        logger.info(f'{comment_user_id}准备开始评论区@流程')
        timeout_count = 0
        for comment in once_comment:
            for _ in range(2):
                ac.type('@').type(comment)
                page_comment.wait(2, 3.5)
                at_all_box = page_comment.wait.ele_loaded('tag:div@data-e2e=comment-at-user', timeout=10).s_ele()
                # break
                if at_all_box:
                    at_box_list = at_all_box.eles('tag:span@data-e2e=comment-at-uniqueid', timeout=10)
                else:
                    at_box_list = []

                user_id_index = 0
                for box in at_box_list:
                    temp = get_string_between_tags(box.html)
                    if temp == comment:
                        break
                    user_id_index += 1

                if user_id_index == len(at_box_list):
                    timeout_count += 1
                    try:
                        ac.type((Keys.CTRL, 'z'))
                    except Exception as e:
                        print(e)
                        title.input('', clear=False)
                        ac.type((Keys.CTRL, 'z'))
                    page_comment.wait(1, 3)
                    continue
                page_comment.wait(0.3, 1)
                id_list_box = page_comment.ele('tag:div@data-e2e=comment-at-user')
                id_box = id_list_box.ele('tag:span@data-e2e=comment-at-uniqueid', index=user_id_index + 1)
                ac.move_to(id_list_box).scroll(on_ele=id_box).click()
                # logger.info(f'{comment_user_id} 当前用户id{comment} 用户id{at_box_list[user_id_index].text}')
                break
            if timeout_count == 2:
                logger.info(f'{comment_user_id} {comment}此用户id无法找到')

        logger.info(f'{comment_user_id}单次评论输入成功')
        # 点击发送评论
        post_box = page_comment.ele('tag:div@data-e2e=comment-post')
        ac.move_to(post_box).click()
        logger.info(f'{comment_user_id}已完成第{comment_input_count}次输入，开始发送评论')
        page_comment.wait(1, 2)
        comment_input_count += 1
        page_comment.wait(2, 3)

    page_comment.get('https://www.tiktok.com/foryou')
    logger.info(f'{comment_user_id}评论区@完成正在回到首页')

    return True


def commentAreaAt(page_comment: Union[ChromiumPage, ChromiumTab], comment_user_id, file_index):
    def get_string_between_tags(s):
        pattern = r'>(.*?)<'
        result = re.search(pattern, s)
        if result:
            return result.group(1)
        else:
            return '//////.......'

    videoUrl_list = ["https://www.tiktok.com/@wuhankgaudw/video/7352361561832377642",
                     "https://www.tiktok.com/@wuhankgaudw/video/7352141368271047978",
                     "https://www.tiktok.com/@wuhankgaudw/video/7327506954903948575",
                     "https://www.tiktok.com/@wuhankgaudw/video/7324876053237796127",
                     "https://www.tiktok.com/@wuhankgaudw/video/7323011907542158622",
                     "https://www.tiktok.com/@wuhankgaudw/video/7322718720193776927",
                     "https://www.tiktok.com/@wuhankgaudw/video/7322635449321753887",
                     "https://www.tiktok.com/@wuhankgaudw/video/7320143431563611422",
                     "https://www.tiktok.com/@wuhankgaudw/video/7320055183377976618",
                     "https://www.tiktok.com/@wuhankgaudw/video/7320054669710052654",
                     "https://www.tiktok.com/@wuhankgaudw/video/7320053666763951406",
                     "https://www.tiktok.com/@wuhankgaudw/video/7320052976784215342",
                     "https://www.tiktok.com/@wuhankgaudw/video/7320052248829119786",
                     "https://www.tiktok.com/@wuhankgaudw/video/7319769114392743199",
                     "https://www.tiktok.com/@wuhankgaudw/video/7319683281941810462",
                     "https://www.tiktok.com/@wuhankgaudw/video/7319384733329198366",
                     "https://www.tiktok.com/@wuhankgaudw/video/7316784758216805663",
                     "https://www.tiktok.com/@wuhankgaudw/video/7316704487048006943",
                     "https://www.tiktok.com/@wuhankgaudw/video/7316418916568403230",
                     "https://www.tiktok.com/@wuhankgaudw/video/7316361612728814879",
                     "https://www.tiktok.com/@wuhankgaudw/video/7315673436993375519",
                     "https://www.tiktok.com/@wuhankgaudw/video/7315609906072046878",
                     "https://www.tiktok.com/@wuhankgaudw/video/7315227351170796830",
                     "https://www.tiktok.com/@wuhankgaudw/video/7314948490969304350",
                     "https://www.tiktok.com/@wuhankgaudw/video/7314491195365887262",
                     "https://www.tiktok.com/@wuhankgaudw/video/7314109903113587998",
                     "https://www.tiktok.com/@wuhankgaudw/video/7313829725103770910",
                     "https://www.tiktok.com/@wuhankgaudw/video/7313739269741317407",
                     "https://www.tiktok.com/@wuhankgaudw/video/7313105634357038367",
                     "https://www.tiktok.com/@wuhankgaudw/video/7313075519967284511",
                     "https://www.tiktok.com/@wuhankgaudw/video/7312998306626538783",
                     "https://www.tiktok.com/@wuhankgaudw/video/7312740410651184415",
                     "https://www.tiktok.com/@wuhankgaudw/video/7312727649032473887",
                     "https://www.tiktok.com/@wuhankgaudw/video/7312701521504800031",
                     "https://www.tiktok.com/@wuhankgaudw/video/7312372622275153183"]

    page_comment.get(random.choice(videoUrl_list))

    # 滑块验证
    if not my_utils.validation(page_comment, comment_user_id):
        logger.info(f'{comment_user_id}滑块验证失败，请检查原因')
        return False, 'error'

    title = page_comment.ele('tag:div@class=DraftEditor-root')

    file_path = f'./split/split_{file_index}.txt'
    try:
        with open(file_path, 'r', encoding='utf8') as comment_f:
            lines = [line.strip() for line in comment_f.readlines()]
    except:
        logger.error(f'{comment_user_id},用户id文件已用完，请添加新文件后再运行')
        return False, '123'

    at_box = page_comment.ele('tag:div@data-e2e=comment-at-icon', timeout=10).ele('tag:svg')
    if at_box:
        page_comment.scroll.to_see(at_box)
    else:
        logger.error(f'{comment_user_id}可能出现网络问题，请检查错误原因')
        return False, 'network_error'

    logger.info(f'{comment_user_id}开始输入评论')

    ac = Actions(page_comment)
    temp_click_box = page_comment.ele('tag:p@class:PCommentTitle')
    comment_input_count = 1
    for once_comment in [lines[i:i + 2] for i in range(0, len(lines), 2)][:3]:
        title.input('Gucci&LV&Chanel')
        ac.type(' starting from $19').click(temp_click_box)
        title.input('', clear=False)

        # page_comment.ele('tag:div@data-e2e=comment-at-icon').click()
        timeout_count = 0
        for comment in once_comment:
            for _ in range(2):
                ac.type('@').type(comment)
                at_all_box = page_comment.wait.ele_loaded('tag:div@data-e2e=comment-at-user', timeout=10)
                # break
                if at_all_box:
                    at_box_list = at_all_box.eles('tag:span@data-e2e=comment-at-uniqueid', timeout=10)
                else:
                    at_box_list = []

                user_id_index = 0
                for box in at_box_list:
                    temp = get_string_between_tags(box.html)
                    if temp == comment:
                        break
                    user_id_index += 1

                if user_id_index == len(at_box_list):
                    # logger.info(f'{user_id_index}----{len(id_text_list)}')
                    timeout_count += 1
                    try:
                        ac.type((Keys.CTRL, 'z'))
                    except Exception as e:
                        print(e)
                        title.input('', clear=False)
                        ac.type((Keys.CTRL, 'z'))
                    page_comment.wait(1, 3)
                    continue

                ac.move_to(at_all_box).scroll(on_ele=at_box_list[user_id_index])
                logger.info(f'{comment_user_id} 当前用户id{comment} 用户id{at_box_list[user_id_index].text}')
                at_box_list[user_id_index].click()
                break
            if timeout_count == 3:
                logger.info(f'{comment_user_id} {comment}此用户id无法找到')
            page_comment.wait(0.5, 1.5)
        logger.info(f'{comment_user_id}单次评论输入成功')
        page_comment.ele('tag:div@data-e2e=comment-post').click()
        logger.info(f'{comment_user_id}已完成第{comment_input_count}次输入，开始发送评论')
        page_comment.wait(1, 2)
        comment_input_count += 1

    page_comment.get('https://www.tiktok.com/foryou')
    logger.info(f'{comment_user_id}评论区@完成正在回到首页')

    return True, '1414'


def resetTabBar(page_reset: Union[ChromiumPage, ChromiumTab]):
    for _ in range(page_reset.tabs_count - 1):
        page_reset.close()

    page_reset.get_tab(1).get('https://www.tiktok.com/')


def collecting_userFans(page_coll_userFans: Union[ChromiumPage, ChromiumTab], coll_fans_user_id,
                        user_url, stop_event: threading.Event):
    page_coll_userFans.get(user_url)
    page_coll_userFans.wait(10, 15)

    page_coll_userFans.ele('tag:strong@title=Followers', timeout=5).click()

    fans_box = page_coll_userFans.ele('tag:section@role=dialog', timeout=5)
    ac = Actions(page_coll_userFans)
    fan_box = fans_box.eles('tag:span@class:SpanNickname', timeout=5)[0]
    logger.info(fan_box.text)
    ac.move_to(fan_box)

    logger.info(f'{coll_fans_user_id}开始滚动用户列表')
    scroll_count = 1
    while not stop_event.is_set():
        ac.scroll(0, 1000)
        logger.info(f'{coll_fans_user_id}正在进行第{scroll_count}次滚动')
        scroll_count += 1
        page_coll_userFans.wait(3, 4)
        if scroll_count == 120:
            stop_event.set()
            break

    pass


# 222 229 228 234 236 235 248 246 250 258 218 211

if __name__ == '__main__':
    x = [1, 2, 3, 4, 5, 6, 7, 5, 4, 5, 4, 1, 555]
    print(x[:3])
