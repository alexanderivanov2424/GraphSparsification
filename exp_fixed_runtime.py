import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

from random_graphs import *
from evaluators import *
from utils import load

from Sparsifiers.effective_resistances import *
from Sparsifiers.approximate_matrix_multiplication import *
from Sparsifiers.quantized_random import *

from experiments import runtime_comparison, parse_experiment_data_mixed, fix_keys

from methods_map import getMethodsMap


methodsMapObj = getMethodsMap()

names = ["ST", "F_RQS", "F_MM", "F_TR", "F_ERI", "F_ER"]
methods = [methodsMapObj.getMethod(name) for name in names]

graph_gen_size = get_random_weighted_graph
sizes = [50, 70, 100, 150, 200, 250, 300, 400]

graph_gen_density = lambda p : get_random_weighted_graph(100, p)
p_values = [.1, .15, .2, .25, .3, .4, .5, .6]


EXP_NAME = "runtime_fixed_comparison_all_size"
runtime_comparison(EXP_NAME, names, methods, graph_gen_size, sizes)

exp = load(EXP_NAME)
fix_keys(exp)
X_methods, Y_methods = parse_experiment_data_mixed(exp)
for name in Y_methods.keys():
  X = X_methods[name]
  Y = Y_methods[name]
  plt.plot(X, Y, label=methodsMapObj.getLabel(name), c=methodsMapObj.getColor(name))

plt.title("Runtime comparison for Erdős-Rényi graphs of varying size")
plt.xlabel("Graph Size (nodes)")
plt.ylabel("Runtime (seconds)")
plt.legend()
plt.savefig(f"./plots/{EXP_NAME}.png")
plt.cla()


EXP_NAME = "runtime_fixed_comparison_all_density"
runtime_comparison(EXP_NAME, names, methods, graph_gen_density, p_values)

exp = load(EXP_NAME)
fix_keys(exp)
X_methods, Y_methods = parse_experiment_data_mixed(exp)
for name in Y_methods.keys():
  X = X_methods[name]
  Y = Y_methods[name]
  plt.plot(X, Y, label=methodsMapObj.getLabel(name), c=methodsMapObj.getColor(name))

plt.title("Runtime comparison for Erdős-Rényi graphs of varying density")
plt.xlabel("Edge Probability (p)")
plt.ylabel("Runtime (seconds)")
plt.legend()
plt.savefig(f"./plots/{EXP_NAME}.png")
plt.cla()





names = ["ST", "RQS", "MM", "ERI"]
methods = [methodsMapObj.getMethod(name) for name in names]
sizes = [50, 70, 100, 200, 300, 400, 500, 700, 1000]
p_values = [.1, .15, .2, .25, .3, .4, .5, .6, .7, .8, .9]

EXP_NAME = "runtime_fixed_comparison_sub_size"
runtime_comparison(EXP_NAME, names, methods, graph_gen_size, sizes)

exp = load(EXP_NAME)
fix_keys(exp)
X_methods, Y_methods = parse_experiment_data_mixed(exp)
for name in Y_methods.keys():
  X = X_methods[name]
  Y = Y_methods[name]
  plt.plot(X, Y, label=methodsMapObj.getLabel(name), c=methodsMapObj.getColor(name))

plt.title("Runtime comparison for Erdős-Rényi graphs of varying size")
plt.xlabel("Graph Size (nodes)")
plt.ylabel("Runtime (seconds)")
plt.legend()
plt.savefig(f"./plots/{EXP_NAME}.png")
plt.cla()


EXP_NAME = "runtime_fixed_comparison_sub_density"
runtime_comparison(EXP_NAME, names, methods, graph_gen_density, p_values)

exp = load(EXP_NAME)
fix_keys(exp)
X_methods, Y_methods = parse_experiment_data_mixed(exp)
for name in Y_methods.keys():
  X = X_methods[name]
  Y = Y_methods[name]
  plt.plot(X, Y, label=methodsMapObj.getLabel(name), c=methodsMapObj.getColor(name))

plt.title("Runtime comparison for Erdős-Rényi graphs of varying density")
plt.xlabel("Edge Probability (p)")
plt.ylabel("Runtime (seconds)")
plt.legend()
plt.savefig(f"./plots/{EXP_NAME}.png")
plt.cla()