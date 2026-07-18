import numpy as np

def solve_linear_system(A, b):
    """
    Returns: float64 array, the solution x to A @ x = b.
    """
    A = np.asarray(A,dtype=float)
    b = np.asarray(b,dtype=float)
    result = np.linalg.solve(A,b)
    return result