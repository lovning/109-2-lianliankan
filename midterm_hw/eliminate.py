# -*- coding: utf-8 -*-
from is_match import *

def no_line_eliminate(x1,y1,x2,y2):#挨著的
    if (y1 == y2 and abs(x1-x2)==1) or (x1 == x2 and abs(y1-y2)==1):
        return True
    return False
def one_line_accsess(x1,y1,x2,y2):#有值的(x1,y1)能否到達空白的(x2,y2)
    if graph[x2][y2]!=0:
        return False
    if y1 == y2 and x1<x2:
        for i in range(x1+1, x2+1):
            if graph[i][y1] != 0:
                return False
        return True
    elif y1 == y2 and x1>x2:
        for i in range(x1-1, x2-1,-1):
            if graph[i][y1] != 0:
                return False
        return True
    elif x1 == x2 and y1<y2:
        for j in range(y1+1, y2+1):
            if graph[x1][j] != 0:
                return False
        return True
    elif x1 == x2 and y1>y2:
        for j in range(y1-1, y2-1,-1):
            if graph[x1][j] != 0:
                return False
        return True
    return False
def two_line_access(x1, y1, x2, y2):#有值的(x1,y1)能否到達有值的(x2,y2)
    # 左下右上
    if (x2 - x1) * (y2 - y1) < 0:
        temp_x=min(x1,x2);temp_y=min(y1,y2)
        if one_line_accsess(x1,y1,temp_x,temp_y) and one_line_accsess(x2,y2,temp_x,temp_y):
            return True
        temp_x=max(x1,x2);temp_y=max(y1,y2)
        if one_line_accsess(x1,y1,temp_x,temp_y) and one_line_accsess(x2,y2,temp_x,temp_y):
            return True
    # 左上右下
    elif (x2 - x1) * (y2 - y1) > 0:
        temp_x = min(x1, x2);temp_y = max(y1, y2)
        if one_line_accsess(x1, y1, temp_x, temp_y) and one_line_accsess(x2, y2, temp_x, temp_y):
            return True
        temp_x = max(x1, x2);temp_y = min(y1, y2)
        if one_line_accsess(x1, y1, temp_x, temp_y) and one_line_accsess(x2, y2, temp_x, temp_y):
            return True
    return False
def three_line_access(x1, y1, x2, y2):
    #print('three')
    for i in range(x1+1 , 14):
        if not one_line_accsess(x1,y1,i,y1):
            break
        if two_line_access(i,y1,x2,y2):
            return True
    for i in range(x1-1, -1, -1):
        if not one_line_accsess(x1, y1, i, y1):
            break
        if two_line_access(i, y1, x2, y2):
            return True
    for j in range(y1+1,8):
        if not one_line_accsess(x1,y1,x1,j):
            break
        if two_line_access(x1,j,x2,y2):
            return True
    for j in range(y1-1,-1,-1):
        if not one_line_accsess(x1,y1,x1,j):
            break
        if two_line_access(x1, j, x2, y2):
            return True
    return False
def can_eliminate(x1,y1,x2,y2):
    if no_line_eliminate(x1,y1,x2,y2) or two_line_access(x1,y1,x2,y2) or three_line_access(x1,y1,x2,y2):
        print(x1, ',', y1, ' and ', x2, ',', y2, ' can eliminate')
        return True
    return False