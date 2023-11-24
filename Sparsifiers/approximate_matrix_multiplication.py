import numpy as np
import networkx as nx

from constants import getConstObj

"""
Graph Sparsification by Approximate Matrix Multiplication
Neophytos Charalambides, Alfred O. Hero III
https://arxiv.org/abs/2304.08581

ApproxMatMult() implements Algorithm 2
"""

def ApproxMatMult(G, eps):
  B = nx.incidence_matrix(G, oriented=True, weight="weight").toarray().T
  B = np.sqrt(np.abs(B)) * np.sign(B)

  p = []
  for edge in G.edges(data=True):
    p.append(edge[2]["weight"])
  p = np.array(p)
  W = np.sum(p)
  p /= W

  constants = getConstObj()
  t = constants.epsilon * constants.ApproxMatMult_delta
  r = int(1 / (t * t))
  samples = np.random.choice(range(len(p)), r, p=p) 
  
  Incedence = nx.incidence_matrix(G, oriented=True).toarray().T

  n = G.number_of_nodes()
  L = np.zeros((n,n))

  for i in samples:
    L += np.outer(Incedence[i], Incedence[i]) * W / r 
  
  H = nx.from_numpy_matrix(np.diag(np.diagonal(L, 0)) - L)
  return H