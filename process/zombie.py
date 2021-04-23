#!/usr/local/bin/python3
import os, sys, time
import psutil

ttl=60


for i in range(10):
    pid = os.fork()
    if pid == 0:
        print('查看zombie: ps aux | grep Z')
        print('child:',os.getpid())
        p = psutil.Process(os.getpid())
        l = '1'*1024*1024*1024
        print("len:",len(l))
        mem=p.memory_info().rss / 1024 ** 2
        print("mem:",mem, "M")
        time.sleep(15)
        print("exit mem:",mem)
        sys.exit(0)

print("mainid:",os.getpid())
time.sleep(ttl)
os.wait() 
