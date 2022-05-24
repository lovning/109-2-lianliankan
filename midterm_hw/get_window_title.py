# -*- coding: utf-8 -*-
import win32gui

hwnd_title = {}
def get_all_hwnd(hwnd, mouse):
    if (win32gui.IsWindow(hwnd)
            and win32gui.IsWindowEnabled(hwnd)
            and win32gui.IsWindowVisible(hwnd)):
        hwnd_title.update({hwnd: win32gui.GetWindowText(hwnd)})
def print_hwnd_title():
    win32gui.EnumWindows(get_all_hwnd, 0)
    print(hwnd_title)
    for h, t in hwnd_title.items():
        if t :
            print (h, t.encode('utf-8').decode('utf-8'))