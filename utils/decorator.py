import math
import re
import time

from loguru import logger


def reset_file(func):
    def wrapper(*args, **kwargs):
        platformType = None
        for arg in kwargs:
            if 'platformType' in arg:
                platformType = kwargs[arg]
        if platformType is not None:
            xx = input("是否重置文件 Y/N：")
            if xx == 'Y' or xx == 'y':
                with open(f'txt_path/{platformType}_complete_id.txt', 'w') as f:
                    f.write('')
        return func(*args, **kwargs)

    return wrapper


def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        run_time = end_time - start_time
        if run_time < 60:
            logger.info(f'耗时{run_time}秒')
        else:
            logger.info(f'耗时{math.floor(run_time / 60)}分{math.ceil(run_time % 60)}秒')
        return result

    return wrapper
