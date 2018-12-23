# -*- coding: utf-8 -*-
"""
Created on Sun Dec 23 19:44:06 2018

@author: Chen
"""
import numpy

def Simrank(a,b,count):
    if a==b :
        return 1
    if count>maxnode:
        return 0
    if (numpy.sum(A[a])==0)or(numpy.sum(A[b])==0):
        return 0
    total = numpy.sum(A[a]) + numpy.sum(A[b])
    ans = 0
    for x in range(maxnode):
        if A[a][x]==0:
            continue
        for y in range(maxnode):
            if A[b][y]==0:
                continue
            ans += Simrank(x,y,count+1)
    return (0.8/total)*ans
    
for i in range(5):
    print('graph'+str(i+1)+':')
    text = open('hw3dataset/graph_'+str(i+1)+'.txt')
    lines = text.readlines()
    a = []
    for line in lines:                  #把txt中存進list
        line=line.strip('\n')           #省略,跟\n
        a.append(line.split(','))
    #print(a)
    maxnode = 0
    for items in a:                     #把每一個str轉成int 把最大的node存起來
        for item in items:
            item = int(item)
            if item > maxnode:
                maxnode = item
    
    A = numpy.zeros((maxnode,maxnode),float)#建立Adjacency matrix
    for items in a:
        A[(int)(items[0])-1][(int)(items[1])-1] = 1
    A = numpy.transpose(A)
    #print(A)
    
    simrank = numpy.zeros((maxnode,maxnode),float)
    for i in range(maxnode):
        for j in range(maxnode):
            simrank[i][j] = Simrank(i,j,0)
    print(simrank)
    text.close()