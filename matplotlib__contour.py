# -*- coding: utf-8 -*-
"""
Created on Tue Aug 16 09:11:10 2016

@author: WangHaiTao
"""
#等值线图
import numpy as np
import matplotlib.pyplot as plt
y,x=np.ogrid[-2:2:200j,-3:3:300j]

z=x*np.exp(-x**2-y**2)

extent=[np.min(x),np.max(x),np.min(y),np.max(y)]

plt.figure(figsize=(10,4))
plt.subplot(121)
cs=plt.contour(z,10,extent=extent)#调用contourf()绘制数组Z的等值线图，extent指令X轴和Y轴的范围
plt.clabel(cs)
plt.subplot(122)
plt.contourf(x.reshape(-1),y.reshape(-1),z,20)#调用contour()，绘制将取值范围分成20份，带填充效果的等值线图
plt.show()
