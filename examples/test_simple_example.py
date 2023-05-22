# coding: utf-8
#

import sys
import os

sys.path.insert(0, os.getcwd())

import uiautomator2 as u2


def test_simple():
    d = u2.connect()
    print(d.info)


def test_stop_app() :
    d = u2.connect()
    d.app_stop("com.tencent.wework", user_id='999')


def test_app_current() :
    d = u2.connect()
    print(d.app_current())

if __name__ == "__main__":
    #test_simple()
    #test_stop_app()
    test_app_current()
