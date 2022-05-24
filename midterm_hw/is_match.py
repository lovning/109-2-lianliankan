# -*- coding: utf-8 -*-
import numpy as np

graph = np.zeros((14, 8), dtype=np.int32)
def make_regalur_image(img, size=(20, 20)):
    gray_image = img.resize(size).convert('RGB')
    return gray_image
# 計算直方圖
def hist_similar(lh, rh):
    assert len(lh) == len(rh)
    hist = sum(1 - (0 if l == r else float(abs(l - r)) / max(l, r)) for l, r in zip(lh, rh)) / len(lh)
    return hist
# 計算相似度
def calc_similar(li, ri):
    calc_sim = hist_similar(li.histogram(), ri.histogram())
    return calc_sim
def is_match(im1,im2):
    if calc_similar(im1,im2)>0.60:
        return True
    return False