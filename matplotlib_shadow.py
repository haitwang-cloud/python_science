# -*- coding: utf-8 -*-
"""
Created on Mon Aug 15 15:12:22 2016

@author: WangHaiTao
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.transforms as transforms

x=np.arange(0.,2.,0.01)
y=np.sin(2*np.pi*x)

N=7 #阴影的条数
for i in xrange(N,0,-1):
    offset=transforms.ScaledTranslation(i,-i,transforms.IdentityTransform())
    shadow_trans=plt.gca().transData+offset#阴影曲线的坐标转换由shadow_trans完成
    plt.plot(x,y,linewidth=4,color="orange",transform=shadow_trans,alpha=(N-i)/2.0/N)#最后通过transform参数传递给plot()来绘图
plt.plot(x,y,linewidth=4,color='blue')
plt.ylim((-1.5,1.5))
plt.show()

