# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 21:15:24 2018

@author: Wenqi Zheng
"""
import authAndQury
import numpy as np
import argparse
import IO
import csv

def append(oriList,addList):
    for i in addList:
        oriList.append(i)
    return oriList
    
def searchWithOffset(maxOffset):
    DEFAULT_TERM = 'pizza'
    DEFAULT_LOCATION = 'Boston'
    DEFAULT_PRICE='1'
    parser = argparse.ArgumentParser()
    parser.add_argument('-q', '--term', dest='term', default=DEFAULT_TERM,type=str, help='Search term (default: %(default)s)')
    parser.add_argument('-l', '--location', dest='location',default=DEFAULT_LOCATION, type=str,help='Search location (default: %(default)s)')
    parser.add_argument('-p', '--price', dest='price',default=DEFAULT_PRICE, type=str,help='Search price (default: %(default)s)')
    parser.add_argument('-o', '--offset', dest='offset', type=int,help='Search offset (default: %(default)s)')    
    location=[]
    ratings=[]
    idList=[]
    priceList=[]
    for i in range(maxOffset):
        input_values = parser.parse_args()
        input_values.offset=i*50
        locationAdd,ratingsAdd,idListAdd,priceListAdd=searchParams(input_values)
        append(location,locationAdd)
        append(ratings,ratingsAdd)
        append(idList,idListAdd)
        append(priceList,priceListAdd)
    return location,ratings,idList,priceList
    
def searchParams(input_values):
    response=authAndQury.searchInputVal(input_values)
    location=[]
    ratings=[]
    businessList=[]
    priceList=[]
    priceParser=['$','$$','$$$','$$$$']
    for i in response['businesses']:
        if('price' not in i):
            continue;
        location.append([i['coordinates']['longitude'],i['coordinates']['latitude']])
        businessList.append(i['id'])
        ratings.append(i['rating'])
        for j in range(4):
            if(i['price']==priceParser[j]):
                priceList.append(j)
    locationArray = np.array(location)
    return locationArray,ratings,businessList,priceList

def searchReviews(idList):
    #writes=[]
    path="../LDA/reviews.csv"
    myFile = open(path, 'w')
    """
    Write data to a CSV file path
    """
    csv_writer = csv.writer(myFile,delimiter=',')
    #print("idList",len(idList))
    with myFile:
        for i in idList:
            reviews= authAndQury.searchReviews(i)["reviews"]
            for j in reviews:
                #print("************",j["text"])
                #writes.append(j["text"])
                    csv_writer.writerow([j["text"]])
    return reviews