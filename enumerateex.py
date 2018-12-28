from threading import *
import time
def display():
    print(current_thread().name,'started')
    time.sleep(3)
    print(current_thread().name,'ended')
print('The number of active thread',active_count())

t1 = Thread(target=display,name='Child thread-1')
t2 = Thread(target=display,name='Child thread-2')
t3 = Thread(target=display,name='Child thread-3')
t1.start()
t2.start()
t3.start()
t1.join(5)
t2.join(5)
t3.join(5)
l = enumerate()
for t in l:
    print(t.name,'Name')
