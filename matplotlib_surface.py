# -*- coding: utf-8 -*-
"""
Created on Wed Aug 17 09:37:15 2016

@author: WangHaiTao
"""
import numpy as np
import matplotlib.pyplot as plt

x,y=np.mgrid[-2:2:20j,-2:2:20j]
z=x*np.exp(-x**2-y**2)
ax=plt.subplot(111,projection='3d')
ax.plot_surface(x,y,z,rstride=2,cstride=1,cmap=plt.cm.Blues_r)
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")
plt.show()
 
