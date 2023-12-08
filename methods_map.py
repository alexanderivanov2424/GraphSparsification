from Sparsifiers.effective_resistances import EffRes_Pinv, EffRes_SDDSolver, EffRes_Pinv_Fixed, EffRes_SDDSolver_Fixed
from Sparsifiers.approximate_matrix_multiplication import ApproxMatMult, ApproxMatMult_Fixed
from Sparsifiers.quantized_random import randQuant_Sparsify, randQuant_Sparsify_Fixed
from Sparsifiers.trace_reduction import TraceRed_Sparsify, TraceRed_Sparsify_Fixed
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
    EffRes = lambda G : EffRes_SDDSolver(G, SpanTree_Solver)

    EffRes_Fixed = lambda G : EffRes_SDDSolver_Fixed(G, SpanTree_Solver)

    self.methodsMap["RQS"] = MethodObj(randQuant_Sparsify, "Random Quantized Sampling", 'tab:blue')
    self.methodsMap["MM"] = MethodObj(ApproxMatMult, "Matrix Multiplication", 'tab:orange')
    self.methodsMap["TR"] = MethodObj(TraceRed_Sparsify, "Trace Reduction", 'tab:green')
    self.methodsMap["ERI"] = MethodObj(EffRes_Pinv, "Effective Resistances with Inverse", 'tab:red')
    self.methodsMap["ER"] = MethodObj(EffRes, "Effective Resistances", 'tab:purple')
    self.methodsMap["ST"] = MethodObj(spanTree_Sparsify, "Maximum Spanning Tree", 'tab:brown')

    self.methodsMap["F_RQS"] = MethodObj(randQuant_Sparsify_Fixed, "Random Quantized Sampling", 'tab:blue')
    self.methodsMap["F_MM"] = MethodObj(ApproxMatMult_Fixed, "Matrix Multiplication", 'tab:orange')
    self.methodsMap["F_TR"] = MethodObj(TraceRed_Sparsify_Fixed, "Trace Reduction", 'tab:green')
    self.methodsMap["F_ERI"] = MethodObj(EffRes_Pinv_Fixed, "Effective Resistances with Inverse", 'tab:red')
    self.methodsMap["F_ER"] = MethodObj(EffRes_Fixed, "Effective Resistances", 'tab:purple')

  def getMethod(self, code):
    return self.methodsMap[code].method
  
  def getLabel(self, code):
    return self.methodsMap[code].label
  
  def getColor(self, code):
    return self.methodsMap[code].color

MethodsMapObj = MethodsMap()

def getMethodsMap():
  return MethodsMapObj