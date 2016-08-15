# -*- coding: utf-8 -*-
"""
Created on Mon Aug 15 16:08:12 2016

@author: WangHaiTao
"""
import numpy as np
import matplotlib.pyplot as plt
plt.figure(figsize=(8,4))
x=np.random.random(100)
y=np.random.random(100)
plt.scatter(x,y,s=x*1000,c=y,marker=(6,1),alpha=0.8,lw=2,facecolor="none")
plt.xlim(0,1)
plt.ylim(0,1)