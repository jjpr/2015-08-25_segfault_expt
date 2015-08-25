__author__ = 'jjpr'

import os, signal
from multiprocessing import Process

def kill_me():
  print("before kill")
  os.kill(os.getpid(), signal.SIGSEGV)
  print("after kill")

def start_process():
  p = Process(target=kill_me)
  p.start()
  print("after start")
  p.join()
  print("after join")

if __name__ == "__main__":
  start_process()
