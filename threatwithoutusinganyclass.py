from threading import *

def display():
    for i in range(10):
        print("Chile Thread")

t = Thread(target=display)
t.start()
for i in range(10):
       print("main Thread")
