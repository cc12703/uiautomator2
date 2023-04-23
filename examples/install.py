
import sys
import os
import time

sys.path.insert(0, os.getcwd())


import uiautomator2 as u2




def install() :
    u2.installByADBWifi('192.168.43.161:43301', ':7912') 

    dev = u2.connect_wifi('192.168.43.161')
    dev.reset_uiautomator()


def installByADB() :
    dev = u2.adbutils.adb.device()
    init = u2.init.Initer(dev)
    init.install()


if __name__ == '__main__':
   #install() 
   installByADB()