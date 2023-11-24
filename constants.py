



class Constants:
  def __init__(self):
    self.epsilon = .1 # accuracy bound for spectral sparcifier


    self.EffRes_C = 1

    self.ApproxMatMult_delta = .1 # probability to NOT obtain epsilon close sparsification

    self.TraceRed_alpha = .1 # fraction of number of nodes for number of edges to recover
    self.TraceRed_Nr = 5 # number of edges to recover in each itteration
    self.TraceRed_delta = .1 # parameter delta for Sparse Approximate Inverse of the Cholesky Factor
    self.TraceRed_beta = 5 #size of neiborhood for trace reduction calculation
    self.TraceRed_eps = .1 #epsilon bound for marking simlar edges

ConstObj = Constants()

def getConstObj():
  return ConstObj