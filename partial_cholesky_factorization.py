import numpy as np

"""
Incomplete Cholesky factorization
https://en.wikipedia.org/wiki/Incomplete_Cholesky_factorization
"""

def icholesky(A):
    n = A.shape[0]
    for k in range(n): 
        A[k,k] = np.sqrt(A[k,k])
        non_zero = A[k+1:,k].nonzero()[0] + (k+1)
        if len(non_zero) > 0:
            A[non_zero,k] = A[non_zero,k]/A[k,k]
        for j in non_zero: 
            non_zero2 = A[j:n,j].nonzero()[0] + j
            if len(non_zero2) > 0:
                A[non_zero2,j]  = A[non_zero2,j] - A[non_zero2,k]*A[j,k]
    return A