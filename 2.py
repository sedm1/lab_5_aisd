import numpy as np
def strassen_multiply(A, B):
    if len(A) == 1:
        return A * B
    n = len(A) // 2
    A11 = A[:n, :n]
    A12 = A[:n, n:]
    A21 = A[n:, :n]
    A22 = A[n:, n:]
    B11 = B[:n, :n]
    B12 = B[:n, n:]
    B21 = B[n:, :n]
    B22 = B[n:, n:]
    P1 = strassen_multiply(A11 + A22, B11 + B22)
    P2 = strassen_multiply(A21 + A22, B11)
    P3 = strassen_multiply(A11, B12 - B22)
    P4 = strassen_multiply(A22, B21 - B11)
    P5 = strassen_multiply(A11 + A12, B22)
    P6 = strassen_multiply(A21 - A11, B11 + B12)
    P7 = strassen_multiply(A12 - A22, B21 + B22)
    C11 = P1 + P4 - P5 + P7
    C12 = P3 + P5
    C21 = P2 + P4
    C22 = P1 - P2 + P3 + P6
    C = np.zeros_like(A)
    C[:n, :n] = C11
    C[:n, n:] = C12
    C[n:, :n] = C21
    C[n:, n:] = C22
    return C
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
result = strassen_multiply(A, B)
print(result)