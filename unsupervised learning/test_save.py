#!/usr/bin/env python 
# -*- coding:utf-8 -*-
#!/usr/bin/env python
# -*- coding:utf-8 -*-
import numpy as np

def Dist2Centers(sample,centers):
    dis2cents = np.sqrt(np.sum(np.power(sample - centers,2)))
    return dis2cents

def s(plabel,data):
    m = len(plabel)

    ai = np.zeros(m)
    bi1 = np.zeros(m)
    bi2 = np.zeros(m)
    g = 0
    for i in range(m):
        #遍历每一个点
        a = 0
        b1 = 0
        b2 = 0
        mark1 = -1
        mark2 = -1
        #mark = np.array([-1]*(k-1))
        for j in range(m):
            #对于每一个点，访问一遍别的点
            if plabel[j]==plabel[i]:
                ai[i]+=Dist2Centers(data[i],data[j])
                a+=1
            else:
                if mark1 ==-1:
                    mark1 = plabel[j]
                    bi1[i]+=Dist2Centers(data[i],data[j])
                    b1+=1
                elif plabel[j]==mark1:
                    bi1[i] += Dist2Centers(data[i],data[j])
                    b1+=1
                elif mark2 ==-1:
                    mark2 = plabel[j]
                    bi2[i] +=Dist2Centers(data[i],data[j])
                    b2+=1
                elif mark2==plabel[j]:
                    bi2[i] += Dist2Centers(data[i],data[j])
                    b2 +=1
        ai[i]/=a
        bi1[i]/=b1
        bi2[i]/=b2
    ans = np.zeros(m)
    for k in range(m):
        b = min(bi1[k],bi2[k])
        ans[k] = (b-ai[k])/max(ai[k],b)
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

