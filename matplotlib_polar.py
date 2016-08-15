# -*- coding: utf-8 -*-
"""
Created on Mon Aug 15 16:07:09 2016

@author: WangHaiTao
"""
import numpy as np
import matplotlib.pyplot as plt

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
