# -*- coding: utf-8 -*-
"""
Created on Mon Aug 15 15:38:56 2016

@author: WangHaiTao
"""
import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(-1,1,10)
y=x**2

fig=plt.figure(figsize=(8,4))
ax=plt.subplot(111)
plt.plot(x,y)

for i,(_x,_y) in enumerate(zip(x,y)):
    plt.text(_x,_y,str(i),color="red",fontsize=i+10)
plt.text(0.5,0.8,u"text in axis",color="blue",ha="center",transform=ax.transAxes)
plt.figtext(0.1,0.92,u"text in charm",color="green")
plt.show()