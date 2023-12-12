import numpy as np
import networkx as nx

from constants import getConstObj


"""
A Fast Random Sampling Algorithm for Sparsifying Matrices
Sanjeev Arora, Elad Hazan, Satyen Kale
https://link.springer.com/chapter/10.1007/11830924_26
"""

def randQuant_Sparsify_Fixed(G):
  eps = getConstObj().epsilon
  num_edges = G.number_of_edges() * getConstObj().edgeRatio

  A = nx.adjacency_matrix(G, weight="weight").toarray()
  n = G.number_of_nodes()
  A_ = np.zeros((n,n))
  r = eps / np.sqrt(n)
  
  norm = num_edges * (np.sum(np.abs(A[A<r])) + len(A > r))

  for i in range(n):
    for j in range(n):
      if A[i,j] > r:
        A_[i,j] = A[i,j]
      elif np.random.rand() < np.abs(A[i,j]) / norm:
        A_[i,j] = np.sign(A[i,j]) * r
  H = nx.from_numpy_matrix(A_)
  return H

def randQuant_Sparsify(G):
  eps = getConstObj().epsilon

  A = nx.adjacency_matrix(G, weight="weight").toarray()
  n = G.number_of_nodes()
  A_ = np.zeros((n,n))
  r = eps / np.sqrt(n)
  norm = np.sum(np.abs(A[A <= r]) / r)
  for i in range(n):
    for j in range(n):
      if A[i,j] > r:
        A_[i,j] = A[i,j]
      elif np.random.rand() < np.abs(A[i,j]) / (r * norm):
        A_[i,j] = np.sign(A[i,j]) * r
  H = nx.from_numpy_matrix(A_)
  return H
