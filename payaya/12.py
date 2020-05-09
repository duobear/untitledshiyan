# coding=utf-8
import threading  # 导入threading包
from time import sleep
import time


def fun1():
    print("Task 1 executed.")
    time.sleep(3)
    print("Task 1 end.")


def fun2():
    print("Task 2 executed.")
    time.sleep(5)
    print("Task 2 end.")


threads = []
t1 = threading.Thread(target=fun1)
threads.append(t1)
t2 = threading.Thread(target=fun2)
threads.append(t2)

for t in threads:
    # t.setDaemon(True)
    t.start()