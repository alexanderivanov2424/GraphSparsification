import numpy as np
import networkx as nx

import heapq

from constants import getConstObj

"""
Pursuing More Effective Graph Spectral Sparsifiers via Approximate Trace Reduction
Zhiqiang Liu, Wenjian Yu
https://arxiv.org/abs/2206.06223

Implementing the main sparsification algorithm, algorithm 2, and the sparse approximate inverse of the Cholesky factor, algorithm 1
"""

def TraceRed_Sparsify(G, eps):
  m = G.number_of_edges()
  alpha = getConstObj().TraceRed_alpha * m
  Nr = getConstObj().TraceRed_Nr
  num_iter = alpha / Nr
  delta = getConstObj().TraceRed_delta
  beta = getConstObj().TraceRed_beta
  eps_traceRed = getConstObj().TraceRed_eps

  S = nx.maximum_spanning_tree(G, weight='weight', algorithm='kruskal')

  markedEdges = set()
  for i in range(1, Nr + 1):
    neighbourhoodMap = buildNeighbourhoodMap(S, beta)
    offSubgraphEdges = getSortedOffSubgraphEdges(G, S, neighbourhoodMap, beta, delta)
    count = 0
    k = 0
    while count < num_iter and k < len(offSubgraphEdges):
      edge, _ = offSubgraphEdges[k]
      k += 1
      edge_tuple = (edge[0], edge[1])
      if not edge_tuple in markedEdges:
        S.add_edge(edge[0], edge[1], weight=edge[2]["weight"])
        markedEdges.add(edge_tuple)
        count += 1
        for similar_edge in getSimilarEdges(edge[0], edge[1], S, neighbourhoodMap, beta, eps_traceRed):
          markedEdges.add(similar_edge)
 
  return S

def getSimilarEdges(p, q, G, neighbourhoodMap, beta, eps=.1):
  Nbp = neighbourhoodMap[p]
  Nbq = neighbourhoodMap[q]
  path = nx.shortest_path(G, source=p, target=q)
  path_edges = set()
  for i in range(len(path) - 1):
    path_edges.add((path[i], path[i+1]))
    path_edges.add((path[i+1], path[i]))

  v = {}
  v[p] = 1
  v[q] = 0
  for edge in nx.bfs_edges(G, p, beta):
    v[edge[1]] = v[edge[0]]
    if edge in path_edges:
      v[edge[1]] -= 1 / G.get_edge_data(edge[0], edge[1])["weight"]

  for edge in nx.bfs_edges(G, q, beta):
    v[edge[0]] = v[edge[1]]
    if edge in path_edges:
      v[edge[0]] += 1 / G.get_edge_data(edge[0], edge[1])["weight"]

  thresh = (v[p] - v[q]) * (1 - eps)
  similar_edges = []
  for i in Nbp:
    t = v[i]
    for j in Nbq:
      if t - v[j] > thresh:
        similar_edges.append((i,j))
  return similar_edges

def getSortedOffSubgraphEdges(G, S, neighbourhoodMap, beta, delta):
  L = nx.laplacian_matrix(S).toarray()
  Z = computeZApprox(L, delta)

  offSubgraphEdges = []
  for edge in G.edges(data=True):
    p = edge[0]
    q = edge[1]
    if S.has_edge(p, q):
      continue
    tTR = truncatedTraceReduction(p, q, G, Z, neighbourhoodMap[p], neighbourhoodMap[q])
    offSubgraphEdges.append((edge, tTR))
  
  offSubgraphEdges.sort(key=lambda x: -x[1])
  return offSubgraphEdges


def truncatedTraceReduction(p, q, G, Z, Nbp, Nbq):
  Zpq = Z[p] - Z[q]
  tTR = 0
  for i in Nbp:
    for j in Nbq:
      e_data = G.get_edge_data(i, j)
      if e_data is None:
        continue
      w = e_data["weight"]
      tTR += w * np.square((Z[i] - Z[j]).T @ Zpq)

  w = G.get_edge_data(p, q)["weight"]
  tTR = tTR * w / (1 + w * np.dot(Zpq, Zpq))
  return tTR

def buildNeighbourhoodMap(G, beta):
  neighbourhoodMap = {}
  for i in range(G.number_of_nodes()):
    neighbourhoodMap[i] = getNeighbourhood(i, G, beta)
  return neighbourhoodMap

def getNeighbourhood(p, G, beta):
  paths = nx.single_source_dijkstra_path_length(G, p, weight="", cutoff=beta)
  neighbourhood = set(paths.keys())
  return neighbourhood


# Sparse Approximate Inverse of the Cholesky Factor
def computeZApprox(L, delta):
  n = len(L)
  Z = np.zeros((n,n))
  for j in range(n-1, -1, -1):
    z = np.eye(n)[j]
    for i in range(n-1, j, -1):
      z -= L[i,j] * Z[i]
    z /= L[j,j]

    if np.sum(z != 0) > np.log(n):
      thresh = delta * np.max(z)
      z[z < thresh] = 0
    Z[j] = z
  return Z


