from threading import *
import time
class Test:
    def sq(self,num):
        for i in num:
            time.sleep(1)
            print('Square0is',i*i)

    def db(self,num):
        for i in num:
            time.sleep(1)
            print('Double is',2*i)
num = [1,2,3,4,5]
btime = time.time()
t = Test()
t1 = Thread(target=t.sq,args =(num,))
t2 = Thread(target=t.db,args =(num,))
t1.start()
t2.start()
t1.join()
t2.join()
etime=time.time()
print(etime-btime)
