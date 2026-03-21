import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    A = np.array(A)    
    i = len(A)
    j = len(A[0])
    A_transpose = np.zeros((j,i))
    for n in range(i):
        for m in range(j):
            A_transpose[m][n] = A[n][m]
    return A_transpose