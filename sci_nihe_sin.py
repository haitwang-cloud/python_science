# -*- coding: utf-8 -*-
"""
Created on Fri Aug 12 15:33:01 2016

@author: WangHaiTao
"""
import numpy as np
from scipy.optimize import leastsq
def func(x,p):
    A,k,theta=p
    return A*np.sin(2*np.pi*k*x+theta)
def residuals(p,y,x):
    """拟合x,y和拟合函数的差值，p为拟合需得到的参数"""
    return y-func(x,p)
    
x=np.linspace(0,2*np.pi,100)
A,k,theta=10,0.44,np.pi/6#真是数据的函数参数
y0=func(x,[A,k,theta])#真实数据
#加入噪声的实验数据
y1=y0+2*np.random.randn(len(x))
p0=[7,0.5,0] #第一次猜测的函数拟合参数

#调用leastsq进行数据拟合
#residuals为计算误差的函数
#p0为拟合参数的初始值
#args为需要拟合的实验数据
plsq=leastsq(residuals,p0,args=(y1,x))
print u"真实参数",[A,k,theta]
print u"拟合参数",plsq[0]
