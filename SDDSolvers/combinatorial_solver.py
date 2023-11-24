import numpy as np
import networkx as nx

from constants import getConstObj

"""
A Simple, Combinatorial Algorithm for Solving SDD Systems in Nearly-Linear Time
Jonathan A. Kelner, Lorenzo Orecchia, Aaron Sidford
https://arxiv.org/pdf/1301.6628.pdf


"""
  
def Comb_Solver(G, x, eps):
  n = G.number_of_nodes()
  T = nx.minimum_spanning_tree(G, weight='weight', algorithm='kruskal')

  f = np.zeros(n)
  B = nx.incidence_matrix(G, oriented=True, weight="weight").toarray().T

  # TODO need a good way to compute initial flow f_0
  # this solves B^T * f_0 = x which seems like just pushing the problem of solving L * v = x back a step

  # TODO implement data structure that actually allows cycle sampling to be log(n) time.

