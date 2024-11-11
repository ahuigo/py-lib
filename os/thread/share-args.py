import queue
import threading
from threading import Thread
import time

class producer(Thread):
    n = 0
    store = None
    def __init__(self, n=0, store=None):
        super().__init__()
        self.n=n
        self.store = store

    def run(self):
        for i in range(self.n):
            item = f'item-{i}'
            print(f'Produced {item}')
            if type(self.store) == list:
                self.store.append(item)
            time.sleep(0.1)
    def set_store(self,store):
        self.store=store

def main():
    num_items = 10
    store = []
    p = producer(num_items)
    #p.daemon = True  # 设置为守护线程
    p.start()
    time.sleep(0.2)
    p.set_store(store)
    time.sleep(0.5)
    assert 4<=len(store)<=6
    print('store list:',store)

main()
