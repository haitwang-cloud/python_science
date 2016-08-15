# -*- coding: utf-8 -*-
"""
Created on Mon Aug 15 09:23:34 2016

@author: WangHaiTao
"""
import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(0,10,1000)
y=np.sin(x)
z=np.cos(x**2)

plt.figure(figsize=(8,4))#调用figure()来创建一个Figure对象，
#指定宽度和高度（单位：inch）

plt.plot(x,y,label="$sin(x)$",color="red",linewidth=2)
plt.plot(x,z,"b--",label="$cos(x**2)$")#通过b--来指定曲线的颜色和线形，
#b为blue,--为虚线，可通过plt.plot?查看

plt.xlabel("Time(s)")
plt.ylabel("Volt")
plt.title("First demo plt")
plt.ylim(-1.1,1.1)
plt.legend()#x轴和y轴的显示范围

plt.show()#最后调用plt.show()显示绘图窗口
#run matplotlib_demo_plot.py
#plt.savefig("test.png",dpi=120)