import os
import subprocess

ds = subprocess.Popen(r'python test.py',creationflags =subprocess.CREATE_NEW_CONSOLE)
ds.wait()
