from Sparsifiers.effective_resistances import EffRes_Pinv, EffRes_SDDSolver
from Sparsifiers.approximate_matrix_multiplication import ApproxMatMult
from Sparsifiers.quantized_random import randQuant_Sparsify
from Sparsifiers.trace_reduction import TraceRed_Sparsify
from Sparsifiers.spanning_tree import spanTree_Sparsify

from SDDSolvers.spanning_tree_PCG import SpanTree_Solver

class MethodObj:
  def __init__(self, method, label, color):
    self.method = method
    self.label = label
    self.color = color


class MethodsMap:
  def __init__(self):
    self.methodsMap = {}

    EffRes = lambda G, eps : EffRes_SDDSolver(G, SpanTree_Solver, eps)

    self.methodsMap["RQS"] = MethodObj(randQuant_Sparsify, "Random Quantized Sampling", 'tab:blue')
    self.methodsMap["MM"] = MethodObj(ApproxMatMult, "Matrix Multiplication", 'tab:orange')
    self.methodsMap["TR"] = MethodObj(TraceRed_Sparsify, "Trace Reduction", 'tab:green')
    self.methodsMap["EFI"] = MethodObj(EffRes_Pinv, "Effective Resistances with Inverse", 'tab:red')
    self.methodsMap["EF"] = MethodObj(EffRes, "Effective Resistances", 'tab:purple')
    self.methodsMap["ST"] = MethodObj(spanTree_Sparsify, "Maximum Spanning Tree", 'tab:brown')

  def getMethod(self, code):
    return self.methodsMap[code].method
  
  def getLabel(self, code):
    return self.methodsMap[code].label
  
  def getColor(self, code):
    return self.methodsMap[code].color

MethodsMapObj = MethodsMap()

def getMethodsMap():
  return MethodsMapObj