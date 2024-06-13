import sys
import os
from typing import List


sys.path.insert(0, os.getcwd())

from uiautomator2.xpath import XMLElement
import uiautomator2 as u2






if __name__ == '__main__':
    d = u2.connect_usb()
    item: XMLElement = d.xpath('//*[@resource-id="com.tencent.wework:id/fyf"]').get()

    print(item.build_string())