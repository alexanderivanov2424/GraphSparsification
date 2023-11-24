import numpy as np
import networkx as nx

from constants import getConstObj


"""
A Fast Random Sampling Algorithm for Sparsifying Matrices
Sanjeev Arora, Elad Hazan, Satyen Kale
https://link.springer.com/chapter/10.1007/11830924_26
"""


def randQuant_Sparsify(G, eps):
  A = nx.adjacency_matrix(G, weight="weight").toarray()
  n = G.number_of_nodes()
  A_ = np.zeros((n,n))
  r = eps / np.sqrt(n)
  for i in range(n):
    for j in range(n):
      if A[i,j] > r:
        A_[i,j] = A[i,j]
      elif np.random.rand() < np.abs(A[i,j]) / r:
        A_[i,j] = np.sign(A[i,j]) * r
  H = nx.from_numpy_matrix(A_)
  return H
