import threading
import time

def worker(n):
    time.sleep(2)
    print threading.currentThread().getName(), 'Exiting'+str(n)

for i in xrange(5):
    t = threading.Thread(target=worker,name='worker',args=[i])
    t.start()


