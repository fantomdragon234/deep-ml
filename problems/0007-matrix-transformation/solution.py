import numpy as np

def transform_matrix(A: list[list[int|float]], T: list[list[int|float]], S: list[list[int|float]]) -> list[list[int|float]]:

    if(np.linalg.det(T)!=0 and np.linalg.det(S)!=0):
        T_inverse=np.linalg.inv(T)
        A_new=T_inverse @ A @ S
    else:
        return "-1"
    return A_new.tolist()

