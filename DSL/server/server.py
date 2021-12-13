from enum import EnumMeta
from logging import log
import threading
from types import coroutine, prepare_class
from pynput.keyboard import Key, Listener
from DSL.util.logger import get_core_logger, get_user_logger
import subprocess
import argparse
from queue import Queue
from threading import Thread
from rich.progress import track
from rich import print
from rich.console import Console
from rich.table import Table
import time
import os

thread_queue = Queue()
class server:
    def __init__(self, file_path) -> None:
        self.process = []
        self.process_info = []
        self.file_path = file_path
        self.console = Console()


    def create_process(self):
        id = str(len(self.process))
        start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        state = "running"
        new_process = subprocess.Popen(f'python DSL/server/process.py --id {str(len(self.process))} --file_path {self.file_path}',\
                        creationflags =subprocess.CREATE_NEW_CONSOLE)
        self.process.append(new_process)
        self.process_info.append([id, start_time, state])

    def print_state(self):

        for id,process in enumerate(self.process):
            if process.poll() == 0:
                self.process_info[id][2] = "over"
            elif not process.poll() == None:
                self.process_info[id][2] = "error"


        table = Table(show_header=True, header_style="bold magenta")
        table.add_column("process_id", style="dim", width=12)
        table.add_column("start_time")
        table.add_column("state", justify="right")
        for process_info in self.process_info:
            color = "green" if process_info[2] == 'running' else "red"
            state = "[" + color + "]" + process_info[2] + "[/" + color + "]"
            table.add_row( "[bold]" + process_info[0] + "[/bold]", process_info[1], state)
        os.system('cls') 
        self.console.print(table)  


    def main(self):
        for s in track(range(10), description='正在启动系统....'):
            time.sleep(0.3)
            
        thread = Thread(target=self.key_board_listen)
        thread.start()
        while True:
            try:
                value = thread_queue.get(timeout=1)
            except:
                value = ""
            if value == "creat":
                self.create_process()
            elif value == "over":
                thread.join()
                for process in track(self.process, description='正在杀死未结束进程...'): 
                    time.sleep(1) 
                    process.kill()   
                    self.print_state()    
                break
            self.print_state()


    def key_board_listen(self):
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
    

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--file_path', type=str, required=True)
    args = parser.parse_args()
    myServer = server(args.file_path)
    myServer.main()