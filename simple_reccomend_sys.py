# -*- coding: utf-8 -*-
"""
Created on Wed Aug 17 10:43:31 2016

@author: WangHaiTao
"""
import numpy as np
import pandas as pd

header=['user_id','item_id','rating','timestamp']
df=pd.read_csv('E:\pythonSci\ml-100k\u.data',sep='\t',names=header)

n_users=df.user_id.unique().shape[0]
n_items=df.item_id.unique().shape[0]
print'Num of users='+str(n_users)+'| Num of movies='+str(n_items)

from sklearn import cross_validation as cv

train_data,test_data=cv.train_test_split(df,test_size=0.25)
#创建用户-产品矩阵
train_data_matrix=np.zeros((n_users,n_items))
for line in train_data.itertuples():
    train_data_matrix[line[1]-1,line[2]-1]=line[3]

test_data_matrix=np.zeros((n_users,n_items))
for line in test_data.itertuples():
    test_data_matrix[line[1]-1,line[2]-1]=line[3]
    
from sklearn.metrics.pairwise import pairwise_distances
user_similarity=pairwise_distances(train_data_matrix,metric='cosine')
item_similarity=pairwise_distances(train_data_matrix.T,metric='cosine')

def predict(ratings,similarity,type='user'):
    if type=='user':
        mean_user_rating=ratings.mean(axis=1)
        ratings_diff = (ratings - mean_user_rating[:, np.newaxis])
        pred = mean_user_rating[:, np.newaxis] + similarity.dot(ratings_diff) / np.array([np.abs(similarity).sum(axis=1)]).T
    elif type=='item':
        pred=ratings.dot(similarity) / np.array([np.abs(similarity).sum(axis=1)])
        return pred

item_prediction = predict(train_data_matrix, item_similarity, type='item')
user_prediction = predict(train_data_matrix, user_similarity, type='user')
from sklearn.metrics import mean_squared_error
from math import sqrt
def rmse(prediction, ground_truth):
    prediction = prediction[ground_truth.nonzero()].flatten()
    ground_truth = ground_truth[ground_truth.nonzero()].flatten()
    return sqrt(mean_squared_error(prediction, ground_truth))
#print 'User-based CF RMSE: ' + str(rmse(user_prediction, test_data_matrix))
print 'Item-based CF RMSE: ' + str(rmse(item_prediction, test_data_matrix))
        