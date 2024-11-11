import queue
import threading
import time

# Define a worker function to put items into the queue
def producer(q, n):
    for i in range(n):
        item = f'item-{i}'
        q.put(item)
        print(f'Produced {item}')
        time.sleep(1)

# Define a worker function to get items from the queue
def consumer(q, n):
    for i in range(n):
        item = q.get()
        print(f'Consumed {item}')
        q.task_done()
        time.sleep(2)

# Create a Queue instance
q = queue.Queue()

# Number of items to produce/consume
num_items = 5

# Create producer and consumer threads
producer_thread = threading.Thread(target=producer, args=(q, num_items))
consumer_thread = threading.Thread(target=consumer, args=(q, num_items))

# Start the threads
producer_thread.start()
consumer_thread.start()

# Wait for all threads to complete
producer_thread.join()
consumer_thread.join()

# Ensure all items have been processed
q.join()
print('All items have been processed.')
