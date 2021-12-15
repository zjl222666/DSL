'''
overview:
    you can define other muti_process method here
    the main server will creat a thread to run your method
        - once you want to raise a process, you just need to put a string "创建对话"  into thread_queue
        - once you want to shutdown the server ,you just need to put a string "结束退出" into thread_queue
rules:
    input: None
    output: None
    note: 
        1. you need to make the muti_process methord correspond to a string one by one in dict `muti_processer_dict`
setting:
    you can choose your muti_process method in `setting.py`
'''

from pynput import keyboard
from pynput.keyboard import Key, Listener
from SerWise.util.logger import get_core_logger, get_user_logger
from queue import Queue

thread_queue = Queue()



def key_board_listen():
    logger = get_core_logger("keyboard_listen")
    def on_press(key):
        logger.info(f"输入{key}")
    def on_release(key):
        global thread_queue
        if key == Key.tab:
            logger.info(f"创建对话")
            thread_queue.put("creat")
        if key == Key.esc:
            logger.info(f"结束退出")
            thread_queue.put("over")
            return False

    with Listener(on_press=on_press,on_release=on_release) as listener:
        listener.join()


muti_processer_dict = {
    'default': key_board_listen
}