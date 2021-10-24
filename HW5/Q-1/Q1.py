import numpy as np

C = [[5,8,1,2],
    [6,7,3,0],
    [4,5,9,1]]
def transpose_matrix(A):
    R = np.zeros((len(A[0]), len(A)))
    for i in range(len(A)):
        #rows
        for j in range(len(A[0])):
            #columns
            R[j][i] = A[i][j]
    return R

transpose_matrix(C)
