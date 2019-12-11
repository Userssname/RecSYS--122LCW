#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 16:56:04 2019

@author: kamy-wkm
"""

import pdb
import csv
import time

#
def getData(collection,key,default):
    if key in collection:
        value = collection[key]
    else:
        value = default
    return value
    
start_time = time.time()
rating_file = "user_ratings.csv"

result = {}
ids = []
headers = []
#read the source file, then store it in mem
with open(rating_file) as csvfile:
    csv_reader = csv.reader(csvfile)  
    rating_header = next(csv_reader)  
    i=0
    for row in csv_reader:  
        i=i+1
        id,name,value = row
        
        if id in result:
            user_data=result[id]
        else:
            user_data={}
            result[id]=user_data
            ids.append(id)
        if name in user_data:
            #in case some error data, warn and debug
            pdb.set_trace()
        else:
            user_data[name]=value
        if not name in headers:
            headers.append(name)

#sort the rows and columns          
ids.sort()
headers.sort()

#print result to csv
with open('user_data.csv', "w", newline='') as f:
    writer = csv.writer(f)
    # write headers
    csv_headers =['USER_ID']
    csv_headers.extend(headers)
    
    writer.writerows([csv_headers])
    i=0
    for id in ids:
        i=i+1
        csv_data = [id]
        user_data = result[id]
        for key in headers:
            csv_data.append(getData(user_data,key,''))
        
        writer.writerows([csv_data])

    f.close()

