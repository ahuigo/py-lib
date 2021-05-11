#!/usr/local/bin/python3
import os, sys, time
import psutil
from datetime import date
from multiprocessing import Process

def worker():
    print('worker pid:',os.getpid())
    for i in range(50):
        f = open('a.txt', 'a')
        date = time.ctime() +"\n"
        f.write(date)
        f.flush()
        time.sleep(3)


def main():
    print("mainid:",os.getpid())
    pid = os.fork()
    if pid == 0:
        task = Process(target=worker, args=())
        task.start()
        print('parent pid:',os.getpid())
        time.sleep(300)
    else:
        time.sleep(300)

if __name__ =='__main__':
    main()


'''
# 启动后
    $ pstree -p 30842
         \-+= 30842 ahui Python kill-parent.py
           \-+- 30857 ahui Python kill-parent.py
             |--- 30858 ahui Python -c from multiprocessing.resource_tracker import main;main(3)

# 杀parent:
    $ kill 30857

# 子进程会正常运行
    $ pstree -p 30858
    -+= 00001 root /sbin/launchd
     \--- 30858 ahui Python -c from multiprocessing.resource_tracker import main;main(3)

# parent 会变成僵尸
    $ ps aux|grep Z
    USER               PID  %CPU %MEM      VSZ    RSS   TT  STAT STARTED      TIME COMMAND
    ahui             30857   0.0  0.0        0      0 s029  Z+    4:27PM   0:00.00 (Python)

    $ pstree -p 30842
             \-+= 30842 ahui  kill-parent.py
               \--- 30857 ahui (Python)
'''
