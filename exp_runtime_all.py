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

from experiments import runtime_comparison, parse_experiment_data

from constants import getConstObj
from methods_map import getMethodsMap

eps = getConstObj().epsilon

methodsMapObj = getMethodsMap()

names = ["ST", "RQS", "MM", "TR", "EFI", "ER"]
methods = [methodsMapObj.getMethod(name) for name in names]

graph_gen_size = get_random_weighted_graph
sizes = [50, 70, 100, 200, 300, 400, 500]

graph_gen_density = lambda p : get_random_weighted_graph(300, p)
p_values = [.05, .1, .15, .2, .25, .3, .4, .5, .6, .7, .8]



EXP_NAME = "runtime_comparison_all_size"
runtime_comparison(EXP_NAME, names, methods, graph_gen_size, sizes, eps)

exp = load(EXP_NAME)
X, Y_methods = parse_experiment_data(exp)
for name in Y_methods.keys():
  Y = Y_methods[name]
  plt.plot(X, Y, label=methodsMapObj.getLabel(name), c=methodsMapObj.getColor(name))

plt.title("Runtime comparison for Erdős-Rényi graphs of varying size")
plt.xlabel("Graph Size (nodes)")
plt.ylabel("Runtime (seconds)")
plt.legend()
plt.savefig(f"./plots/{EXP_NAME}.png")
plt.cla()


EXP_NAME = "runtime_comparison_all_density"
runtime_comparison(EXP_NAME, names, methods, graph_gen_density, p_values, eps)

exp = load(EXP_NAME)
X, Y_methods = parse_experiment_data(exp)
for name in Y_methods.keys():
  Y = Y_methods[name]
  plt.plot(X, Y, label=methodsMapObj.getLabel(name), c=methodsMapObj.getColor(name))

plt.title("Runtime comparison for Erdős-Rényi graphs of varying density")
plt.xlabel("Edge Probability (p)")
plt.ylabel("Runtime (seconds)")
plt.legend()
plt.savefig(f"./plots/{EXP_NAME}.png")
plt.cla()






names = ["Random Quantized Sampling", "Matrix Multiplication", "Trace Reduction", "Effective Resistances with Inverse"]
methods = [randQuant_Sparsify, ApproxMatMult, TraceRed_Sparsify, EffRes_Pinv]


EXP_NAME = "runtime_comparison_sub_size"
runtime_comparison(EXP_NAME, names, methods, graph_gen_size, sizes, eps)

exp = load(EXP_NAME)
X = exp["X"]
Y_methods = exp["Y"]
for name in Y_methods.keys():
  Y = Y_methods[name]
  plt.plot(X, Y, label=methodsMapObj.getLabel(name), c=methodsMapObj.getColor(name))

plt.title("Runtime comparison for Erdős-Rényi graphs of varying size")
plt.xlabel("Graph Size (nodes)")
plt.ylabel("Runtime (seconds)")
plt.legend()
plt.savefig(f"./plots/{EXP_NAME}.png")
plt.cla()


EXP_NAME = "runtime_comparison_sub_density"
runtime_comparison(EXP_NAME, names, methods, graph_gen_density, p_values, eps)

exp = load(EXP_NAME)
X = exp["X"]
Y_methods = exp["Y"]
for name in Y_methods.keys():
  Y = Y_methods[name]
  plt.plot(X, Y, label=methodsMapObj.getLabel(name), c=methodsMapObj.getColor(name))

plt.title("Runtime comparison for Erdős-Rényi graphs of varying density")
plt.xlabel("Edge Probability (p)")
plt.ylabel("Runtime (seconds)")
plt.legend()
plt.savefig(f"./plots/{EXP_NAME}.png")
plt.cla()