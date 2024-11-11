import threading

# Lock 是普通锁
# RLock 可重入锁, 同一线程多锁多次,　多线程间会被阻塞
rlock = threading.RLock()

def function_with_rlock():
    if rlock.acquire(blocking=False):
        print("async locking")
        rlock.release()
    rlock.acquire()
    try:
        # 执行一些操作
        print("RLock acquired")
        # 同一个线程可以再次获取锁
        rlock.acquire()
        try:
            print("RLock acquired again")
        finally:
            rlock.release()
    finally:
        rlock.release()


def test():
    thread = threading.Thread(target=function_with_rlock)
    thread.start()
    thread.join()
    with rlock:  
        print("main thread locking...")
        thread = threading.Thread(target=function_with_rlock)
        thread.start()
        thread.join()

test()
