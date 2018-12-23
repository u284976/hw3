# -*- coding: utf-8 -*-
"""
Created on Fri Dec 21 17:34:33 2018

@author: Chen
"""
import numpy
for i in range(6):
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
    
    A = numpy.zeros((maxnode,maxnode),int)#建立Adjacency matrix
    for items in a:
        A[(int)(items[0])-1][(int)(items[1])-1] = 1
    #print(A)
    
    At = numpy.transpose(A)
    #print(At)
    temp = numpy.ones((maxnode,1),float)
    hub = numpy.zeros((maxnode,1),float)
    auth = numpy.zeros((maxnode,1),float)
    dev = 0.001
    
    auth = numpy.matmul(At,temp)            #先做第一遍
    hub = numpy.matmul(A,auth)
    auth = auth/[numpy.sum(auth)]           #normalization
    hub = hub/[numpy.sum(hub)]
    
    while True:
        temp_auth = numpy.matmul(At,hub)
        temp_hub = numpy.matmul(A,auth)
        temp_auth = temp_auth/[numpy.sum(temp_auth)]
        temp_hub = temp_hub/[numpy.sum(temp_hub)]
        temp_dev = auth - temp_auth + hub - temp_hub
        temp_dev = numpy.abs(temp_dev)
        if numpy.sum(temp_dev) < dev:
            break;
        else:
            auth = temp_auth
            hub = temp_hub
    
    print('auth: ')
    print(temp_auth)
    print('\n','hub:')
    print(temp_hub)
    
    text.close()