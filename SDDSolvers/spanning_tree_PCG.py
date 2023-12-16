import numpy as np
import networkx as nx

from scipy.sparse import csc_matrix
from scipy.sparse.linalg import cg

from constants import getConstObj

"""
A Note on Preconditioning by Low-Stretch Spanning Trees
Daniel A. Spielman, Jae Oh Woo
https://arxiv.org/abs/0903.2816

"""

class SpanTree_Solver:
  def __init__(self, G, eps):
    # TODO this is wrong. A minimum spanning tree is not equivalent to a low stretch spanning tree
    T = nx.minimum_spanning_tree(G, weight='weight', algorithm='kruskal')
    self.L = csc_matrix(nx.laplacian_matrix(G).toarray())
    self.L_T = csc_matrix(nx.laplacian_matrix(T).toarray())

  def solve(self, x):
    y, exit_code = cg(A = self.L, b = x, M = self.L_T)
    return y



