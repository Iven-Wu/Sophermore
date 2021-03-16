#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
import random
import knn
import svm
import logistc

def load_data(file_path):
    df = pd.read_csv(file_path,sep=';')
    df = preprocess(df)
    dataset = df.values
    dataset = dataset.astype(float)
    random.shuffle(dataset)
    for i in range(len(dataset)):
        dataset[i][-1] = 1 if dataset[i][-1] >= 10 else -1
    trainsize = len(dataset) * 7 // 10

    train = dataset[:trainsize]
    test = dataset[trainsize:]
    return train,test

def load_data1(file_path):
    df = pd.read_csv(file_path,sep=';')
    col = []
    df = preprocess(df)
    dataset = df.values
    random.shuffle(dataset)
    for i in range(len(dataset)):
        dataset[i][-1] = 1 if dataset[i][-1] >= 10 else -1
    trainsize = len(dataset) * 7 // 10

    #归一化，对于逻辑回归需要，否则会溢出

    for j in range(len(dataset[0])):
        for i in range(len(dataset)):
            dataset[i, j] = (dataset[i, j] - min(dataset[:, j])) / (max(dataset[:, j]) - min(dataset[:, j]))

    train = dataset[:trainsize]
    test = dataset[trainsize:]
    return train,test

def preprocess(df):
    col = []
    for i in range(df.shape[1]):
        if df.dtypes[i] =='object':
            col.append(df.columns[i])
    if col is not None:
        for c in col:
            df[c] = LabelEncoder().fit_transform(df[c])
    return df

def calcu(plabel,olabel):   #plabel指预测的，olabel指原来的
    TP = 0
    FP = 0
    FN = 0
    TN = 0
    for i in range(len(plabel)):
        if olabel[i]==1:
            if plabel[i]==1:
                TP +=1
            else:
                FN+=1
        else:
            if plabel[i] ==1:
                FP +=1
            else:
                TN+=1
    P = TP / (TP + FP)
    R = TP / (TP + FN)
    F1 = 2 * P * R / (P + R)
    return F1

if __name__ == '__main__':
    #这里需要手动写入要输入的数据
    train,test = load_data('student-mat.csv')
    knnlabel1 = knn.knn(train,test)
    knnlabel2 = knn.knn(train,test,g=False)
    print('KNN with g1g2 ,F1=',calcu(knnlabel1,test[:,-1]))
    print('KNN without g1g2,F1 = ',calcu(knnlabel2,test[:,-1]))

    b1,alpha1,w1 = svm.svmtrain(train, 0.6, 2,'rbf')
    svmlabel1 = svm.svmpredict(train,test[:, :-1], w1, b1, alpha1, 2,'rbf')

    b2,alpha2,w2 = svm.svmtrain(train,0.6,2,'rbf',g1g2=False)
    svmlabel2 = svm.svmpredict(train,test[:,:-1], w2, b2, alpha2, 2,'rbf',g1g2=False)

    print('gaussian kernel with g1g2 svm,F1 = ',calcu(svmlabel1,test[:,-1]))
    print('gaussian kernel without g1g2 svm,F1 = ', calcu(svmlabel2, test[:, -1]))

    train1,test1 = load_data('student-mat.csv')
    loglabel = logistc.log(train1,test1)
    print('log,F1=', calcu(loglabel, test1[:, -1]))
