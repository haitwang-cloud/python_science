# -*- coding: utf-8 -*-
"""
Created on Fri Aug 12 19:52:54 2016

@author: WangHaiTao
"""
import numpy as np
from scipy import interpolate
import pylab as pl

x1=np.linspace(0,10,20)
y1=np.sin(x1)
sx1=np.linspace(0,12,100)
sy1=interpolate.UnivariateSpline(x1,y1,s=0)(sx1)

x2=np.linspace(0,20,200)
y2=np.sin(x2)+np.random.standard_normal(len(x2))*0.2
sx2=np.linspace(0,20,200)
sy2=interpolate.UnivariateSpline(x2,y2,s=8)(sx2)
