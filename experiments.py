import numpy as np
import time
import networkx as nx

from utils import save
from evaluators import *

def runtime_comparison(exp_name, names, methods, graph_generator, sizes, eps):
  X = []
  Y_methods = {}

  for name in names:
    Y_methods[name] = []

  print(exp_name)
  TOTAL_RUNS = len(sizes) * len(methods)
  RUN_COUNT = 0

  for n in sizes:
    G = graph_generator(n)
    X.append(n)

    for i, method in enumerate(methods):
      t, _ = time_method(method, (G, eps))
      Y_methods[names[i]].append(t)

      RUN_COUNT+=1
      print(f"{RUN_COUNT}/{TOTAL_RUNS}", end="\r")

  experiment = {"X" : X, "Y": Y_methods}
  save(experiment, exp_name)


def time_method(method, inputs):
  t = time.time()
  val = method(*inputs)
  return (time.time() - t), val

def edge_reduction_comparison(exp_name, names, methods, graph_generator, sizes, eps):
  generic_comparison(edgeReductionRatio, exp_name, names, methods, graph_generator, sizes, eps)

def spectral_error_comparison(exp_name, names, methods, graph_generator, sizes, eps):
  generic_comparison(average_error_spectral, exp_name, names, methods, graph_generator, sizes, eps)

def adjacency_error_comparison(exp_name, names, methods, graph_generator, sizes, eps):
  generic_comparison(adjacency_L2, exp_name, names, methods, graph_generator, sizes, eps)

def laplacian_error_comparison(exp_name, names, methods, graph_generator, sizes, eps):
  generic_comparison(laplacian_L2, exp_name, names, methods, graph_generator, sizes, eps)

def condition_number_comparison(exp_name, names, methods, graph_generator, sizes, eps):
  generic_comparison(relativeConditionNumberBound, exp_name, names, methods, graph_generator, sizes, eps)

def generic_comparison(eval_func, exp_name, names, methods, graph_generator, sizes, eps):
  X = []
  Y_methods = {}

  for name in names:
    Y_methods[name] = []

  print(exp_name)
  TOTAL_RUNS = len(sizes) * len(methods)
  RUN_COUNT = 0

  for n in sizes:
    G = graph_generator(n)
    X.append(n)

    for i, method in enumerate(methods):
      H = method(G, eps)
      val = eval_func(G, H)
      Y_methods[names[i]].append(val)

      RUN_COUNT+=1
      print(f"{RUN_COUNT}/{TOTAL_RUNS}", end="\r")

  experiment = {"X" : X, "Y": Y_methods}
  save(experiment, exp_name)