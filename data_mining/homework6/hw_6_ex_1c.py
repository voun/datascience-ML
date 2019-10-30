#!/usr/bin/env python3

'''
Skeleton for Homework 6: Random Walk Kernel and DBSCAN

Authors: Christian Bock
'''

import numpy as np
import networkx as nx
from hw_6_ex_1a import *
from hw_6_ex_1b import *

def degree_matrix(A):
    """
    Creates degree matrix from given adjacency matrix A

    Args:
        Adjacency matrix

    Returns:
        np.ndarray: Degree matrix of graph represented by adjacency matrix A
    """
    
    # Your code goes here

    degree_matrix = np.zeros((len(A),len(A)))
    for i in range(0,len(A)):
        degree_matrix[i,i] = np.sum(A[i,:])

    return degree_matrix

def starting_prob_vector(A):
    """
    Creates an 1 x n dimensional vector whose entries 
    are the degree of the nth node normalized by the sum of all degrees

    Args:
        Adjacency matrix

    Returns:
        np.ndarray: 1 x n dimensional vector with starting probabilities
    """
    
    # Your code goes here

    diag = np.diagonal(degree_matrix(A))
    return diag/np.sum(diag)

def stopping_prob_vector(A):
    """
    Creates an 1 x n dimensional vector whose entries 
    are the degree of the nth node normalized by the sum of all degrees

    Args:
        Adjacency matrix

    Returns:
        np.ndarray: 1 x n dimensional vector with stopping probabilities
    """
    
    # Your code goes here

    return starting_prob_vector(A)

def rw_kernel(G_1, G_2, lam):
    """
    Calculates the random walk kernel as defined in equation 2 of the homework sheet
    The starting and stopping probabilities are supposed to be calculated in this function

    Args:
        G_1 (nx.Graph): First graph for direct product graph construction
        G_2 (nx.Graph): Second graph for direct product graph construction
        lam (float): lambda parameter

    Returns:
        The value of the random walk graph kernel applied to the graphs
        of figure 1 of the homework sheet
    """

    # Your code goes here
    G_x = nx.to_numpy_matrix(direct_product_graph_adj_matrix(G_1,G_2))
    start_prob = starting_prob_vector(G_x)
    stop_prob = stopping_prob_vector(G_x)

    return stop_prob.T.dot(np.linalg.inv(np.eye(len(G_x))-lam*G_x)).dot(start_prob)

if __name__ == '__main__':
    # This is the code that gets executed when you run 'python hw_6_ex_1c.py' 

    # TODO: Generate Graph 1 with edges from:
    #    node 1 to node 2
    #    node 1 to node 3
    #    node 2 to node 3

    # Your code goes here

    # TODO: Generate Graph 2
    #    node 1' to node 2'
    #    node 1' to node 4'
    #    node 2' to node 3'
    #    node 3' to node 4'

    # Your code goes here

    G_1 = nx.Graph()
    G_1.add_nodes_from([1,2,3])
    G_1.add_edges_from([(1,2),(1,3),(2,3)])

    G_2 = nx.Graph()
    G_2.add_nodes_from(["1'","2'","3'","4'"])
    G_2.add_edges_from([("1'","2'"),("1'","4'"),("2'","3'"),("3'","4'")])

    kernel_result = rw_kernel(G_1, G_2, 0.01)
    print(kernel_result)
