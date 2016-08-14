# -*- coding: utf-8 -*-
"""
Created on Sun Aug 14 14:39:43 2016

@author: WangHaiTao
"""
import scipy.weave as weave 
import numpy as np
import time

def my_sum(a):
    n=int(len(a))
    code="""
    int i;
    double counter;
    counter=0;
    for(i=0;i<n;++i){
    counter=counter+a(i);    
    }
    return_val=counter;
    """
    err=weave.inline(
    code,
    ['a','n'],
    type_converters=weave.converters.blitz,
    compiler="gcc"    
    )
    return err
a=np.arange(0,10000000,1.0)
#下面调用一次my_sum，weave会自动对C语言进行编译之后的代码
my_sum(a)

start=time.clock()
for i in xrange(100):
    my_sum(a)#直接运行编译之后的代码
print"my_sum:",(time.clock()-start)/100.0

start=time.clock()
for i in xrange(100):
    np.sum(a)#numpy中的sum，其实现也是C语言级别
print"my_sum:",(time.clock()-start)/100.0

start=time.clock()
sum(a)#python内置的sum，速度较慢
print"my_sum:",time.clock()-start