import multiprocessing
import time

def worker(event):
    print("hello world")
    time.sleep(1)
    event.set()

if __name__ == '__main__':
    event = multiprocessing.Event()

    process = multiprocessing.Process(
        target=worker, args=[event])
    process.start()

    event.wait()
    print("finished")
