import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

from random_graphs import *
from evaluators import *
from utils import load

from Sparsifiers.effective_resistances import *
from Sparsifiers.approximate_matrix_multiplication import *
from Sparsifiers.quantized_random import *


from experiments import condition_number_comparison, parse_experiment_data_mixed, fix_keys

from methods_map import getMethodsMap


methodsMapObj = getMethodsMap()

names = ["F_RQS", "F_MM", "F_TR", "F_ERI"]
methods = [methodsMapObj.getMethod(name) for name in names]

graph_gen_size = get_random_weighted_graph
sizes = [50, 70, 100, 200, 300]#, 400, 500]

graph_gen_density = lambda p : get_random_weighted_graph(100, p)
p_values = [.1, .15, .2, .25, .3, .4, .5, .6, .7, .8]


EXP_NAME = "condNum_fixed_comparison_size"
condition_number_comparison(EXP_NAME, names, methods, graph_gen_size, sizes)

exp = load(EXP_NAME)
fix_keys(exp)
X_methods, Y_methods = parse_experiment_data_mixed(exp)
for name in Y_methods.keys():
  X = X_methods[name]
  Y = Y_methods[name]
  plt.plot(X, Y, label=methodsMapObj.getLabel(name), c=methodsMapObj.getColor(name))

plt.title("Approximate Condition Number for Erdős-Rényi graphs of varying size")
plt.xlabel("Graph Size (nodes)")
plt.ylabel("Approximate Condition Number")
plt.legend()
plt.savefig(f"./plots/{EXP_NAME}.png")
plt.cla()


EXP_NAME = "condNum_fixed_comparison_density"
condition_number_comparison(EXP_NAME, names, methods, graph_gen_density, p_values)

exp = load(EXP_NAME)
fix_keys(exp)
X_methods, Y_methods = parse_experiment_data_mixed(exp)
for name in Y_methods.keys():
  X = X_methods[name]
  Y = Y_methods[name]
  plt.plot(X, Y, label=methodsMapObj.getLabel(name), c=methodsMapObj.getColor(name))

plt.title("Approximate Condition Number for Erdős-Rényi graphs of varying density")
plt.xlabel("Edge Probability (p)")
plt.ylabel("Approximate Condition Number")
plt.legend()
plt.savefig(f"./plots/{EXP_NAME}.png")
plt.cla()


graph_gen_size = get_random_unweighted_graph

EXP_NAME = "condNum_fixed_comparison_unweighted_size"
condition_number_comparison(EXP_NAME, names, methods, graph_gen_size, sizes)

exp = load(EXP_NAME)
fix_keys(exp)
X_methods, Y_methods = parse_experiment_data_mixed(exp)
for name in Y_methods.keys():
  X = X_methods[name]
  Y = Y_methods[name]
  plt.plot(X, Y, label=methodsMapObj.getLabel(name), c=methodsMapObj.getColor(name))

plt.title("Approximate Condition Number for\nUnweighted Erdős-Rényi graphs of varying size")
plt.xlabel("Graph Size (nodes)")
plt.ylabel("Approximate Condition Number")
plt.legend()
plt.savefig(f"./plots/{EXP_NAME}.png")
plt.cla()


EXP_NAME = "condNum_fixed_comparison_unweighted_density"
condition_number_comparison(EXP_NAME, names, methods, graph_gen_density, p_values)

exp = load(EXP_NAME)
fix_keys(exp)
X_methods, Y_methods = parse_experiment_data_mixed(exp)
for name in Y_methods.keys():
  X = X_methods[name]
  Y = Y_methods[name]
  plt.plot(X, Y, label=methodsMapObj.getLabel(name), c=methodsMapObj.getColor(name))

plt.title("Approximate Condition Number for\nUnweighted Erdős-Rényi graphs of varying density")
plt.xlabel("Edge Probability (p)")
plt.ylabel("Approximate Condition Number")
plt.legend()
plt.savefig(f"./plots/{EXP_NAME}.png")
plt.cla()