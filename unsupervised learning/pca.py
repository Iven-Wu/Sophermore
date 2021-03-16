#!/usr/bin/env python
# -*- coding:utf-8 -*-
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class DimensionValueError(ValueError):
    """定义异常类"""
    pass


class PCA(object):
    """定义PCA类"""
    def __init__(self, x, n_components=None):
        self.x = x
        self.dimension = x.shape[1]
        if n_components and n_components >= self.dimension:
            raise DimensionValueError("n_components error")
        self.n_components = n_components

    def cov(self):
        """求x的协方差矩阵"""
        x_T = np.transpose(self.x)  # 矩阵转置
        x_cov = np.cov(x_T)  # 协方差矩阵
        return x_cov

    def get_feature(self):
        """求协方差矩阵C的特征值和特征向量"""
        x_cov = self.cov()
        a, b = np.linalg.eig(x_cov)
        #下面写的其实就是len
        m = a.shape[0]
        c = np.hstack((a.reshape((m, 1)), b))
        c_sort = c[np.argsort(-c[:,0])]
        return c_sort

    def explained_varience_(self):
        c_sort = self.get_feature()
        return c_sort[:, 0]

    def reduce_dimension(self,threshold):
        """指定维度降维和根据方差贡献率自动降维"""
        c_sort = self.get_feature()
        varience = self.explained_varience_()
        if self.n_components:  # 指定降维维度
            p = c_sort[0:self.n_components, 1:]#取前几个特征值
            y = np.dot(p, np.transpose(self.x))
            return np.transpose(y)
        varience_sum = sum(varience)
        varience_radio = varience / varience_sum

        varience_contribution = 0
        for i in range(self.dimension):
            varience_contribution += varience_radio[i]
            if varience_contribution >= threshold:
                break
        p = c_sort[0:i + 1, 1:]  # 取前i个特征向量
        y = np.dot(p, np.transpose(self.x))
        return np.transpose(y)

def p(data,threshold):
    pca = PCA(data)
    label = pca.reduce_dimension(threshold)
    return label


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
    pca = PCA(data)
    threshold = 0.6
    label = pca.reduce_dimension(threshold)
    #print(label)
    print(type(label))
    print(np.shape(label))
