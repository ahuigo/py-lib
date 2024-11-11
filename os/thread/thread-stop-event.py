import queue
import threading
from threading import Thread
import time

class Producer(Thread):
    mode = 0 # 0:use running, 1: use _stop_event
    running = True
    _stop_event = threading.Event()
    def __init__(self, mode=0):
        super().__init__()
        self.mode = mode
    def run(self):
        i = 0
        while self.is_run() and i<100:
            i+=1
            print(f'item-{i}')
            time.sleep(0.5)

    def is_run(self):
        if self.mode == 0:
            return self.running # 线程不安全
        return not self._stop_event.is_set()
    def stop(self):
        if self.mode == 0:
            print("stop running")
            self.running = 0
        else:
            print("stop event")
            self._stop_event.set()


producer= Producer(0)
producer.start()
time.sleep(1.5)
producer.stop()
print('main end')
