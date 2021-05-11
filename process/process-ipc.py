#!/usr/local/bin/python3
import os, sys, time
import psutil
from multiprocessing import Manager
from multiprocessing import Process

def task(pids):
    pid = os.getpid()
    pids.append(pid)
    print('run task(pid): ', pid)
    time.sleep(1000)

class Worker(object):
    def __init__(self):
        self.pids = Manager().list()
        self._monitor_process = Process(target=self.monitor_zombie, args=(self.pids,))
        self._monitor_process.start()

    def start(self):
        pids = self.pids
        t = Process(target=task, args=(pids,))
        t.start()
        
    def monitor_zombie(self, pids):
        while True:
            print("start monitor pids:")
            for pid in pids:
                print("monitor pids:", pid)
            time.sleep(5)



if __name__ == '__main__':
    wo = Worker()
    for i in range(10):
        time.sleep(2)
        print("start task:", i)
        wo.start()
    time.sleep(1000)

