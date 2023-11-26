import numpy as np
import networkx as nx


def evaluate_spectral(G, H, eps, num_tests = 100):
  n = G.number_of_nodes()
  successful_test_count = 0

  #precomputing sqrt of weighted incidence matrix: sqrt(B)
  B_G = get_sqrt_incidence(G)
  B_H = get_sqrt_incidence(H)

  for test in range(num_tests):
    x = np.random.rand(n)

    G_sum = spectral_sum_for_graph(B_G, x)
    H_sum = spectral_sum_for_graph(B_H, x)

    if G_sum * (1 - eps) < H_sum and H_sum < G_sum * (1 + eps):
       successful_test_count += 1
    else:
       print(G_sum, H_sum)
       pass

  return successful_test_count/num_tests

def average_error_spectral(G, H, num_tests = 100):
  n = G.number_of_nodes()

  #precomputing sqrt of weighted incidence matrix: sqrt(B)
  B_G = get_sqrt_incidence(G)
  B_H = get_sqrt_incidence(H)

  errors = []

  for test in range(num_tests):
    x = np.random.rand(n)

    G_sum = spectral_sum_for_graph(B_G, x)
    H_sum = spectral_sum_for_graph(B_H, x)

    errors.append(np.abs(G_sum - H_sum))

  return np.mean(errors)

def average_error_ratio_spectral(G, H, num_tests = 100):
  n = G.number_of_nodes()

  #precomputing sqrt of weighted incidence matrix: sqrt(B)
  B_G = get_sqrt_incidence(G)
  B_H = get_sqrt_incidence(H)

  errors = []

  for test in range(num_tests):
    x = np.random.rand(n)

    G_sum = spectral_sum_for_graph(B_G, x)
    H_sum = spectral_sum_for_graph(B_H, x)

    errors.append(H_sum/G_sum)

  return np.mean(errors)

def evaluate_spectral_int(G, H, eps):
  n = G.number_of_nodes()
  successful_test_count = 0

  #precomputing sqrt of weighted incidence matrix: sqrt(B)
  B_G = get_sqrt_incidence(G)
  B_H = get_sqrt_incidence(H)

  for i in range(n):
    x = np.zeros((n,1))
    x[i] = 1

    G_sum = spectral_sum_for_graph(B_G, x)
    H_sum = spectral_sum_for_graph(B_H, x)

    if G_sum * (1 - eps) < H_sum and H_sum < G_sum * (1 + eps):
       successful_test_count += 1
    else:
       print(G_sum, H_sum)
       pass

  return successful_test_count/n

def average_error_int_ratio_spectral(G, H):
  n = G.number_of_nodes()

  #precomputing sqrt of weighted incidence matrix: sqrt(B)
  B_G = get_sqrt_incidence(G)
  B_H = get_sqrt_incidence(H)

  errors = []

  for i in range(n):
    x = np.zeros((n,1))
    x[i] = 1

    G_sum = spectral_sum_for_graph(B_G, x)
    H_sum = spectral_sum_for_graph(B_H, x)

    errors.append(H_sum/G_sum)

  return np.mean(errors)

def get_sqrt_incidence(G):
  B = nx.incidence_matrix(G, oriented=True, weight="weight").toarray().T
  return np.sqrt(np.abs(B)) * np.sign(B)

def spectral_sum_for_graph(sqrt_B, x):
  #multiplying sqrt(B) by x. For edge e = (a,b) with weight e_w this gives
  # (x[a] - x[b])^2 * e_w
  # summed for all edges
  return np.sum(np.square(np.matmul(sqrt_B, x)))

def laplacian_L2(G, H):
   L_G = nx.laplacian_matrix(G).toarray()
   L_H = nx.laplacian_matrix(H).toarray()
   return np.sum(np.square(L_G - L_H))

def adjacency_L2(G, H):
   L_G = nx.adjacency_matrix(G).toarray()
   L_H = nx.adjacency_matrix(H).toarray()
   return np.sum(np.square(L_G - L_H))

def evaluate_laplacian_L2(G, H, eps):
   return 1.0 if laplacian_L2(G, H) < eps else 0.0

def evaluate_adjacency_L2(G, H, eps):
   return 1.0 if adjacency_L2(G, H) < eps else 0.0

def relativeConditionNumberBound(G, H):
   L_G = nx.laplacian_matrix(G).toarray()
   L_H = nx.laplacian_matrix(H).toarray()
   L_H_inv = np.linalg.inv(L_H)
   return np.trace(L_H_inv @ L_G)

def edgeReductionRatio(G, H):
   return H.number_of_edges() / G.number_of_edges()