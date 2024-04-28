import re
import threading
import time
import urllib
from typing import Union

from DrissionPage._pages.chromium_page import ChromiumPage
from DrissionPage._pages.chromium_tab import ChromiumTab
from loguru import logger


def search_tel(page_searchMore: Union[ChromiumPage, ChromiumTab], user_id, site, keyword):
    def start_process(page_searchMore_sp, user_id_sp, site_sp, keyword_sp, code_list: list):
        while page_searchMore_sp.tabs_count < len(code_list):
            page_searchMore_sp.new_tab()
        threads = []
        # 创建线程并启动
        tab_count = 1
        for code in code_list:
            thread = threading.Thread(target=search_tel_one,
                                      args=(
                                          page_searchMore_sp.get_tab(id_or_num=tab_count), user_id_sp, site_sp, code,
                                          keyword_sp,))
            thread.start()
            tab_count += 1
            threads.append(thread)
            page_searchMore_sp.wait(0.8, 1.2)

        # 等待所有线程完成
        for thread in threads:
            thread.join()

    # 创建事件对象
    country_code_more = [998, 996, 357, 374, 60, 62, 63, 65, 66, 670, 673, 7, 81, 82, 84, 850, 855, 856]

    # 创建线程并启动
    for code_list_more in [country_code_more[i_more:i_more + 4] for i_more in range(0, len(country_code_more), 4)]:
        logger.debug(f'{user_id}当前关键词{keyword}')
        start_process(page_searchMore, user_id, site, keyword, code_list_more)


def search_tel_one(page_searchOne: Union[ChromiumPage, ChromiumTab], user_id_findOne, site_findOne, country_code_one,
                   keyword_findOne):
    query = f'site:{site_findOne} +{country_code_one} {keyword_findOne}'
    url = f'https://google.com/search?q=' + urllib.parse.quote(query)
    logger.debug(
        f'{user_id_findOne}当前组合 网站: {site_findOne},国家代码: {country_code_one},关键词 {keyword_findOne}')
    page_searchOne.get(url)
    page_searchOne.wait(2, 4)
    current_time = time.time()
    count = 1
    while True:
        more_result = page_searchOne.ele('tag:span@@text()=More results')
        if more_result:
            current_time += 3
            more_result.click()
        if time.time() - current_time > 20 or count > 40:
            break
        page_searchOne.scroll.down(2000)
        logger.info(f'{user_id_findOne}当前滚动{count}次')
        count = count + 1
        page_searchOne.wait(3, 5)
    match2 = re.findall(r"\+[\d() -]{13,20}", page_searchOne.html)
    # logger.debug(f'match2')
    result = [re.sub(r'[() -]', "", text) for text in match2]
    # print(result)
    match = list(set(result))
    logger.success(f'{user_id_findOne}采集结果: {match}')
    save_search(match, user_id_findOne, country_code_one, site_findOne, keyword_findOne)


def save_search(tel_list: list, user_id, country_code_save, site: str, keyword):
    site_after = site.split('//')[1].replace('www.', '').split('.')[0]
    with open(f'tel_txt/{user_id}-{keyword}-{site_after}-{country_code_save}-search.txt', 'w', encoding='utf-8') as f:
        f.write('\n'.join(tel_list))


if __name__ == '__main__':
    country_code = [998, 996, 357, 374, 60, 62, 63, 65, 66, 670, 673, 7, 81, 82, 84, 850, 855, 856]
    for i in [country_code[i:i + 4] for i in range(0, len(country_code), 4)]:
        print(i)
    pass
