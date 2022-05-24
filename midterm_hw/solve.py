# -*- coding: utf-8 -*-
import pyautogui
from PIL import ImageGrab, Image
from eliminate import *

def click_on_windows(x,y):
    pyautogui.click(270+(x-1)*126,300+(y-1)*126)
def get_num_graph():
    x1_y1_x2_y2 = (209, 236, 1723, 989)
    img = ImageGrab.grab(x1_y1_x2_y2)
    img.save('img/full.png')
    a = 126#小元素邊長
    X=0;Y=0
    # ============結成小圖=========================
    img_graph = {}; num_graph = {}
    for x in range(12):
        img_graph[x]= {}; num_graph[x] = {}
        if x!=0:
            X=X+a
        if x==1 or x==4 or x==5 or x==7  or x==8 or x==10 or x==11:
            X=X+1
        Y=0
        for y in range(6):
            if y!=0:
                Y=Y+a
            if y==1 or y==4:
                Y=Y+1
            x1_y1_x2_y2=(X,Y,X+120,Y+120)
            ele= img.crop(x1_y1_x2_y2)
            ele.save('img/'+str(x)+'_'+str(y)+'.png')
            img_graph[x][y]=ele
    #============為小圖編號======================
    img_list= [];has_been_match=False;i=1
    for x in range(12):
        for y in range(6):
            #print('here')
            for i in img_list:
                if is_match(img_graph[x][y], i):
                    num_graph[x][y]=img_list.index(i)+1
                    has_been_match=True
            #print('here')
            if not has_been_match:
                num_graph[x][y]=len(img_list)+1
                img_list.append(img_graph[x][y])
            has_been_match = False
    for x in range(1,13):
        for y in range(1,7):
            graph[x][y]=num_graph[x-1][y-1]
    #==========印矩陣============================
    # for y in range(8):
    #     for x in range(14):
    #         print(graph[x][y],end=' ')
    #     print('')
    #=====解矩陣================
def solve():
    #=====取dict===============
    cood={}
    for y in range(1,7):
        for x in range(1,13):
            if cood.get(graph[x][y])==None:
                cood[graph[x][y]]=list()
            x_y = (x, y)
            cood[graph[x][y]].append(x_y)
    #========遍歷dict===================
    num=72
    while num!=0:
        print(num)
        for key in cood:
            for i in range(len(cood[key])):
                for j in range(i+1,len(cood[key])):
                    if graph[cood[key][i][0]][cood[key][i][1]] == 0 or graph[cood[key][j][0]][cood[key][j][1]] == 0:
                        break
                    if can_eliminate(cood[key][i][0],cood[key][i][1],cood[key][j][0],cood[key][j][1]):
                        #print(cood[key][i][0],',',cood[key][i][1],'<==> ',cood[key][j][0],',',cood[key][j][1])
                        graph[cood[key][i][0]][cood[key][i][1]] = 0
                        graph[cood[key][j][0]][cood[key][j][1]] = 0
                        r1=cood[key][i];r2=cood[key][j]
                        click_on_windows(r1[0], r1[1])
                        click_on_windows(r2[0], r2[1])
                        cood[key].remove(r1)
                        cood[key].remove(r2)
                        num=num-2
                        break