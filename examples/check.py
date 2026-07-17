


import sys
import os
import time

sys.path.insert(0, os.getcwd())


import uiautomator2 as u2



def chkIsRuning() :
    d = u2.connect()
    print(d.isRunning)


def healthCheck() :
    d = u2.connect()
    print(d.healthcheck())


if __name__ == '__main__':
    # chkIsRuning()
    healthCheck()