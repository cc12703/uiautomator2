
import sys
import os


sys.path.insert(0, os.getcwd())


import uiautomator2 as u2






def main():
    u = u2.connect()
    ids = u.user_list_id()
    u.app_start('com.tencent.mm', user_id=ids[0])





if __name__ == '__main__':
    main()