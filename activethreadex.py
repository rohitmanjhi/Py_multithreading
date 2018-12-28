from threading import *
import time
def display():
    print(current_thread().name,'started\n')
    time.sleep(3)
    print(current_thread().name,'ended\n')
print('The number of active thread',active_count())

t1 = Thread(target=display,name='Child thread-1\n')
t2 = Thread(target=display,name='Child thread-2\n')
t3 = Thread(target=display,name='Child thread-3\n')
t1.start()
t2.start()
t3.start()
print("THe number of active thread\n",active_count())
time.sleep(10)
print("THe number of active thread\n",active_count())
