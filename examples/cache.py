
import logging
import sys
import os
import time
import adbutils


sys.path.insert(0, os.getcwd())


from uiautomator2.init import Initer
import uiautomator2 as u2



def main():
    device = adbutils.adb.device(None)
    init = Initer(device, loglevel=logging.DEBUG)
    init.cache()




if __name__ == '__main__':
    main()