import subprocess
import argparse

class server:
    def __init__(self, file_path) -> None:
        self.process = []
        self.file_path = file_path


    def create_process(self):
        new_process = subprocess.Popen(f'python DSL/server/process.py --id {str(len(self.process))} --file_path {self.file_path}',\
                        creationflags =subprocess.CREATE_NEW_CONSOLE)
        new_process.wait()
        self.process.append(new_process)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--file_path', type=str, required=True)
    args = parser.parse_args()
    myServer = server(args.file_path)
    myServer.create_process()