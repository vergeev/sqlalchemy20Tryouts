# SQLALchemy uses module registry (sqlalchemy.util.preloaded._ModuleRegistry)
# citing issue with __import__: https://github.com/python/cpython/issues/83065
# I used the following code in order to dig deeper into the issue.
import importlib
import threading


# examples from the original reproducer
def t1():
    return __import__(name="package.subpackage", level=0)

def t2():
    return __import__(name="package.subpackage.module", level=0)

# importlib.import_module, suggested in the docstring of __import__
# also causes deadlock
def t3():
    return importlib.import_module(name="package.subpackage")

def t4():
    return importlib.import_module(name="package.subpackage.module")

# You can't really import sqlalchemy programmatically.
# Importing fails because of
# barebones calls
# __import__()
# importlib.import_module()
# mid-module in
# sqlalchemy.util.preloaded
def t5():
    return __import__(name="sqlalchemy", level=0)

threads = []
# here, I plug in (t1, t2), (t5, t6), t3
# I didn't find any way to catch _frozen_importlib._DeadlockError
threads.append(threading.Thread(target=t3))
threads.append(threading.Thread(target=t4))

for thread in threads:
    thread.start()
