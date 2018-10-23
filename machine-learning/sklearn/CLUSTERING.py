#CELL 0 
import numpy as np
import pandas as pd
import sklearn
import matplotlib.pyplot as plt
import seaborn as sns

#CELL 1 
#Pure Data
from sklearn.datasets import make_blobs
X, y = make_blobs(n_samples=500, centers=4, random_state=1)
plt.scatter(X[:,0], X[:,1])

#CELL 2 
#k-means
from sklearn.cluster import KMeans
model = KMeans(n_clusters=3)
model.fit(X)
y = model.fit_predict(X)
plt.scatter(X[:,0], X[:,1], c=y)

#CELL 3 
#Agglomerative Clustering
from sklearn.cluster import AgglomerativeClustering
model = AgglomerativeClustering(n_clusters=3)
y = model.fit_predict(X)
plt.scatter(X[:,0], X[:,1], c=y)

#CELL 4 
#Density-based spatial clustering of applications with noise 
from sklearn.cluster import DBSCAN
model = DBSCAN()
model.fit(X)
y = model.fit_predict(X)
plt.scatter(X[:,0], X[:,1], c=y)
