# ####################################
#
#  Josie Evans 
# 
#  Assignment #4: k-means Algorithm
#
# ####################################

import random 
import numpy as np
import matplotlib.pyplot as plot

# (I). Get Vectors in Data Set 
def GetVectors(path):
    
    vectorsK = {} 
    clusterCenters = {}
    
    with open(path, 'r') as f:
        
        contents = f.read().split('\n')
        
        # Split Contents of Data Set 
        contents = [row for row in contents if not row.split(',')[0].strip() in ['Vectors', 'Cluster Centers', '']]
        
        for line in contents:    
            
            curr_line = line.split(',')
            
            # Vectors 
            if curr_line[0].startswith('V'):
                
                vectorsK[curr_line[0]] = [float(val) for val in curr_line[1:len(curr_line)]]
             
            # Cluster Centers
            else:
                clusterCenters[curr_line[0]] = [float(val) for val in curr_line[1:len(curr_line)]]
                
    return clusterCenters, vectorsK
    
#     counter = 1
    
#     with open(data, 'r') as d: 
    
#         contents = d.read().split('\n')
        
#         for columns in contents:
            
#              # Vectors 
#             if counter <= 601:
            
#                 vect = columns.split(',')

#                 vectorsK[vect[0]] = [vect[1],vect[2],vect[3]]  #Each val(1-3) to Key 
            
#             # Cluster Centers 
#             elif counter > 602:
                
#                 clusters = columns.split(',')
                
#                 clusterCenters[clusters[0]] = [clusters[1], clusters[2], clusters[3]]
                
#             elif counter > 606: 
#                 break
                
#         counter = counter + 1

#     print(vectorsK)
        
#     print(clusterCenters)
        
#         # Define Vectors 
#         contents = contents[1:len(contents)] 
        
#         for vect_ID, vect_nums in enumerate(contents):
        
#             if vect_nums == '':
#                 break
        
#             curr_vect = vect_nums.split(',')
            
# #             vectorsK[curr_vect[0]] = [float(val) for val in curr_vect[1:len(curr_vect)]]
            
#             for val in curr_vect[1:len(curr_vect)]:
                
#                 val = float(val)
                
#         # Define Cluster Centers 
#         contents = contents[vect_ID + 2, len(contents)]
        
#         for vect_num in contents: 
            
#             curr_vect = vect_num.split(',')
            
#             clusterCenters[curr_vect[0]] = [float(val) for val in curr_vect[1:len(curr_vect)]]
            
#         #print(clusterCenters)
        
    return vectorsK, clusterCenters

clusterCenters, vectorsK = GetVectors('data.csv')

# print(clusterCenters)

####################################

# (II). Assign k Clusters 
def kClusters(k, clusterCenters, vectorsK):
    
    keys = list(vectorsK.keys())
    
    ''' Initialize all 3 Clusters '''
    
    
# Randomly sample so each cluster does not have repeating values 

# Set / Set difference 

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
    plot.zlabel('Height')
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