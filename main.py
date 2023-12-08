

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


import exp_fixed_edgeRatio
import exp_fixed_condNum
import exp_fixed_error
import exp_fixed_runtime