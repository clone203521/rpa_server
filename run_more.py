import listener_facebook_process as run_listen_face
import run_process as run_tk
import run_process_face as run_face

if __name__ == '__main__':
    model_list = ['modify_personal_data', 'upload_video', 'brushVideo', 'commentAreaAt']
    face_model = ['login_init', 'brushPost', 'joinGroup']
    model_list_run = ['get_group_info', 'get_group_userId', 'listen_group_comment']

    count = 3
    platformType_tk = 'tik_all'
    platformType_face = 'facebook_4_10'
    face_list = 'facebook_account'
    while True:
        if count < 2:
            run_tk.run(1, platformType_tk, 8)
        elif 2 <= count < 4:
            run_tk.run(2, platformType_tk, 12)
        elif 4 <= count < 6:
            run_tk.run(3, platformType_tk, 12)
        elif 6 <= count < 8:
            run_listen_face.run(2, face_list, 10)
        elif 8 <= count < 10:
            run_face.run2(1, platformType_face, 9)
        else:
            run_tk.run(2, platformType_tk, 12)
        if count % 2 == 0:
            with open(f'./txt_path/{platformType_tk}_complete_id.txt', 'w', encoding='utf8') as f:
                f.write('')
            with open(f'./txt_path/{platformType_face}_complete_id.txt', 'w', encoding='utf8') as f:
                f.write('')
        count += 1
