#!/usr/bin/env python3

'''
Skeleton for Homework 6: Random Walk Kernel and DBSCAN

Authors: Christian Bock
'''

import numpy as np
import networkx as nx

def reciprocal_degree_matrix(A):
    """
    Creates a diagonal matrix with the inverse of the degree on the diagonal.

    Args:
        np.ndarray: Adjacency matrix of graph for which to compute the inverse degree matrix

    Returns:
        The inverse degree matrix
    """
    
    # Your code goes here

    Dinv = np.zeros((len(A),len(A)))
    for i in range(0,len(A)):
        Dinv[i,i] = 1/np.sum(A[i,:])
    return Dinv

def normalized_adjacency_matrix(A):
    """
    Creates the normalized adjacency matrix as described in the homework sheet

    Args:
        np.ndarray: Adjacency matrix of graph for which to compute the normalized
                   adjacency matrix

    Returns:
        The normalized adjacency
    """

    # Your code goes here

    rec_degree_matrix = reciprocal_degree_matrix(A)
    normalized_adj = rec_degree_matrix.dot(A)
    return normalized_adj

def direct_product_graph_adj_matrix(G_1, G_2):
    """
    Generates the direct product graph from the Kronecker product of G_1 and G_2

    Args:
        G_1 (nx.Graph): First graph for direct product graph construction
        G_2 (nx.Graph): Second graph for direct product graph construction

    Returns:
        nx.Graph: Direct product graph
    """

    # Get normalized adjacency matrix of G_1
    # Your code goes here

    # Get adjacency matrix of G_2
    # Your code goes here

    # Calculate the Kronecker product of of adjacency matrices and return respective graph
    # Your code goes here

    A_1 = normalized_adjacency_matrix(nx.to_numpy_matrix(G_1))
    A_2 = normalized_adjacency_matrix(nx.to_numpy_matrix(G_2))
    return nx.from_numpy_matrix(np.kron(A_1,A_2))


if __name__ == '__main__':
    # This is the code that gets executed when you run 'python hw_6_ex_1b.py'

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

    G_x = direct_product_graph_adj_matrix(G_1, G_2)
    print("The edges of the resulting direct product graph are:")
    for edge in G_x.edges():
        print(edge)

    print("Its weight matrix looks like")
    print(nx.to_numpy_array(G_x))
