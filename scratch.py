__author__ = 'jjpr'

import os, signal
from multiprocessing import Process, Queue

def kill_me(q):
  some_stuff = ("foo", 42.0)
  q.put(some_stuff)
  print("before kill")
  os.kill(os.getpid(), signal.SIGSEGV)
  print("after kill")

def start_process():
  q = Queue()
  p = Process(target=kill_me, args=(q,))
  p.start()
  # print("after start")
  stuff = q.get()
  print("after get")
  p.join()
  print("after join")
  print(stuff)

if __name__ == "__main__":
  start_process()
