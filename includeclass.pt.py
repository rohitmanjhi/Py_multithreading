from threading import *
def Mythread(Thread):
    def run(self):
        for i in range(10):
            print("Child Thread")

t = Mythread()
t.start()
for i in range(10):
    print("Main THread")
