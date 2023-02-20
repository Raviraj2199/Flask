import threading
import time
  
def print_1():
    for i in range(5):
        # suspend the current thread.
        time.sleep(1)
        print("1")
  
def print_2():
    for i in range(5):
        # suspend the current thread.
        time.sleep(1.5)
        print("2")
  
# two threads are available in this program.
t1 = threading.Thread(target=print_1)
t2 = threading.Thread(target=print_2)
t1.start()
t2.start()
