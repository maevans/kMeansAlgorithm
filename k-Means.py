# ####################################
#
#  Josie Evans 
#  Assignment #4: k-means Algorithm
#
# ####################################

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import random

# (I). Get Vectors in Data Set 
def GetVectors(path):
    
    vectors = {}
    cluster_centers = {}
    
    with open(path, 'r') as f:
        contents = f.read().split('\n')
        contents = [row for row in contents if not row.split(',')[0].strip() in ['Vectors', 'Cluster Centers', '']]
        for line in contents:    
            curr_line = line.split(',')
            if curr_line[0].startswith('V'):
                vectors[curr_line[0]] = np.array([float(val) for val in curr_line[1:len(curr_line)]])
            else:
                cluster_centers[curr_line[0]] = np.array([float(val) for val in curr_line[1:len(curr_line)]])
    return cluster_centers, vectors

####################################

# (II). Plot 3 Clusters 
'''INITIAL clusterCenters in BLUE'''
'''FINAL clusterCenters in GREEN'''
def plot_vectors(cluster_centers, vectors, num_vectors):
    
    fig = plt.figure()
    ax = Axes3D(fig)
    
    # Plot vectors:
    vector_names = list(vectors.keys())
    rand_indices = random.sample(range(0, len(vectors)), num_vectors)
    selected_vectors = [vector_names[idx] for idx in rand_indices]
    target_vectors = tuple([vectors[nm] for nm in selected_vectors])
    target_vectors = np.column_stack(target_vectors)
    
    # Set coordinate limits:
    ax.set_xlim([-20,20])
    ax.set_ylim([-20,20])
    ax.set_zlim([-20,20])
    ax.scatter(target_vectors[:, 0], target_vectors[:, 1], target_vectors[:, 2], color = 'black')
    
    # Plot clusters:
    clusters = np.column_stack([cluster_centers[nm] for nm in cluster_centers])
    ax.scatter(clusters[:,0], clusters[:,1], clusters[:,2], color = 'blue')
    plt.show()

def plot_clusters(clusters_initial, clusters_final, vectors = None):
    fig = plt.figure()
    ax = Axes3D(fig)
    clusters_initial = np.column_stack([clusters_initial[nm] for nm in clusters_initial])
    clusters_final = np.column_stack([clusters_final[nm] for nm in clusters_final])
    ax.scatter(*clusters_initial, color = 'blue')
    ax.scatter(*clusters_final, color = 'green')
    if not vectors is None:
        vectors_arr = np.column_stack([vectors[nm] for nm in vectors])
        ax.scatter(*vectors_arr, color = 'red')
    plt.show()
    

def kMeansAlg(cluster_centers, vectors, abs_dist, abs_step_diff, max_steps):

    # Run K-Means Algorithm:
    avg_dist = 1.7976931348623157e+308
    avg_step_diff = 1.7976931348623157e+308
    step_num = 0
    
    while (avg_dist > abs_dist or avg_step_diff > abs_step_diff) and step_num <= max_steps:
        
        prev_avg_dist = avg_dist
        avg_dist = 0
        
        cluster_assigns = { name : [] for name in cluster_centers }
        
        for vector_name in vectors:
            
            # Assign vector to closest cluster_center (centroid):
            dists = { name : np.linalg.norm(vectors[vector_name] - cluster_centers[name]) for name in cluster_centers }
            
            # Assign vector to closest cluster:
            min_dist = min(dists.values())
            avg_dist += abs(min_dist) / len(vectors)
            for name in dists:
                if dists[name] == min_dist:
                    cluster_assigns[name].append(vector_name)
                    break
                    
        # Update cluster centers to be average of all vectors:
        for name in cluster_assigns:
            vectors_arr = np.array([vectors[vec] for vec in cluster_assigns[name]])
            dims = range(0, vectors_arr.shape[1])
            cluster_centers[name] = np.array([np.mean(vectors_arr[dim]) for dim in dims])
            
        # Compute difference in iteration distance:
        if step_num != 0:
            avg_step_diff = abs(avg_dist - prev_avg_dist)
        else:
            avg_step_diff = avg_dist
        step_num += 1

    return cluster_assigns

###############################
# Main section:
###############################
cluster_centers, vectors = GetVectors('data.csv')
clusters_initial = cluster_centers.copy()
#plot_vectors(cluster_centers, vectors, 10)
kMeansAlg(cluster_centers, vectors, .01, .01, 500)
clusters_final = cluster_centers.copy()
plot_clusters(clusters_initial, clusters_final, vectors)
###############################