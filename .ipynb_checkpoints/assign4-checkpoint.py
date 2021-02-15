# ####################################
#
# Josie Evans 
# 
# Assignment #4: k-means Algorithm
#
# ####################################

#print("k-means Algorithm")

x, y, z = 'Cluster1', 'Cluster2', 'Cluster3'

# print(x)
# print(y)
# print(z)

# import random 
# x = random.randrange(0, 200)

def kMeansAlg():
    
    ''' (1) Initialize all 3 Clusters at random '''
    
    # Cluster 1 
    x = range(200)
    clust1 = "CLUSTER ONE = {}"
    print(clust1.format(x))
        
    # Cluster 2
    y = range(201,400)
    clust2 = "CLUSTER TWO = {}"
    print(clust2.format(y))
    
    # Cluster 3
    z = range(401,600)
    clust3 = "CLUTSTER THREE = {}"
    print(clust3.format(z))
    
    
    ''' (2) Partition the Data into 3 Clusters '''
    
#     for a in dataSet 
    
#         a = txt.rpartition('V400')  # Partition from 400th entry
#         print(a)
    
kMeansAlg()