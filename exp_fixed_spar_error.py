import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

from random_graphs import *
from evaluators import *
from utils import load

from Sparsifiers.effective_resistances import *
from Sparsifiers.approximate_matrix_multiplication import *
from Sparsifiers.quantized_random import *

from experiments import spectral_error_comparison_ratio, laplacian_error_comparison_ratio, parse_experiment_data_mixed, fix_keys

from methods_map import getMethodsMap


methodsMapObj = getMethodsMap()

names = ["ST", "F_RQS", "F_MM", "F_TR", "F_ERI", "F_ER"]
methods = [methodsMapObj.getMethod(name) for name in names]

graph_gen = lambda : get_random_weighted_graph(300)
edgeRatios = [.05, .1, .2, .3, .4, .5]



EXP_NAME = "spectral_fixed_error_comparison_ratio"
spectral_error_comparison_ratio(EXP_NAME, names, methods, graph_gen, edgeRatios)

exp = load(EXP_NAME)
fix_keys(exp)
X_methods, Y_methods = parse_experiment_data_mixed(exp)
for name in Y_methods.keys():
  X = X_methods[name]
  Y = Y_methods[name]
  plt.plot(X, Y, label=methodsMapObj.getLabel(name), c=methodsMapObj.getColor(name))

plt.title("Average L1 Spectral Error for Varying Edge Retention")
plt.xlabel("Fraction of Edges Retained")
plt.ylabel("Average L1 Spectral Error")
plt.legend()
plt.savefig(f"./plots/{EXP_NAME}.png")
plt.cla()


EXP_NAME = "laplacian_fixed_error_comparison_ratio"
laplacian_error_comparison_ratio(EXP_NAME, names, methods, graph_gen, edgeRatios)

exp = load(EXP_NAME)
fix_keys(exp)
X_methods, Y_methods = parse_experiment_data_mixed(exp)
for name in Y_methods.keys():
  X = X_methods[name]
  Y = Y_methods[name]
  plt.plot(X, Y, label=methodsMapObj.getLabel(name), c=methodsMapObj.getColor(name))

plt.title("L2 Laplacian Error for Varying Edge Retention")
plt.xlabel("Fraction of Edges Retained")
plt.ylabel("L2 Laplacian Error")
plt.legend()
plt.savefig(f"./plots/{EXP_NAME}.png")
plt.cla()