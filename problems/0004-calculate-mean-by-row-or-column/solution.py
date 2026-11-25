def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
    import numpy as np
    matrix_arr=np.array(matrix)
    if (mode=="column"):
        return np.mean(matrix_arr,axis=0).tolist()
    elif (mode=="row"):
        return np.mean(matrix_arr,axis=1).tolist()

    

