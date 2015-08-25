__author__ = 'jjpr'

import os, signal
from multiprocessing import Process

def kill_me():
  print("before")
  os.kill(os.getpid(), signal.SIGSEGV)
  print("after")

def start_process():
  p = Process(target=kill_me)
  p.start()
  p.join()

if __name__ == "__main__":
  start_process()