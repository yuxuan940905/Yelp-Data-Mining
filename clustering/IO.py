# -*- coding: utf-8 -*-
"""
Created on Mon Apr 23 19:22:42 2018

@author: admin
"""
import csv
def csv_writer(myData, path,deli):
    myFile = open(path, 'w')
    """
    Write data to a CSV file path
    """
    with myFile:
        csv_writer = csv.writer(myFile,delimiter=',')
        for str in myData: 
           csv_writer.writerow(str)
           
def csv_writer2(myData, path,deli):
    myFile = open(path, 'w')
    """
    Write data to a CSV file path
    """
    with myFile:
        csv_writer = csv.writer(myFile,delimiter=',')
        csv_writer.writerow([myData])
           
def csv_reader(path):
    with open(path,'r') as myFile:
        long=[]
        la=[]
        lines=csv.reader(myFile)  
        for line in lines:
            if (line!=[]):
                long.append(float(line[0]))
                la.append(float(line[1]))
    return long,la