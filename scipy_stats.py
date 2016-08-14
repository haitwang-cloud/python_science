# -*- coding: utf-8 -*-
"""
Created on Sun Aug 14 13:33:25 2016

@author: WangHaiTao
"""
from scipy import stats
import numpy as np
import pylab as pl
print stats.norm.stats()
X=stats.norm(loc=1.0,scale=2.0)
print X.stats()

x=X.rvs(size=10000)#对随机变量取10000个值
print '期望:',np.mean(x)
print '方差:',np.var(x)
print stats.norm.fit(x)#获得随机序列的期望值和标准差
t=np.arange(-10,10,0.01)
pl.plot(t,X.pdf(t))#绘制概率密度函数的理论值
p,t2=np.histogram(x,bins=100,normed=True)#p表示各个区间取样值出现的频数,t2表示区间
t2=(t2[:-1]+t2[1:])/2
pl.plot(t2,p)
#X的累积分布函数和数组p的累加结果
pl.plot(t,X.cdf(t))
pl.plot(t2,np.add.accumulate(p)*(t2[1]-t2[0]))


