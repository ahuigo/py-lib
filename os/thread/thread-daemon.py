import queue
import threading
from threading import Thread
import time

def producer(n):
    for i in range(n):
        item = f'item-{i}'
        print(f'Produced {item}')
        time.sleep(2)

num_items = 5
producer_thread = threading.Thread(target=producer, args=(num_items,))
producer_thread.daemon = True  # 设置为守护线程
producer_thread.start()

print('end')
