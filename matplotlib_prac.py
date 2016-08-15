# -*- coding: utf-8 -*-
"""
Created on Mon Aug 15 15:49:55 2016

@author: WangHaiTao
"""
import numpy as np
import matplotlib.pyplot as plt
#用四种不同的坐标系来绘图
w=np.linspace(0.1,1000,1000)
p=np.abs((1/1+0.1j*w))#计算低通滤波器的频率响应

plt.subplot(221)
plt.plot(w,p,linewidth=2)
plt.ylim(0,1.5)

plt.subplot(222)
plt.semilogx(w,p,linewidth=2)
plt.ylim(0,1.5)

plt.subplot(223)
plt.semilogy(w,p,linewidth=2)
plt.ylim(0,1.5)

plt.subplot(224)
plt.loglog(w,p,linewidth=2)
plt.ylim(0,1.5)
"""
#在极坐标系中画图
theta=np.arange(0,2*np.pi,0.02)

plt.subplot(121,polar=True)
plt.plot(theta,1.6*np.ones_like(theta),linewidth=2)
plt.plot(3*theta,theta/3,"--",linewidth=2)

plt.subplot(122,polar=True)
plt.plot(theta,1.4*np.cos(5*theta),"--",linewidth=2)
plt.plot(theta,1.8*np.cos(4*theta),linewidth=2)
plt.rgrids(np.arange(0.5,2,0.5),angle=45)
plt.thetagrids([0,45])
"""