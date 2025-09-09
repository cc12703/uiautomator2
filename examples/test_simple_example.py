# coding: utf-8
#

import sys
import os

sys.path.insert(0, os.getcwd())

import uiautomator2 as u2

#u2.STATIS = True

def test_click():
    d = u2.connect()
    d(text="消息").click()
    d(text="消息").click_nowait()

def test_simcard() :
    d = u2.connect()
    print(d.simcard_info())

def test_dump() :
    d = u2.connect()
    data = d.dump_hierarchy()
    print(len(data))

def test_exists() :
    d = u2.connect()
    print(d(resourceId='com.tencent.wework:id/l3p').exists())
    print(d(text='消息').exists())

def test_chkurl() :
    d = u2.connect()
    print(d.chkurl_by_cellular(['http://www.baidu.com']))

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
    #test_chkurl()
    #test_click()
    test_simcard()
    test_dump()
    test_exists()
    #test_click()
    #test_retry()
    #test_stop_app()
    #test_app_current()
