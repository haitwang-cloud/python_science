# -*- coding: utf-8 -*-
"""
Created on Fri Aug 12 19:38:59 2016

@author: WangHaiTao
"""
import numpy as np
from scipy import interpolate
import pylab as pl

x=np.linspace(0,10,11)
y=np.sin(x)

x_new=np.linspace(0,10,101)
pl.plot(x,y,'ro')
for kind in['nearest','zero','slinear','quadratic']:
    f=interpolate.interp1d(x,y,kind=kind)
    y_new=f(x_new)
    pl.plot(x_new,y_new,label=str(kind))
pl.legend(loc='lower right')
pl.show()