import numpy as np

# def make_diagonal(v):
#     """
#     Returns: (n, n) NumPy array with v on the main diagonal
#     """
#     v = np.array(v)
#     n =  len(v)
#     diagonal_matrix = np.zeros((n,n))
#     for i in range(len(diagonal_matrix)):
#         for j in range(n):
#             if i == j:
#                 diagonal_matrix[i][j] = v[j]
#     return diagonal_matrix

def make_diagonal(v):
    """
    Returns: (n, n) NumPy array with v on the main diagonal
    """
    return np.diag(v)
    