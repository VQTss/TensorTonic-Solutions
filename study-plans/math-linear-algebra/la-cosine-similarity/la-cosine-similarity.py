import numpy as np

def cosine_similarity(a, b):
    """
    Returns: float in [-1, 1], cosine similarity between a and b.
    """
    a = np.asarray(a,dtype=float)
    b = np.asarray(b,dtype=float)
    dot = np.dot(a,b)
    normA = np.linalg.norm(a)
    normB = np.linalg.norm(b)
    if normA < 1e-10 or normB < 1e-10:
        return 0.0
    return float(dot / (normA * normB))