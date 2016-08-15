# -*- coding: utf-8 -*-
"""
Created on Mon Aug 15 13:37:10 2016

@author: WangHaiTao
"""
from matplotlib.font_manager import fontManager
import matplotlib.pyplot as plt
import os

fig=plt.figure(figsize=(12,6))
ax=fig.add_subplot(111)
plt.subplots_adjust(0,0,1,1,0,0)
plt.xticks([])
plt.yticks([])
x,y=0.05,0.08
fonts=[font.name for font in fontManager.ttflist if 
os.path.exists(font.fname) and os.stat(font.fname).st_size>1e6]
font=set(fonts)#利用os中的stat()获取字体文件的大小，并保留大于1MB的所有字体文件
dy=(1.0-y)/(len(fonts)/4+(len(fonts)%4!=0))
for font in fonts:
#调用子图对象的text()并在其中添加文字
    t=ax.text(x,y,u"中文字体",{'fontname':font,'fontsize':15},transform=ax.transAxes)
    ax.text(x,y-dy/2,font,transform=ax.transAxes) 
    x+=0.25
    if x>=1.0:
        y+=dy
        x=0.05
plt.show()
