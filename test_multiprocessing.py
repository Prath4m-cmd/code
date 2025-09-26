# Processes that run in parallel
### cpu- bound task: tasks that are heavy on CPU usage (e.g mathematical computation, data processing)
# parallel execution- multiple cores of the CPU


import multiprocessing
import time

def square_numbers():
    for i in range(5):
        time.sleep(1)
        print(f"Square:{i*i}")

def cube_numbers():
    for i in range(5):
        time.sleep(1.5)
        print(f"cube : {i*i*i}")

if __name__=="__main__":

    ## create 2 processes
    p1=multiprocessing.Process(target=square_numbers)
    p2 = multiprocessing.Process(target=cube_numbers)

    t=time.time()
    # start the processes
    p1.start()
    p2.start()

    # wait for processes to complete
    p1.join()
    p2.join()

    finish_time = time.time()-t
    print(finish_time)