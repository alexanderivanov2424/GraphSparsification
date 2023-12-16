

"""
generate graphs

compute metrics

sparcify

compute metrics

compare
"""

import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

from random_graphs import *
from evaluators import *
from utils import load

from Sparsifiers.effective_resistances import *
from Sparsifiers.approximate_matrix_multiplication import *
from Sparsifiers.quantized_random import *
from Sparsifiers.trace_reduction import TraceRed_Sparsify

from SDDSolvers.spanning_tree_PCG import SpanTree_Solver

from experiments import spectral_error_comparison, spectral_error_ratio_comparison, parse_experiment_data_mixed, fix_keys

from constants import getConstObj
from methods_map import getMethodsMap

import matplotlib
import osmnx as ox



places = []
#places.append("Piedmont, California, USA")
#places.append("Manhattan, New York, New York, USA")
#places.append("Miami, FL, USA")
places.append("Berkeley, California, USA")

for place in places:
  G = ox.graph_from_place(place, network_type="drive", simplify=True).to_undirected()
  print(G.number_of_nodes())
  print(G.number_of_edges())
  nx.draw(G, node_size=3)
  plt.show()

