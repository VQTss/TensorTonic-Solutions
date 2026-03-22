import numpy as np

def cosine_similarity(a, b):
    """
    Compute cosine similarity between two 1D NumPy arrays.
    Returns: float in [-1, 1]
    """
    a = np.array(a)
    b = np.array(b)
    dot = np.dot(a,b)
    norms_a = np.linalg.norm(a)
    norms_b = np.linalg.norm(b)
    if norms_a == 0 or norms_b == 0:
        return 0
    euclidean_norm =  norms_a * norms_b
    return dot / euclidean_norm