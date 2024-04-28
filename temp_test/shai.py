import json
import re

import pandas as pd


def test1():
    df = pd.read_csv('group_info_4-17.csv')

    drop_index = []
    # filtered_strings = []
    print(len(df))
    # 选择成员大于5000的字符串
    for index in df.index:
        # 提取成员数量
        temp_str = df['group_members'][index]
        member_count_str = re.match(r'^[0-9,.]*', temp_str).group(0)
        print(member_count_str)
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
    print(len(drop_index), '   ', len(df))

    df.to_csv('group_info_final20.csv', index=False)


def excel_test():
    df = pd.read_excel('4.19Tk数据.xlsx', sheet_name='Sheet2')
    before_set = {}
    for index, row in df.iterrows():
        if isinstance(row['账号2'], float):
            break
        before_set.update({row['账号2']: row['评论数2']})
    print(before_set)

    new_col = [None for _ in range(len(df))]
    for index, row in df.iterrows():
        if isinstance(row['账号1'], float):
            break
        if row['账号1'] in before_set:
            new_col[index] = before_set[row['账号1']]
    df['评论数3'] = new_col
    df.to_excel('group_info_final20.xlsx', index=False)


def tiqu():
    with open('x1.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    with open('x1.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


if __name__ == '__main__':
    # test1()
    # excel_test()
    tiqu()
