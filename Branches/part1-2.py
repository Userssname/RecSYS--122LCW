#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 17:03:28 2019

@author: kamy-wkm
"""

import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as pgo
from sklearn import cluster
import pandas as pd
from sklearn.decomposition import IncrementalPCA

history = pd.read_csv('user_history.csv')
history.shape
history.describe()


# elbow method
sse = []
list_k = list(range(1, 11))

for k in list_k:
    km = cluster.KMeans(n_clusters=k)
    km.fit(history.drop(['USER ID'], axis=1)) # we need to drop the first column(user id)
    sse.append(km.inertia_)

# Plot sse against k
plt.figure(figsize=(5, 5))
plt.plot(list_k, sse, '-o')
plt.xlabel('Number of clusters')
plt.ylabel('Sum of squared distance')
plt.show()

# According to elbow method, the best k should be 3
kmeans = cluster.KMeans(3) 
kmeans.fit(history.drop(['USER ID'], axis=1))
kmeans_y = kmeans.predict(history.drop(['USER ID'], axis=1))

# Seperate first 3000 users by their labels
# Create three arrays for each cluster/group of users
First_Group = []
Second_Group = []
Third_Group = []

for i in range(3000): 
    if kmeans.labels_[i] == 0:
        First_Group.append(history['USER ID'].iloc[i])
    if kmeans.labels_[i] == 1:
        Second_Group.append(history['USER ID'].iloc[i])
    if kmeans.labels_[i] == 2:
        Third_Group.append(history['USER ID'].iloc[i])
        
First_Group = np.asarray(First_Group)
Second_Group = np.asarray(Second_Group)
Third_Group = np.asarray(Third_Group)

print(Third_Group)