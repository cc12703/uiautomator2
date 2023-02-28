import sys
import os
import time

sys.path.insert(0, os.getcwd())


import uiautomator2 as u2


# get pid of atx-agent: adb shell ps -A | grep agent 
# kill atx-agent: adb shell kill <pid> 


def reset() :
    d = u2.connect_wifi('192.168.1.242')
    d.settings['reset_adb_wifi_addr'] = '192.168.1.242:34439'
    d.settings['reset_atx_listen_addr'] = ':7912'
    print(d.device_info)

    

    print('sleep now')
    input('wait ....')

    print('reset now')
    d.reset_uiautomator()



def resetByADBWifi() :
    d = u2.connect_adb_wifi('192.168.1.175:34619')

    #d.settings['reset_adb_wifi_addr'] = '192.168.1.242:34439'
    d.settings['reset_atx_listen_addr'] = ':7912'
    d.reset_uiautomator()

    u2.disconnect_adb_wifi('192.168.1.175:34619')



if __name__ == '__main__':
    #reset()
    resetByADBWifi()
