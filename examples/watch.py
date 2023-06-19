import sys
import os
import time

sys.path.insert(0, os.getcwd())


import uiautomator2 as u2





def testNative():
    d = u2.connect()
    w: u2.WatchNative = d.watch_native("test")
    w.when(text="短信").when(text="同意").click(text="同意")
    w.start()

    try:
        while (True):
            time.sleep(1)
    except KeyboardInterrupt:
        w.stop()


if __name__ == '__main__':
    testNative()