
import sys
import os
import time

sys.path.insert(0, os.getcwd())


import uiautomator2 as u2




def pair() :
   guid = u2.pair_by_wifi('192.168.1.175:36381', 447535)
   serial = list(filter(lambda x: x.startswith(guid), u2.listDeviceSerial()))[0]
   print(serial)

   u2.disconnect_adb_wifi(serial)




if __name__ == '__main__':
   pair() 