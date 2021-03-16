#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pca


def initCenters(dataSet , k):
    numSamples , dim = dataSet.shape
    centers = np.zeros((k,dim))
    for i in range(k):
        index = int (np.random.uniform(0,numSamples))
        centers[i, :] = dataSet[index,  :]
    #print(centers)
    return centers

def Dist2Centers(sample,centers):
    k= centers.shape[0]
    dis2cents = np.zeros(k)
    for i in range(k):
        dis2cents[i] = np.sqrt(np.sum(np.power(sample - centers[i,:],2)))
    return dis2cents

#def kmeans(dataSet , k, iterNum):
def kmeans(dataSet, k):
    numSamples = dataSet.shape[0]
    iterCount = 0

    clusterAssignment = np.zeros(numSamples)
    clusterChanged = True
    centers= initCenters(dataSet,k)
    #i = 0
    while clusterChanged:
        #i+=1
        clusterChanged = False
        #iterCount = iterCount+1
        for i in range(numSamples):

            dis2cent =  Dist2Centers(dataSet[i,:],centers)
            minIndex = np.argmin(dis2cent)

            if clusterAssignment[i] != minIndex:
                clusterChanged = True
                clusterAssignment[i] = minIndex

        for j in range(k):
            pointsInCluster = dataSet[np.nonzero(clusterAssignment[:]== j )[0]]
            centers[j,:] = np.mean(pointsInCluster,axis = 0)
    #print('at all',i,'times')
    return centers, clusterAssignment

def km(data,k):
    #print(" clustering")
    dataSet = np.mat(data)

    #centers_result, clusterAssignment_result = kmeans(dataSet , k ,1000)
    centers_result, clusterAssignment_result = kmeans(dataSet, k)
    #print("showing the result")
    #showCluster(dataSet , k , centers_result,clusterAssignment_result)
    np.set_printoptions(precision=3, suppress=True)
    ans = np.array([int(x) for x in clusterAssignment_result])
    #ans=np.transpose([ans])
    #c = np.hstack((ans,data))
    return ans

'''
def showCluster(dataSet, k , centers, clusterAssignment):
    numSamples, dim = dataSet.shape
    mark = ['or','ob','og']

    for i in range(numSamples):
        markIndex = int(clusterAssignment[i])
        plt.plot(dataSet[i,0],dataSet[i,1],mark[markIndex])

    mark = ['Dr','Db','Dg']
    for i in range(k):
        plt.plot(centers[i,0], centers[i,1],mark[i],markersize = 17)
    plt.show()
'''

if __name__ =='__main__':
    def preprocess(filename):
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
        for j in range(len(data[0])):
            ave = np.mean(data[:,j],axis=0)
            stand = np.std(data[:,j])
            for i in range(len(data)):
                data[i,j] = (data[i,j]-ave)/stand
        return data,label
    data,label=preprocess('wine.data')
    threshold = 0.5
    predict = pca.p(data, threshold)
    km(data,3)