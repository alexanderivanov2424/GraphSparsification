import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

def set_graph_weights_to_one(G):
  for edge in G.edges:
    G[edge[0]][edge[1]]['weight'] = 1.0

def get_barbel_graph():
  G = nx.barbell_graph(30, 1)
  set_graph_weights_to_one(G)
  return G

def get_random_unweighted_graph(n, p = .1, seed = 0):
  G = nx.fast_gnp_random_graph(n, p, seed=seed)
  set_graph_weights_to_one(G)
  connect_graph(G)
  return G

def get_random_weighted_graph(n, p = .1, seed = 0):
  G = nx.fast_gnp_random_graph(n, p, seed=seed)
  np.random.seed(seed)
  for edge in G.edges:
    G[edge[0]][edge[1]]['weight'] = np.random.rand()
  connect_graph(G)
  return G

def connect_graph(G):
  comps = list(nx.connected_components(G))
  root = list(comps[0])
  for i in range(1, len(comps)):
    G.add_edge(np.random.choice(root), np.random.choice(list(comps[i])))