import sys
import os
import time

sys.path.insert(0, os.getcwd())


import uiautomator2 as u2





def reset() :
    u2.cfg(u2.CFG_RESET_ADB_WIFI_ADDR, '192.168.1.242:33799')
    u2.cfg(u2.CFG_RESET_ATX_LISTEN_ADDR, ':7912')


    d = u2.connect_wifi('192.168.1.242')
    print(d.device_info)

    

    print('sleep now')
    time.sleep(10)

    print('reset now')
    d.reset_uiautomator()


if __name__ == '__main__':
    reset()
