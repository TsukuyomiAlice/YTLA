# encode = utf-8

import signal
import time
import os
from core.basic.func import scheduleAndScript


@scheduleAndScript.timeout(3)
def test():
    pid = os.getpid()
    try:
        print(f'test start (pid: {str(pid)})')
        time.sleep(10)
        print(f'test end (pid: {str(pid)})')
    except Exception as e:
        print(f'test failed (pid: {str(pid)})')
        os.kill(pid, signal.SIGTERM)


while True:
    a_pid = os.getpid()
    try:
        print(f'script start (pid: {str(a_pid)})')
        test()
        print(f'script end (pid: {str(a_pid)})')
    except Exception as e:
        print(f'exception caught (pid: {str(a_pid)})')

