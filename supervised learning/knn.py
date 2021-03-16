#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import numpy as np
import operator
from sklearn.preprocessing import LabelEncoder
import pandas as pd
import random

def classify(input,train,k):
    label = train[:,-1]
    data = train[:,:-1]
    #计算欧式距离
    diff = np.tile(input,(len(data),1)) - data
    #print(diff)
    sqdiff = diff ** 2
    squareDist = np.sum(sqdiff, axis=1)  ###行向量分别相加，从而得到新的一个行向量
    dist = squareDist ** 0.5
    sortedDistIndex = np.argsort(dist)
    count = {}
    for i in range(k):
        voteLabel = label[sortedDistIndex[i]]
        count[voteLabel] = count.get(voteLabel,0) + 1
    #print(count)
    maxCount = 0
    for key, value in count.items():
        if value > maxCount:
            maxCount = value
            classes = key
    return classes

def findk(train,test):
    kset = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    testlabel = test[:,-1]
    test = test[:,:-1]
    #label = train[:,-1]
    data = train
    f1 = 0
    for k in kset:
        #print('第',k,'次')
        TP = 0
        FP = 0
        FN = 0
        TN = 0
        for i in range(len(test)):
            cla = classify(test[i],data,k)
            if cla==1:
                if testlabel[i] ==1:
                    TP+=1
                else:
                    FP+=1
            elif cla==-1:
                if testlabel[i] ==1:
                    FN+=1
                else:
                    TN+=1
        P = TP/(TP+FP)
        R = TP/(TP+FN)
        F1 = 2*P*R/(P+R)
        #print('F1=',F1)
        if F1>f1:
            f1 = F1
            endk = k
    return endk

def knn(train,test,g=True):
    if g==False:
        train = np.delete(train, -2, axis=1)
        train = np.delete(train, -2, axis=1)
        test = np.delete(test,-2,axis=1)
        test = np.delete(test, -2, axis=1)
    k = findk(train,test)
    anslabel = []
    for i in range(len(test)):
        anslabel.append(classify(test[i,:-1],train,4))
    return anslabel


if __name__ =='__main__':
    def load_data(file_path):
        df = pd.read_csv(file_path, sep=';')
        col = []
        df = preprocess(df)
        dataset = df.values
        dataset = dataset.astype(float)
        random.shuffle(dataset)
        for i in range(len(dataset)):
            dataset[i, -1] = 1 if dataset[i, -1] >= 10 else -1
        trainsize = len(dataset) * 7 // 10
        train = dataset[:trainsize]
        test = dataset[trainsize:]
        return train,test
    def preprocess(df):
        col = []
        for i in range(df.shape[1]):
            if df.dtypes[i] == 'object':
                col.append(df.columns[i])
        if col is not None:
            for c in col:
                df[c] = LabelEncoder().fit_transform(df[c])
        return df

    train,test = load_data('student-mat.csv')
    print(np.shape(test))
    #数据归一化处理
    '''
    for j in range(len(dataset[0])):
        for i in range(len(dataset)):
            dataset[i,j] = (dataset[i,j] - min(dataset[:,j]))/(max(dataset[:,j])-min(dataset[:,j]))
    '''

    endk = findk(train,test)
    print('最优的k等于=',endk)
    ans =knn(train,test)
    print(ans)
    #k = 5
    #classify(test[0],train,label,k)