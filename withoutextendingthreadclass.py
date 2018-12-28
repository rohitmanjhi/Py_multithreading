from threading import *
class Test:
    def display(self):
        for i in range(10):
            print("Child Thread ",current_thread().getName())
t= Test()
t1 = Thread(target=t.display())
t1.start()
t2 = Thread(target=t.display())
t2.start()
