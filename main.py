

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

eps = getConstObj().epsilon
methodsMapObj = getMethodsMap()


#manual plot generation

names = ["RQS", "MM", "EFI"]


EXP_NAME = "spectral_error_ratio_comparison_size"
exp = load(EXP_NAME)
fix_keys(exp)
X_methods, Y_methods = parse_experiment_data_mixed(exp)
for name in names:
  X = X_methods[name]
  Y = Y_methods[name]
  plt.plot(X, Y, label=methodsMapObj.getLabel(name), c=methodsMapObj.getColor(name))

plt.title("L1 Spectral Error Ratio for Erdős-Rényi graphs of varying size")
plt.xlabel("Graph Size (nodes)")
plt.ylabel("Average L1 Spectral Error Ratio")
plt.legend()
plt.savefig(f"./plots/{EXP_NAME}_manual.png")
plt.cla()


EXP_NAME = "spectral_error_ratio_comparison_density"
exp = load(EXP_NAME)
fix_keys(exp)
X_methods, Y_methods = parse_experiment_data_mixed(exp)
for name in names:
  X = X_methods[name]
  Y = Y_methods[name]
  plt.plot(X, Y, label=methodsMapObj.getLabel(name), c=methodsMapObj.getColor(name))

plt.title("L1 Spectral Error Ratio for Erdős-Rényi graphs of varying density")
plt.xlabel("Edge Probability (p)")
plt.ylabel("Average L1 Spectral Error Ratio")
plt.legend()
plt.savefig(f"./plots/{EXP_NAME}_manual.png")
plt.cla()