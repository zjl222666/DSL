import logging
from DSL.setting import *

user_logger = {}
core_logger = {}

def get_user_logger(file_name):
    global user_logger
    if not file_name  in user_logger:
        logger = logging.getLogger()
        formatter = logging.Formatter('[%(asctime)s] %(message)s')
        
        # 文件打印
        fh = logging.FileHandler("{}.log".format(file_name))
        fh.setFormatter(formatter)

        # 控制台打印
        sh = logging.StreamHandler()
        sh.setFormatter(formatter)

        logger.setLevel(user_logging_level)
        logger.addHandler(fh)
        logger.addHandler(sh)
        user_logger[file_name] = logger
    return user_logger[file_name]

def get_core_logger(file_name):
    global core_logger
    if not file_name in core_logger:
        logger = logging.getLogger()

        formatter = logging.Formatter('[%(asctime)s][%(filename)15s][%(levelname)8s] %(message)s')
        # 文件输出
        fh = logging.FileHandler("{}.log".format(file_name))
        fh.setFormatter(formatter)
        logger.setLevel(core_logging_level)
        logger.addHandler(fh)
        user_logger[file_name] = logger
    return user_logger[file_name]
