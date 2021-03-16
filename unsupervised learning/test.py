#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import numpy as np

def Dist2Centers(sample,centers):
    dis2cents = np.sqrt(np.sum(np.power(sample - centers,2)))
    return dis2cents

def s(plabel,data,k):
    m = len(plabel)

    ai = np.zeros(m)
    bi = np.array([np.zeros(m)]*(k-1))
    g = 0
    for i in range(m):
        #遍历每一个点
        a = 0
        b = np.zeros(k-1)
        mark = np.array([-1]*(k-1))
        for j in range(m):
            #对于每一个点，访问一遍别的点
            if plabel[j]==plabel[i]:
                ai[i]+=Dist2Centers(data[i],data[j])
                a+=1
            else:
                for x in range(k-1):
                    if mark[x]==-1:
                        mark[x] = plabel[j]
                        bi[x][i] +=Dist2Centers(data[i],data[j])
                        b[x]+=1
                        break
                    elif plabel[j] ==mark[x]:
                        bi[x][i] +=Dist2Centers(data[i],data[j])
                        b[x]+=1
                        break
        ai[i]/=a
        for x in range(k-1):
            bi[x][i]/=b[x]
    ans = np.zeros(m)
    for h in range(m):
        b = min(bi[x][h] for x in range(k-1))
        ans[h] = (b-ai[h])/max(ai[h],b)
    si = np.mean(ans)
    return si

def ri(plabel,olabel):
    a = 0
    b = 0
    c = 0
    d = 0
    m = len(plabel)
    for i in range(m):
        for j in range(i+1,m):
            if plabel[i]==plabel[j] and olabel[i]==olabel[j]:
                a+=1
            elif olabel[i] == olabel[j] and plabel[i]!=plabel[j]:
                b+=1
            elif olabel[i]!=olabel[j] and plabel[i]==plabel[j]:
                c+=1
            elif olabel[i]!=olabel[j] and plabel[i]!=plabel[j]:
                d+=1
    ri = (a+d)/(a+b+c+d)
    return ri

