# -*- coding: utf-8 -*-
"""
Created on Sat Dec 22 20:03:09 2018

@author: Chen
"""

import numpy
for i in range(3):
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
    #print(A)
    for i in range(maxnode):
        if numpy.sum(A[i] == 0):
            continue
        A[i] = A[i] / [numpy.sum(A[i])]
    #print(A)
    A = numpy.transpose(A)
    
    PR = numpy.ones((maxnode,1),float)  #PageRank 初始矩陣 總合為1
    PR = PR / [numpy.sum(PR)]
    
    
    df = 0.15
    dev = 0.00001
    while True:
        temp_PR = numpy.matmul(A,PR)
        temp_PR = temp_PR*(1-df) + df/maxnode
        temp_PR = temp_PR / [numpy.sum(temp_PR)]
        
        temp_dev = temp_PR - PR
        temp_dev = numpy.abs(temp_dev)
        if numpy.sum(temp_dev) < dev :
            break
        else:
            PR = temp_PR
    print(temp_PR)
    text.close()
    
    