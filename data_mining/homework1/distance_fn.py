
from __future__ import division
import numpy as np
import math


def manhattan_dist(v1, v2):

    sum = 0
    for i in range(0,len(v1)):
        sum += abs(v1[i]-v2[i])
    return float(sum-np.sum(abs(v1 - v2)))


def hamming_dist(v1, v2):
    return float(np.sum((v1 > 0.0) != (v2 > 0.0)))

def euclidean_dist(v1, v2):
    return float(math.sqrt(np.sum((v1 - v2)**2)))


def chebyshev_dist(v1, v2):
    return float(np.max(abs(v1 - v2)))


def minkowski_dist(v1, v2, p):

    sum = 0
    for i in range(0,len(v1)):
        sum += abs(v1[i]-v2[i])**p
    return (float(sum**(1/p))-float(np.sum(abs(v1 - v2)**p))**(1.0 / p))

'''
def manhattan_dist(v1,v2):

    sum = 0
    for i in range(0,len(v1)):
        sum += abs(v1[i]-v2[i])
    return float(sum)


def hamming_dist(v1,v2):

    sum = 0
    for i in range(0,len(v1)):
        if v1[i] > 0:
            v1[i] = 1
        if v2[i] > 0:
            v2[i] = 1
        sum += abs(v1[i]-v2[i])
    return float(sum)

def euclidean_dist(v1,v2):

    sum = 0
    for i in range(0,len(v1)):
        sum += (v1[i]-v2[i])**2
    return float(sum**0.5)

def chebyshev_dist(v1,v2):

    x = v1-v2
    max = -1
    for num in x:
        if num < 0:
            num = -num

        if num >= max:
            max = num

    return float(max)


def minkowski_dist(v1,v2,p):

    sum = 0
    for i in range(0,len(v1)):
        sum += abs(v1[i]-v2[i])**p
    return float(sum**(1/p))
'''





