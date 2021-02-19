# ####################################
#
#  Josie Evans 
# 
#  Assignment #4: k-means Algorithm
#
# ####################################

import random 
# import numpy as np
import matplotlib.pyplot as plot

# (I). Get Vectors in Data Set 
def GetVectors(data):
    
    # Import & Read Data Set 
    #dataSet = r'data.csv'
    
    vectorsK = {} 
    clusterCenters = {}
    
    with open(data, 'r') as d: 
    
        contents = d.read().split('\n')
        
        # Define Vectors 
        contents = contents[1:len(contents)] 
        
        for vect_ID, vect_nums in enumerate(contents):
        
            if vect_nums == '':
                break
        
            curr_vect = vect_nums.split(',')
            
            vectorsK[curr_vect[0]] = [float(val) for val in curr_vect[1:len(curr_vect)]]
            
            '''for val in curr_vect[1:len(curr_vect)]:
                
                val = float(val)'''
                
        # Define Cluster Centers 
        contents = contents[vect_ID + 2, len(contents)]
        
        for vect_num in contents: 
            
            curr_vect = vect_num.split(',')
            
            clusterCenters[curr_vect[0]] = [float(val) for val in curr_vect[1:len(curr_vect)]]
            
        #print(clusterCenters)
        
    return vectorsK, clusterCenters

clusterCenters, vectorsK = GetVectors('data.csv')

print(clusterCenters)

####################################

# (II). Assign k Clusters 
def kClusters(k, clusterCenters, vectorsK):
    
    keys = list(vectorsK.keys())
    
    ''' Initialize all 3 Clusters '''
    
    # Cluster 1 
    clust_k1 = random.randrange(0, len(vectorsK))
    clust1 = "CLUSTER ONE = {}"
    print(clust1.format(clust_k1))
    clust1 = keys[0:clust_k1]

        
    # Cluster 2
    clust_k2 = random.randrange(clust_k1, len(vectorsK))
    clust2 = "CLUSTER TWO = {}"
    print(clust2.format(clust_k2))
    clust2 = keys[clust_k1:clust_k2]
    

    # Cluster 3
    clust_k3 = random.randrange(clust_k2, len(vectorsK))
    clust3 = "CLUTSTER THREE = {}"
    print(clust3.format(clust_k3))
    clust3 = keys[clust_k2:len(keys)]
    
    return kClusters(k, clusterCenters, vectorsK)
    
kClusters()

####################################

# (III). Plot Initial k Clusters 
'''INITIAL clusterCenters in BLUE'''
def plotK(dataSet, clusterCenters): 
    
    plot.plot(range(1,600), dataSet)
    plot.title('k-Means Algorithm')
    plot.xlabel('Clusters')
    plot.ylabel('Value')
    plot.show()

####################################

# (IV). Compute the Distance b/w Centroids & Points
def findDistance():
    # sqrt of sum of squares 
    from math import sqrt
    nums = {int(sqrt((vectorsK)**2)) for vectorsK in range(200)}
    print(nums)
    


####################################

# (V). Locate new Cluster Center / Centroid 
def updateCenter():
    # compute AVG of clust & update 
    
'''while (prev_val - current <=0)''' 
# until unchanged 

# --> Prev Value of Jclust <= 1
# Summation for each cluster within value 


####################################

# (). Plot Final j Clusters 
'''FINAL clusterCenters in GREEN'''
def plotJ(dataSet, clusterCenters): 
    
    plot.plot(range(1,600), dataSet)
    plot.title('k-Means Algorithm')
    plot.xlabel('Clusters')
    plot.ylabel('Value')
    plot.show()