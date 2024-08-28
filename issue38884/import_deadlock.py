# Requires pip install tensorflow==2.0.0 tensorflow-transform==0.15.0
import threading

def t1():
    return __import__("package.subpackage", 0)

def t2():
    return __import__("package.subpackage.module", 0)

threads = []
threads.append(threading.Thread(target=t1))
threads.append(threading.Thread(target=t2))

for thread in threads:
    thread.start()
