


import sys
import os

sys.path.insert(0, os.getcwd())


import uiautomator2 as u2






def uninstallByADB() :
    dev = u2.adbutils.adb.device()
    init = u2.init.Initer(dev)
    init.uninstall()


def removeOldFile() :
    dev = u2.adbutils.adb.device()
    init = u2.init.Initer(dev)
    init.removeOldFiles()

if __name__ == '__main__':
   #uninstallByADB()
   removeOldFile()