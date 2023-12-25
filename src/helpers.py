import numpy as np

null_value = 0


allowed_values = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def is_wrong(cell_block: np.ndarray):
    non_null_values = [
        value for value
        in cell_block
        if value != null_value
    ]

    return len(set(non_null_values)) != len(non_null_values)
