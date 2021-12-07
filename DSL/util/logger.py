import logging
import os
from DSL.setting import *

user_logger = None
core_logger = None

def get_user_logger():
    global user_logger
    id = os.getpid()
    if user_logger is None:
        logger = logging.getLogger()
        formatter = logging.Formatter('[%(asctime)s] %(message)s')
        fh = logging.FileHandler("log_for_{}.txt".format(user_name))
        fh.setFormatter(formatter)
        sh = logging.StreamHandler()
        sh.setFormatter(formatter)
        logger.setLevel(user_logging_level)
        logger.addHandler(fh)
        logger.addHandler(sh)
        user_logger = logger
    return user_logger

def get_core_logger():
    global core_logger
    id = os.getpid()
    if core_logger is None:
        logger = logging.getLogger()
        formatter = logging.Formatter('[%(asctime)s][%(filename)15s][%(levelname)8s] %(message)s')
        fh = logging.FileHandler("log_for_core.txt")
        fh.setFormatter(formatter)
        logger.setLevel(core_logging_level)
        logger.addHandler(fh)
        user_logger = logger
    return user_logger
