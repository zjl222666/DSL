
'''
overview:
    you can define other input method here and setting in `setting.py`

rules:
    input: None
    output: achieved object 
    note: 
        1. if the output isn't string, you need to make sure there isn't any compare between string and input content in your code
        2. you need to make the input_method correspond to a string one by one in dict `listen_dict`
setting:
    you can choose your input method in `setting.py`

'''
from DSL.util import logger
from DSL.util.logger import get_user_logger
import time
from queue import Queue
from threading import Thread

def keyboard(kwargs):
    # keyboard input
    words = input() 
    return words


def wait_input(q):
    words = input() 
    q.put(words)

q = Queue()
p = None

def clock_listen(kwargs):

    if len(kwargs) == 1 and kwargs[0].isdigit():
        wait_time = int(kwargs[0])
    else:
        wait_time = 10
    global q, p
    if not isinstance(p, Thread) or not p.is_alive():
        if isinstance(p, Thread): p.join()
        p = Thread(target=wait_input, args=(q,))
        p.start()
    result = ""
    for i in range(wait_time):
        if not p.is_alive():
            result = q.get()
            break
        else:
            print("\r 你需要在{}s内完成输入".format(wait_time - i), end='')
        time.sleep(1)
    if result == "":
        print('\r 您已超过规定的输入时间    ', end="")
    return result

listen_dict = {
    "default": keyboard,
    "clock": clock_listen
}




