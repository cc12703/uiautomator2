

import sys
import os
from typing import List


sys.path.insert(0, os.getcwd())

from uiautomator2.xpath import XMLElement
import uiautomator2 as u2





if __name__ == '__main__':
    d = u2.connect_usb()
    d.app_start('com.tencent.wework')
    
    items: List[XMLElement] = d.xpath("//*[@resource-id='com.tencent.wework:id/c_7']/android.widget.RelativeLayout").all()
    print(len(items))
    for item in items :
        title = item.xpath(".//android.widget.TextView[@resource-id='com.tencent.wework:id/gc_']").get_text()
        print(title)
        descObj = item.xpath(".//android.widget.TextView[@resource-id='com.tencent.wework:id/k_z']")
        if descObj.exists:
            desc = descObj.get_text()
            print(desc)