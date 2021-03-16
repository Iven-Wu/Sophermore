#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import numpy as np
import pandas as pd
import pca
import kmeans
import test
import test_save

def preprocess(odata):
    data = odata.copy()
    for j in range(len(data[0])):
        ave = np.mean(data[:,j],axis=0)
        stand = np.std(data[:,j])
        for i in range(len(data)):
            data[i,j] = (data[i,j]-ave)/stand
    return data


def load_data(filename):
    label = []
    data = []
    fp = open(filename)
    for line in fp.readlines():
        lineArr = line.strip().split(',')
        for i in range(len(lineArr)):
            lineArr[i] = float(lineArr[i])
        label.append(lineArr[0])
        data.append(lineArr[1:])
    data = np.array(data)
    label = np.array(label)
    return data,label

if __name__ =='__main__':
    odata,label=load_data('wine.data')
    data = preprocess(odata)
    threshold = 0.8
    predict=pca.p(data,threshold)   #predict 是经过了处理的数据


    ks = [2,3,4,5,6,7]
    ss = -2
    k = -1
    Ri1 ={}
    #S = {}
    for i in range(len(ks)):
        klabel = kmeans.km(predict,ks[i])   #计算出来的分类结果
        Si = test.s(klabel, data,ks[i])
        Ri1[ks[i]] = test.ri(klabel,label)
        #S[ks[i]] = Si
        if Si>ss:
            ss = Si
            k = ks[i]
            kans = klabel
    print('after pca,this is best si=',ss)
    print('after pca,this is the best k=',k)
    print('after pca,thsi is Ri',Ri1)
    c = np.hstack((np.transpose([kans]), odata))
    np.savetxt('after_pca_ans.csv', c, delimiter=',', fmt='%.03f')
    #print(S)

    kt = [2,3,4,5,6,7]
    ss = -2
    k = -1
    Ri2={}
    S={}
    for i in range(len(kt)):
        olabel = kmeans.km(data, kt[i])
        Si = test.s(olabel, data, kt[i])
        Ri2[kt[i]] = test.ri(olabel, label)
        S[kt[i]] = Si
        if Si > ss:
            ss = Si
            k = kt[i]
            oans = olabel
    print('before pca,this is best si=', ss)
    print('before pca,this is the best k=', k)
    print('before pca,thsi is Ri', Ri2)
    d = np.hstack((np.transpose([oans]), odata))
    np.savetxt('before_pca_ans.csv', d, delimiter=',', fmt='%.03f')
    print(S)
    #olabel = kmeans.km(data,3)
    #c=np.hstack((np.transpose([klabel]),odata))
    #np.savetxt('classans.csv', c, delimiter=',', fmt='%.03f')
    comri = test.ri(klabel,olabel)
    print('compared ri=',comri)
    #ri = test.ri(klabel,label)
    #print(ri)





