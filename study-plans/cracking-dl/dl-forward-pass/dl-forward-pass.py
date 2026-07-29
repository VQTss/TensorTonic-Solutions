import numpy as np


def forward_pass(x, weights, bias):
    """
    Returns a dictionary containing activations and
    pre-activations, rounded to 4 decimal places.
    """

    current = np.asarray(x, dtype=float)

    activations = [
        [round(float(value), 4) for value in current]
    ]
    pre_activations = []

    for layer_index in range(len(weights)):
        weight = np.asarray(weights[layer_index], dtype=float)
        layer_bias = np.asarray(bias[layer_index], dtype=float)

        # z = Wx + b
        z = weight @ current + layer_bias

        pre_activations.append(
            [round(float(value), 4) for value in z]
        )

        # ReLU cho lớp ẩn, không kích hoạt ở lớp cuối
        if layer_index < len(weights) - 1:
            current = np.maximum(0, z)
        else:
            current = z

        activations.append(
            [round(float(value), 4) for value in current]
        )

    return {
        "activations": activations,
        "pre_activations": pre_activations
    }