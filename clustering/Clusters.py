# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 21:02:03 2018

@author: Wenqi Zheng
"""
from numpy import *
import numpy as np  
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

#normalize the data
def normData(dataset):
    dataset=np.array(dataset)
    mean=dataset.mean()
    std=dataset.std()
    dataset=(dataset-mean)/std
    return dataset

def showCluster2(dataSet, k, clusterAssment,attachLables,path):
    dataSet=np.array(dataSet)
    labelsSet=['1','2','3','4','5']
    colors=['red','blue','green','yellow','black']
    # draw all samples
    for i in range(len(dataSet)):
        #markIndex = int(clusterAssment[i]) 
        plt.plot(dataSet[i, 0], dataSet[i, 1], color=colors[clusterAssment[i]], marker='o')
    patches=[]
    # draw the centroids
    for i in range(k):
        patches.append ( mpatches.Patch(color=colors[i], label=labelsSet[attachLables[i]]))
    plt.title('GMM clustering result for\npizza in Boston')
    plt.xlabel('longitude') # latitude
    plt.ylabel('latitude')
    plt.legend(handles=patches)
    plt.savefig(path, bbox_inches='tight')
    plt.show()  
    
def showCluster(dataSet, k, centroids, clusterAssment,attachLables,path):
    dataSet=np.array(dataSet)
    labelsSet=['1','2','3','4','5']
    colors=['red','blue','green','yellow','black']
    # draw all samples
    for i in range(len(dataSet)):
        #markIndex = int(clusterAssment[i]) 
        plt.plot(dataSet[i, 0], dataSet[i, 1], color=colors[clusterAssment[i]], marker='o')
    patches=[]
    # draw the centroids
    for i in range(k):
        plt.plot(centroids[i, 0], centroids[i, 1], marker='D', color=colors[i], markersize = 12)
        patches.append ( mpatches.Patch(color=colors[i], label=labelsSet[attachLables[i]]))
    plt.title('K-Means clustering result for\npizza in Boston')
    plt.xlabel('longitude') # latitude
    plt.ylabel('latitude')
    plt.legend(handles=patches)
    plt.savefig(path, bbox_inches='tight')
    plt.show()    
    
    
def attachLables(ratings,clusterAss,k):
    #print(ratings)
    attachLables=[]
    sumCluster=[0]*k
    avgCluster=[0]*k
    countCluster=[0]*k
    hashIndex={}
    #print(ratings)
    for i in range(len(ratings)):
        t=int(ratings[i])
        sumCluster[clusterAss[i]]+=t
        countCluster[clusterAss[i]]+=1
    for i in range(k):
        avgCluster[i]=sumCluster[i]/countCluster[i]
        hashIndex[avgCluster[i]]=i
    #print(hashIndex)
    print("avg: ",avgCluster)
    avgCluster=sort(avgCluster)
    print("avg: ",avgCluster)
    for i in range(k):
        attachLables.append(hashIndex[avgCluster[i]])
    print(avgCluster)
    print(attachLables)
    return attachLables