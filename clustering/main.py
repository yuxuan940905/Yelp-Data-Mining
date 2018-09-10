# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 21:04:22 2018

@author: Wenqi Zheng
"""
import sklearn
import search
from numpy import *
import numpy as np
import Clusters
import IO
import mapAPI
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
#from sklearn import metrics
from sklearn import mixture

GOOGLE_API_KEY='AIzaSyAGYh9__XDQTdmyP6mezjbP3Yz8NtVUmqs'

def main():
    
    Location=[]
    Location,ratings,idList,priceList=search.searchWithOffset(20)
    kmeans = KMeans(n_clusters=5, random_state=0).fit(Location)
    maxLables=Clusters.attachLables(ratings,kmeans.labels_,5)
    Clusters.showCluster(Location,5, kmeans.cluster_centers_, kmeans.labels_,maxLables,"kmeans_on_ratings.pdf")
    Location=np.array(Location)
    #print("Silhouette Score:",metrics.silhouette_score(Location, kmeans.labels_,metric='euclidean'))
    
    gmm = mixture.GMM(n_components=5,covariance_type='full')
    gmm.fit(Location)
    gaussian = gmm.predict(Location)
    maxLables=Clusters.attachLables(ratings,gaussian,5)
    Clusters.showCluster2(Location,5, gaussian,maxLables,"gmm_on_ratings.pdf")
    Location=np.array(Location)
    #print("Silhouette Score:",metrics.silhouette_score(Location, gaussian,metric='euclidean'))
    
    kmeans = KMeans(n_clusters=4, random_state=0).fit(Location)
    maxLables=Clusters.attachLables(priceList,kmeans.labels_,4)
    Clusters.showCluster(Location,4, kmeans.cluster_centers_, kmeans.labels_,maxLables,"kmeans_on_price.pdf")
    Location=np.array(Location)
    #print("Silhouette Score:",metrics.silhouette_score(Location, kmeans.labels_,metric='euclidean'))
    
    gmm = mixture.GMM(n_components=4,covariance_type='full')
    gmm.fit(Location)
    gaussian = gmm.predict(Location)
    maxLables=Clusters.attachLables(priceList,gaussian,4)
    Clusters.showCluster2(Location,4, gaussian,maxLables,"gmm_on_price.pdf")
    Location=np.array(Location)
    #print("Silhouette Score:",metrics.silhouette_score(Location, gaussian,metric='euclidean'))

    path = "location.csv"
    IO.csv_writer(Location, path,',')
    
    long,la=IO.csv_reader(path)
    mapAPI.mapOut(GOOGLE_API_KEY,long,la)
    
    search.searchReviews(idList)
    
if __name__ == '__main__':
    main()
