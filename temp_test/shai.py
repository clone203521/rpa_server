import re

import pandas as pd


def test1():
    df = pd.read_csv('group_info_final.csv')

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
            if float(member_count_str) < 0.5:
                drop_index.append(index)
        elif member_count_str:
            if float(member_count_str) < 5000:
                drop_index.append(index)
        elif ',' in temp_str:
            if float(member_count_str.replace(',', '')) < 5000:
                drop_index.append(index)

    df.drop(drop_index, axis=0, inplace=True)
    print(len(drop_index), '   ', len(df))

    df.to_csv('group_info_final20.csv', index=False)


if __name__ == '__main__':
    test1()
