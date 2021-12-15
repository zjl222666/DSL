from logging import log
from SerWise.util.logger import get_core_logger, get_user_logger
from SerWise.server.process import DslProcess
from SerWise.API.muti_process import thread_queue, muti_processer_dict
from SerWise.setting import muti_process_method
import subprocess
import argparse
from threading import Thread
from rich.progress import track
from rich import print
from rich.console import Console
from rich.table import Table
import time
import os
import sys
import signal




class server:
    '''
    Overview:
        The main class of the program, responsible for the scheduling and operation of the process and information feedback
    Parameters:
        - file_path <str>: the file path of the script will be run
    '''
    def __init__(self, file_path) -> None:
        self.process = []
        self.process_info = []
        self.file_path = file_path
        self.console = Console()


    def create_process(self):
        '''
        Overview:
            Start a conversation process
        '''
        id = str(len(self.process))
        start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        state = "running"
        new_process = subprocess.Popen(f'dslProcess --id {str(len(self.process))} --file_path {self.file_path}',\
                        creationflags =subprocess.CREATE_NEW_CONSOLE)
        self.process.append(new_process)
        self.process_info.append([id, start_time, state])

    def print_state(self):
        '''
        Overview:
            Print the current status of all processes
        '''
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
        '''
        Overview:
            the main step of the server
        '''
        for s in track(range(10), description='正在读取脚本....'):
            time.sleep(0.3)
            
        thread = Thread(target=muti_processer_dict[muti_process_method])
        thread.start()


        while True:

            # Attempt to read the process wakeup/end information once per second
            try:
                value = thread_queue.get(timeout=1)
            except:
                value = ""
            

            if value == "creat":
                self.create_process()
            elif value == "over":
                thread.join()
                if sys.platform[0] == 'L':
                    for process in track(self.process, description='正在杀死未结束进程...'): 
                        time.sleep(1)
                        os.kill(process.pid, signal.SIGTERM)                   
                    self.print_state()    
                break
            self.print_state()


    

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--muti_process', action='store_true')
    parser.add_argument('file_path', type=str, help="path of your script file")
    args = parser.parse_args()
    if args.muti_process:
        myServer = server(args.file_path)
        myServer.main()
    else:
        f = open(args.file_path, encoding="utf-8")
        codes = f.readlines()
        f.close()
        process = DslProcess("0", codes, args.file_path)
        process.run()
        
if __name__ == '__main__':
    main()