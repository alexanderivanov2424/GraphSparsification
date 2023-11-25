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


from experiments import condition_number_comparison

from constants import getConstObj
from methods_map import getMethodsMap

eps = getConstObj().epsilon

methodsMapObj = getMethodsMap()

names = ["ST", "RQS", "MM", "TR", "EFI"]
methods = [methodsMapObj.getMethod(name) for name in names]

graph_gen_size = get_random_weighted_graph
sizes = [50, 70, 100, 200, 300, 500]

graph_gen_density = lambda p : get_random_weighted_graph(300, p)
p_values = [.05, .1, .15, .2, .25, .3, .4, .5, .6, .7, .8, .9]


EXP_NAME = "edgRatio_comparison_size"
condition_number_comparison(EXP_NAME, names, methods, graph_gen_size, sizes, eps)

exp = load(EXP_NAME)
X = exp["X"]
Y_methods = exp["Y"]
for name in Y_methods.keys():
  Y = Y_methods[name]
  plt.plot(X, Y, label=methodsMapObj.getLabel(name), c=methodsMapObj.getColor(name))

plt.title("Fraction of edges remaining for Erdős-Rényi graphs of varying size")
plt.xlabel("Graph Size (nodes)")
plt.ylabel("Fraction of Edges Remaining")
plt.legend()
plt.savefig(f"./plots/{EXP_NAME}.png")
plt.cla()


EXP_NAME = "edgRatio_comparison_density"
condition_number_comparison(EXP_NAME, names, methods, graph_gen_density, p_values, eps)

exp = load(EXP_NAME)
X = exp["X"]
Y_methods = exp["Y"]
for name in Y_methods.keys():
  Y = Y_methods[name]
  plt.plot(X, Y, label=methodsMapObj.getLabel(name), c=methodsMapObj.getColor(name))

plt.title("Fraction of edges remaining for Erdős-Rényi graphs of varying density")
plt.xlabel("Edge Probability (p)")
plt.ylabel("Fraction of Edges Remaining")
plt.legend()
plt.savefig(f"./plots/{EXP_NAME}.png")
plt.cla()