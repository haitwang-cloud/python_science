# -*- coding: utf-8 -*-
"""
Created on Sun Aug 14 12:11:16 2016

@author: WangHaiTao
"""
import numpy as np
import scipy.signal as signal
t=np.arange(0,20,0.1)
x=np.sin(t)
x[np.random.randint(0,len(t),20)]+=np.random.standard_normal(20)*0.6
x2=signal.medfilt(x,5)
print 'x2:',x2
x3=signal.order_filter(x,np.ones(5),3)
print 'x3:',x3
print np.all(x2==x3)

