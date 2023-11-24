import numpy as np
import networkx as nx


"""
Naive approach which returns just the maximum spanning tree
"""


def spanTree_Sparsify(G, eps):
  return nx.maximum_spanning_tree(G, weight='weight', algorithm='kruskal')