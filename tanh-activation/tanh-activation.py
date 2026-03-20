import numpy as np

def tanh(x):
    """
    Implement Tanh activation function.
    """
    x = np.array(x,dtype=float)
    result =  (np.exp(x) - np.exp(-x)) / (np.exp(x) + np.exp(-x))

    return result
