# coding: utf-8
#

import sys
import os

sys.path.insert(0, os.getcwd())

import uiautomator2 as u2



def test_click():
    d = u2.connect()
    d(resourceId='com.tencent.wework:id/l3p').click_direct()

def test_retry():
    #d = u2.connect()
    d = u2.connect_wifi('xxx')
    print(d.info)

    val = input('wait input')
    print(d.info)




def test_stop_app() :
    d = u2.connect()
    d.app_stop("com.tencent.wework", user_id='999')


def test_app_current() :
    d = u2.connect()
    print(d.app_current())

if __name__ == "__main__":
    test_click()
    #test_retry()
    #test_stop_app()
    #test_app_current()
