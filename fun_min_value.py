# -*- coding: utf-8 -*-
"""
Created on Fri Aug 12 16:06:59 2016

@author: WangHaiTao
计算函数z=(1-x)**2+100*(y-x**2)**2的最小值
"""
import scipy.optimize as opt
import numpy as np
import sys

points=[]
def f(p):
    x,y=p
    z=(1-x)**2+100*(y-x**2)**2
    points.append((x,y,z))
    return z
def fprime(p):#求导函数
    x,y=p
    dx=-2+2*x-400*x*(y-x**2)
    dy=200*y-200*x**2
    return np.array([dx,dy])
    
init_point=(-2,-2)
try:
    method=sys.argv[1]
except:
    method="fmin_bfgs"
fmin_func=opt._dict_[method]
if method in["fmin","fmin_powell"]:
    result=fmin_func(f,init_point)#参数为目标函数和初始值
elif method in["fmin_cg","fmin_bfgs","fmin_l_bfgs_b","fmin_tnc"]:
    #参数为目标函数，初始值和导函数
    result=fmin_func(f,init_point,fprime)
elif method in["fmin_cobyla"]:
    result=fmin_func(f,init_point,[])
else:
    print "fmin function not found"
    sys.exit(0)
###绘图部分
import pylab as pl
p=np.array(points)
xmin,xmax=np.min(p[:,0])-1,np.max(p[:,0])+1
ymin,ymax=np.min(p[:,0])-1,np.max(p[:,0])+1
X,Y=np.ogrid[ymin:ymax:500,xmin:xmax:500j]
Z=np.log10(f((X,Y)))
zmin,zmax=np.min(Z),np.max(Z)
pl.imshow(Z,extent=(xmin,xmax,ymin,ymax),origin="bottom",aspect="auto")
pl.slot(p[:,0],p[:,1])
pl.scatter(p[:,0],p[:,1],c=range(len(p)))
pl.xlim(xmin,ymax)
pl.ylim(ymin,ymax)
pl.show()
