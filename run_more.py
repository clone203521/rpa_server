import random
from datetime import datetime

import listener_facebook_process as run_listen_face
import run_process as run_tk
import run_process_face as run_face


def run_loop(run_count):
    platformType_tk = 'tik_all'
    # platformType_face = 'facebook_4_10'
    face_list = 'facebook_account'
    face_list = 'none'

    flag_y = input('是否重置文件: ')
    if flag_y == 'y' or flag_y == 'Y':
        with open(f'./txt_path/{platformType_tk}_complete_id.txt', 'w', encoding='utf8') as f:
            f.write('')
        with open(f'./txt_path/{face_list}_complete_id.txt', 'w', encoding='utf8') as f:
            f.write('')
    original_time = datetime.now()
    current_time = f'{original_time.strftime("%m-%d")}'
    get_group_flag = False

    while True:
        # print('count=', run_count)
        if run_count < 2:
            # if run_count == 0:
            #     my_utils.move_video_txt(platformType_tk)
            run_tk.run(1, platformType_tk, 8)
        elif 2 <= run_count < 4:
            run_tk.run(2, platformType_tk, 12)
        elif 4 <= run_count < 6:
            run_tk.run(3, platformType_tk, 12)
        elif 8 <= run_count < 10:
            run_listen_face.run(2, face_list, 10)
        elif 6 <= run_count < 8:
            run_face.run2(1, face_list, 10)
        elif 10 <= run_count < 12:
            run_tk.run(2, platformType_tk, 12)
        elif 14 <= run_count < 16:
            run_listen_face.run(2, face_list, 10)
        elif 20 <= run_count < 22:
            run_face.run2(1, face_list, 10)
        else:
            original_time = datetime.now()
            temp_time = f'{original_time.strftime("%m-%d")}'
            if temp_time != current_time:
                current_time = temp_time
                get_group_flag = False
                run_listen_face.run(1, face_list, 10)

            if random.random() < 0.4:
                run_tk.run(2, platformType_tk, 12)
            elif random.random() < 0.1:
                run_listen_face.run(2, face_list, 10)
            elif random.random() < 0.4:
                run_face.run2(1, face_list, 10)
            else:
                pass
            with open(f'./txt_path/{platformType_tk}_complete_id.txt', 'w', encoding='utf8') as f:
                f.write('')
            with open(f'./txt_path/{face_list}_complete_id.txt', 'w', encoding='utf8') as f:
                f.write('')
        run_count += 1

        if run_count % 2 == 0:
            with open(f'./txt_path/{platformType_tk}_complete_id.txt', 'w', encoding='utf8') as f:
                f.write('')
            with open(f'./txt_path/{face_list}_complete_id.txt', 'w', encoding='utf8') as f:
                f.write('')

        if get_group_flag:
            run_listen_face.run(1, face_list, 10)
            get_group_flag = False
            continue


if __name__ == '__main__':
    model_list_tk = ['modify_personal_data', 'upload_video', 'brushVideo', 'commentAreaAt']
    face_model = ['login_init', 'brushPost', 'joinGroup']
    face_listen = ['get_group_info', 'get_group_userId', 'listen_group_comment']

    count = 2

    run_loop(count)
