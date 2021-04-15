from selenium import webdriver
import time
from selenium.common.exceptions import NoSuchElementException
# -*- coding: utf-8 -*-
import win32gui
import win32con
import os
import sys
import re
import commands
import datetime

def cameraphotos():
    name=datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    a=commands.getoutput("fswebcam --no-banner -r 640x480 "+name+".jpg")
    return name


path="C:\\Users\\2283754\\OneDrive - Jabil\\Desktop\\Projects\\AI\\LTSM\\helmet\\yolov5\\data\\images\\13.jpg"
driver = webdriver.Chrome('./chromedriver')
driver.get("http://10.186.162.179:8888/")

def upload(name):
    login = driver.find_element_by_id("uploader-btn")
    login.click()
    time.sleep(1)
    dialog = win32gui.FindWindow('#32770', u'Open') # 对话框
    ComboBoxEx32 = win32gui.FindWindowEx(dialog, 0, 'ComboBoxEx32', None)
    ComboBox = win32gui.FindWindowEx(ComboBoxEx32, 0, 'ComboBox', None)
    Edit = win32gui.FindWindowEx(ComboBox, 0, 'Edit', None) # 上面三句依次寻找对象，直到找到输入框Edit对象的句柄
    button = win32gui.FindWindowEx(dialog, 0, 'Button', None) # 确定按钮Button
    win32gui.SendMessage(Edit, win32con.WM_SETTEXT, None, path+name) # 往输入框输入绝对地址
    win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button) # 按button
    time.sleep(2)
    result = driver.find_element_by_id("results")
    print(result.get_attribute('value'))
    return result.get_attribute('value')

while 1:
    path1=cameraphotos()
    print(str(path1))
    result1=upload(path1)
    print(result1)

# driver.find_element_by_id(".upload-pic").send_keys(path)