def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:
    import numpy as np

    trace=np.trace(matrix)
    det = np.linalg.det(matrix)
    coefficients = [1,-trace, det]
    eigenvalues = np.roots(coefficients)

    return eigenvalues

