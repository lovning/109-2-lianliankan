# -*- coding: utf-8 -*-
import win32com.client
from get_window_title import *
from solve import *
import time

def start_lianliankan():
    #print_hwnd_title() 
    #直接調取窗口可能有bug，可以加上下面這句，參考自https://stackoverflow.com/questions/14295337/win32gui-setactivewindow-error-the-specified-procedure-could-not-be-found
    shell = win32com.client.Dispatch("WScript.Shell")
    shell.SendKeys('%')
    hwnd = win32gui.FindWindow(None, "Onet Connect Classic - Google Chrome")  # 获取窗口的句柄
    assert hwnd, "大哥，你還沒打開或者最小化了"
    win32gui.SetForegroundWindow(hwnd)  # 窗口置顶
    get_num_graph()
    solve()
if __name__ == '__main__':
    
    start_lianliankan()

