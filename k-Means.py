# ####################################
#
#  Josie Evans 
# 
#  Assignment #4: k-means Algorithm
#
# ####################################

import random 
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
    
    ''' Initialize all 3 Clusters '''
    
    # Cluster 1 
    x = range(200)
    clust1 = "CLUSTER ONE = {}"
    print(clust1.format(x))
    
#     for x in range(200): 
#         kMeans = clusterK
        
    # Cluster 2
    y = range(201,400)
    clust2 = "CLUSTER TWO = {}"
    print(clust2.format(y))
    
    # Cluster 3
    z = range(401,600)
    clust3 = "CLUTSTER THREE = {}"
    print(clust3.format(z))
    
    
    ''' Partition the Data into 3 Clusters '''
    
#     for a in dataSet 
    
#         a = txt.rpartition('V400')  # Partition from 400th entry
#         print(a)
    
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