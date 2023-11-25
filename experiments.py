import numpy as np
import time
import networkx as nx

from utils import save, load, exists
from evaluators import *


def fix_keys(experiment_data):
  for name in experiment_data:
    fixed = {}
    for key in experiment_data[name]:
      try:
        fixed[int(key)] = experiment_data[name][key]
      except:
        fixed[float(key)] = experiment_data[name][key]
    experiment_data[name] = fixed

def parse_experiment_data(experiment_data):
  X = []
  Y_methods = {}
  for name in experiment_data.keys():
    data = experiment_data[name]
    for x in data.keys():
      X.append(x)
  X.sort()
  for name in experiment_data.keys():
    Y_methods[name] = [experiment_data[name][x] for x in X]
  return X, Y_methods

def runtime_comparison(exp_name, names, methods, graph_generator, sizes, eps):
  experiment_data = {} # { method -> { x -> y } }
  
  if exists(exp_name):
    experiment_data = load(exp_name)
    fix_keys(experiment_data)
  
  for name in names:
    if not name in experiment_data:
      experiment_data[name] = {}

  print(exp_name)
  TOTAL_RUNS = len(sizes) * len(methods)
  RUN_COUNT = 0

  for n in sizes:
    G = graph_generator(n)

    for i, method in enumerate(methods):
      RUN_COUNT+=1
      print(f"{RUN_COUNT}/{TOTAL_RUNS}  {names[i]}", end="\r")

      if n in experiment_data.get(names[i], {}):
        continue
      t, _ = time_method(method, (G, eps))
      experiment_data[names[i]][n] = t

      save(experiment_data, exp_name)


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
  experiment_data = {} # { method -> { x -> y } }
  
  if exists(exp_name):
    experiment_data = load(exp_name)
    fix_keys(experiment_data)
  
  for name in names:
    if not name in experiment_data:
      experiment_data[name] = {}

  print(exp_name)
  TOTAL_RUNS = len(sizes) * len(methods)
  RUN_COUNT = 0

  for n in sizes:
    G = graph_generator(n)
    
    for i, method in enumerate(methods):
      RUN_COUNT+=1
      print(f"{RUN_COUNT}/{TOTAL_RUNS}  {names[i]}", end="\r")

      if n in experiment_data.get(names[i], {}):
        continue
      H = method(G, eps)
      val = eval_func(G, H)
      experiment_data[names[i]][n] = val

      save(experiment_data, exp_name)