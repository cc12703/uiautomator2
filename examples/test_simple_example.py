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


if __name__ == "__main__":
    #test_simple()
    test_stop_app()
