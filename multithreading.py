### Multithreading
## When to use multithreading 
# I/O - bound task: Task that spend more time waiting for I/O operations (e.g file operation, network requests)
## concurent execution: when you eant to improve the throughput of your application by performing multiple operations concurrently.

import threading
import time

def print_numbers():
    for i in range(5):
        time.sleep(2)
        print(f"Number:{i}")

def print_letter():
    for letter in "abcde":
        time.sleep(2)
        print(f"Letter:{letter}")

# t=time.time()
# print_numbers()
# print_letter()
# finish_time = time.time()-t
# print(finish_time)

# creating 2 threads
t1=threading.Thread(target=print_numbers)
t2= threading.Thread(target=print_letter)

t=time.time()
# Start the thread
t1.start()
t2.start()

# wait for the thread to complete
t1.join()
t2.join()


finish_time = time.time()-t
print(finish_time)
