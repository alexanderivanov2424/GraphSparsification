import numpy as np
import networkx as nx

from constants import getConstObj

"""
Graph Sparsification by Effective Resistances
Daniel A. Spielman, Nikhil Srivastava
https://arxiv.org/abs/0803.0929

EffRes_Pinv() implements the algorithm in section 1.1, computing effective resistances directly from Moore-Penrose Pseudoinverse
"""


def EffRes_SampleCount(n, eps):
  C = getConstObj().EffRes_C
  return int(9.0 * C * C * n * np.log(n) / (eps * eps))

def EffRes_Pinv_Fixed(G):
  num_edges = int(G.number_of_edges() * getConstObj().edgeRatio)
  return EffRes_Pinv_Base(G, num_edges, True)

def EffRes_Pinv(G):
  return EffRes_Pinv_Base(G)

# Compute effective resistances directly from Moore-Penrose Pseudoinverse
def EffRes_Pinv_Base(G, num_edges = 0, forceEdges = False):
  n = G.number_of_nodes()
  eps = getConstObj().epsilon
  q = EffRes_SampleCount(n, eps)

  L = nx.laplacian_matrix(G).toarray()
  L_pinv = np.linalg.pinv(L)

  weights = []

  for edge in G.edges(data=True):
    X = np.zeros((n, 1))
    X[edge[0]] = 1
    X[edge[1]] = -1
    r = (X.T @ L_pinv @ X)[0,0]
    w = edge[2]["weight"] if "weight" in edge[2] else 1.0
    weights.append(r * w)

  weights = np.array(weights)
  weights = weights / np.sum(weights)

  H = nx.Graph()
  H.add_nodes_from(G.nodes)

  edges = list(G.edges(data=True))

  num_samples = 0
  while H.number_of_edges() < num_edges:
    samples = np.random.choice(range(len(weights)), q, p=weights) 

    for sample in samples:
      edge = edges[sample]
      w = edge[2]["weight"]/weights[sample]

      if H.has_edge(edge[0], edge[1]):
        H[edge[0]][edge[1]]["weight"] += w
      else:
        H.add_edge(edge[0], edge[1], weight=w)

      num_samples += 1

      if forceEdges and H.number_of_edges() >= num_edges:
        break

    if not forceEdges:
      break
  
  edges = list(H.edges(data=True))
  for edge in edges:
    H[edge[0]][edge[1]]["weight"] /= num_samples

  return H

# estimation of L_pinv as described in theorem 8. solver can be an arbirary SDD solver L * x = y
def ComputeREstimate(G, SDDSolver, eps):
  n = G.number_of_nodes()
  m = G.number_of_edges()
  k = int(24 * np.log(n) / (eps * eps))

  Q = np.random.randint(0, 2, (k, m)) * 2.0 - 1.0
  Q /= np.sqrt(float(k))
  W = np.diag([e[2]["weight"] for e in G.edges(data=True)])
  B = nx.incidence_matrix(G, oriented=True, weight="weight").toarray().T

  Y = np.matmul(Q, np.matmul(W, B))
  
  solver = SDDSolver(G, eps)
  Z = []
  for y in Y:
    Z.append(solver.solve(y))
  
  return np.array(Z)

def EffRes_SDDSolver_Fixed(G, SDDSolver):
  num_edges = int(G.number_of_edges() * getConstObj().edgeRatio)
  return EffRes_SDDSolver_Base(G, SDDSolver, num_edges, True)

def EffRes_SDDSolver(G, SDDSolver):
  return EffRes_SDDSolver_Base(G, SDDSolver)

# Estimate effective resistances using provided solver
def EffRes_SDDSolver_Base(G, SDDSolver, num_edges = 0, forceEdges = False):
  n = G.number_of_nodes()
  eps = getConstObj().epsilon
  q = EffRes_SampleCount(n, eps)

  Z = ComputeREstimate(G, SDDSolver, eps)

  weights = []

  for edge in G.edges(data=True):
    X = np.zeros((n, 1))
    X[edge[0]] = 1
    X[edge[1]] = -1
    r = np.sum(np.square(Z @ X))
    w = edge[2]["weight"] if "weight" in edge[2] else 1.0
    weights.append(r * w)

  weights = np.array(weights)
  weights = weights / np.sum(weights)

  H = nx.Graph()
  H.add_nodes_from(G.nodes)

  edges = list(G.edges(data=True))

  num_samples = 0

  while H.number_of_edges() < num_edges:
    samples = np.random.choice(range(len(weights)), q, p=weights) 

    for sample in samples:
      edge = edges[sample]
      w = edge[2]["weight"]/weights[sample]

      if H.has_edge(edge[0], edge[1]):
        H[edge[0]][edge[1]]["weight"] += w
      else:
        H.add_edge(edge[0], edge[1], weight=w)
      
      num_samples += 1
      
      if forceEdges and H.number_of_edges() >= num_edges:
        break

    if not forceEdges:
      break

  edges = list(H.edges(data=True))
  for edge in edges:
    H[edge[0]][edge[1]]["weight"] /= num_samples
    
  return H