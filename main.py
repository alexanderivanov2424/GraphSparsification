

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

from experiments import runtime_comparison

from constants import getConstObj

eps = getConstObj().epsilon


# names = ["Random Quantized Sampling", "Matrix Multiplication", "Effective Resistances"]
# methods = [randQuant_Sparsify, ApproxMatMult, EffRes_Pinv]
# graph_gen = get_random_weighted_graph
# sizes = [50, 70, 100, 200, 300, 500, 700, 1000]

# runtime_comparison("runtime_comparison", names, methods, graph_gen, sizes, eps)
# exp = load("runtime_comparison")
# X = exp["X"]
# Y_methods = exp["Y_methods"]
# plot_XY(X, Y_methods)

# exit()

# G = get_random_weighted_graph(100)
# H = randQuant_Sparsify(G, eps)
# r = evaluate_spectral(G, H, .1)
# print(r)

# exit()

# G = get_random_weighted_graph(100)
# H = ApproxMatMult(G, eps)
# r = evaluate_spectral(G, H, .1)
# print(r)

# exit()

G = get_random_weighted_graph(50)
H = TraceRed_Sparsify(G, eps)
r = evaluate_spectral(G, H, eps)

print(r)
exit()



G = get_random_weighted_graph(50, .5)
H = EffRes_SDDSolver(G, SpanTree_Solver, eps)
# H = EffRes_Pinv(G, eps)
r = evaluate_spectral(G, H, eps)
print(r)
