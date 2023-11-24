import numpy as np
import networkx as nx
from sksparse.cholmod import cholesky


"""
Approximate Gaussian Elimination for Laplacians – Fast, Sparse, and Simple
Rasmus Kyng, Sushant Sachdeva
https://arxiv.org/pdf/1605.02353.pdf

existing implementation can be found here:


Sparse Cholesky decomposition
https://scikit-sparse.readthedocs.io/en/latest/cholmod.html


from sksparse.cholmod import cholesky
factor = cholesky(A)
x = factor(b)
"""

# convenience wrapper
def Cholesky_Solver(G, x, eps):
  L = nx.laplacian_matrix(G).toarray().T
  factor = cholesky(L)
  return factor(x)