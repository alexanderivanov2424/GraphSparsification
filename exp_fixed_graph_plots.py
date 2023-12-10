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


methodsMapObj = getMethodsMap()

names = ["ST", "F_RQS", "F_MM", "F_TR", "F_ER", "F_ERI"]

graphs = {}

G = nx.connected_caveman_graph(10, 30)
set_random_weights(G)
graphs["caveman"] = G


G = nx.relaxed_caveman_graph(10, 30, .1, seed=0)
set_random_weights(G)
graphs["rel_caveman"] = G


G = nx.barabasi_albert_graph(300, 5, seed=0)
set_random_weights(G)
graphs["preferential"] = G


G = nx.grid_2d_graph(17, 17, periodic=False)
set_random_weights(G)
graphs["2d_grid"] = G


for key in graphs:
  G = graphs[key]
  pos = nx.spring_layout(G, k = 10 / np.sqrt(G.number_of_nodes()), iterations=100)

  nx.draw(G, pos=pos, node_size=3)
  plt.savefig(f"./GraphPlots/graph_{key}.png")
  plt.cla()

  for name in names:
    method = methodsMapObj.getMethod(name)
    for ratio in [0.05, 0.1, 0.25, 0.5]:
      getConstObj().edgeRatio = ratio
      H = method(G)

      nx.draw(H, pos=pos, node_size=3)
      plt.savefig(f"./GraphPlots/graph_{key}_{name}_{ratio}.png")
      plt.cla()
