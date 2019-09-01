#!/usr/bin/python
#-*-coding:utf8-*-
#美好生活从python开始！
from   appium  import webdriver
def  swipe_left(dr,t=500):

    #获取手机屏幕的大小
    a=dr.get_window_size()
    #放缩屏幕
    x1 = a['width']*0.5
    x2 = a['width']*0.75
    y1 = a['height']*0.25
    y2 = a['height']*0.5
    #左滑
    dr.swipe(x2,y1,x1,y1,duration=t)

def swipe_right(dr, t=500):
    a = dr.get_window_size()
    x1 = a['width'] * 0.5
    x2 = a['width'] * 0.75
    y1 = a['height'] * 0.25
    y2 = a['height'] * 0.5
    #右滑
    dr.swipe(x1,y1,x2,y1,duration=t)

def swipe_up(dr, t=500):
    #上滑
    a = dr.get_window_size()
    x1 = a['width'] * 0.5
    x2 = a['width'] * 0.75
    y1 = a['height'] * 0.25
    y2 = a['height'] * 0.5
    dr.swipe(x1, y2, x1, y1, duration=t)

def swipe_down(dr, t=500):
    #下滑
    a = dr.get_window_size()
    x1 = a['width'] * 0.5
    x2 = a['width'] * 0.75
    y1 = a['height'] * 0.25
    y2 = a['height'] * 0.5
    dr.swipe(x1, y1, x1, y2, duration=t)


"""
swipe(self, start_x, start_y, end_x, end_y, duration=None) 
    Swipe from one point to another point, for an optional duration.
    从一个点滑动到另外一个点，duration是持续时间

    :Args:
    - start_x - 开始滑动的x坐标
    - start_y - 开始滑动的y坐标
    - end_x - 结束点x坐标
    - end_y - 结束点y坐标
    - duration - 持续时间，单位毫秒

    :Usage:
    driver.swipe(100, 100, 100, 400)
"""