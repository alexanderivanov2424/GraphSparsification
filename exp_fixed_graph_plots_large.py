import numpy as np
import networkx as nx
import matplotlib.pyplot as plt


from random_graphs import *
from evaluators import *
from utils import load

from Sparsifiers.effective_resistances import *
from Sparsifiers.approximate_matrix_multiplication import *
from Sparsifiers.quantized_random import *

from experiments import spectral_error_comparison, spectral_error_ratio_comparison, parse_experiment_data_mixed, fix_keys

from methods_map import getMethodsMap
from constants import getConstObj

import osmnx as ox

methodsMapObj = getMethodsMap()

names = ["F_RQS", "F_MM", "F_TR", "F_ER", "F_ERI"]

graphs = {}

G = ox.graph_from_point((37.6020, -120.8653), network_type="walk", dist=1000, simplify=True).to_undirected()
G = nx.convert_node_labels_to_integers(nx.Graph(G))
set_uniform_weights(G, 1.0)
graphs["Huston"] = G

G = ox.graph_from_point((40.7831, -73.9712), network_type="walk", dist=500, simplify=True).to_undirected()
G = nx.convert_node_labels_to_integers(nx.Graph(G))
set_uniform_weights(G, 1.0)
graphs["Manhattan"] = G

G = ox.graph_from_point((25.7617, -80.1918), network_type="walk", dist=300, simplify=True).to_undirected()
G = nx.convert_node_labels_to_integers(nx.Graph(G))
print(G.number_of_nodes(), G.number_of_edges())
set_uniform_weights(G, 1.0)
graphs["Miami"] = G

G = ox.graph_from_point((37.858495, -122.267468), network_type="walk", dist=500, simplify=True).to_undirected()
G = nx.convert_node_labels_to_integers(nx.Graph(G))
print(G.number_of_nodes(), G.number_of_edges())
set_uniform_weights(G, 1.0)
graphs["Berkeley"] = G


for key in graphs:
  G = graphs[key]
  pos = nx.spring_layout(G, iterations=150)

  nx.draw(G, pos=pos, node_size=3)
  plt.savefig(f"./GraphPlots/graph_{key}.png")
  plt.cla()

  for name in names:
    print(key, name, G.number_of_nodes(), G.number_of_edges())
    if G.number_of_edges() > 500 and name in ["F_TR", "F_ER", "F_MM"]:
      continue

    method = methodsMapObj.getMethod(name)
    for ratio in [0.5, 0.75]:
      getConstObj().edgeRatio = ratio
      H = method(G)

      nx.draw(H, pos=pos, node_size=3)
      plt.savefig(f"./GraphPlots/graph_{key}_{name}_{ratio}.png")
      plt.cla()
