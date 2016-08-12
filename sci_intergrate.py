# -*- coding: utf-8 -*-
"""
Created on Fri Aug 12 20:03:24 2016

@author: WangHaiTao
求数值积分的方法
"""
import numpy as np
def half_circle(x):
    return (1-x**2)**0.5
N=10000#分成N份求和
x=np.linspace(-1,1,N)
dx=x[1]-x[0]
y=half_circle(x)
print 2*dx*np.sum(y)
print np.trapz(y,x)*2#trapz计算以（x,y）为顶点坐标的折现与X轴的所夹面积
from scipy import integrate
pi_half,err=integrate.quad(half_circle,-1,1)#quad为数值积分函数
print pi_half*2
def half_sphere(x,y):
    return (1-x**2-y**2)**0.5
print integrate.dblquad(half_sphere,-1,1,
                  lambda x:-half_circle(x),
                  lambda x:half_circle(x)) #dblquad为二重积分

