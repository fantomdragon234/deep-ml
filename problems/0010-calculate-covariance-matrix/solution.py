def calculate_covariance_matrix(vectors: list[list[float]]) -> list[list[float]]:
    import numpy as np
    return np.cov(vectors).tolist()