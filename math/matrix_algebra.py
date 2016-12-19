# Matrix Algebra

import numpy as np

A = np.matrix([[1, 2, 3], [2, 7, 4]])
B = np.matrix([[1, -1], [0, 1]])
C = np.matrix([[5, -1], [9, 1], [6, 0]])
D = np.matrix([[3, -2, -1], [1, 2, 3]])
u = np.matrix([6, 2, -3, 5])
v = np.matrix([3, 5, -1, 4])
w = np.matrix([[1], [8], [0], [5]])
alpha = 6

# 1. Write the dimensions of each matrix
mat = [A, B, C, D, u, w]
for item in mat:
    dim = item.shape
    print "The dimensions of"
    print item, "are", dim[0], "x", dim[1], "\n"

# 2. Vector Operations
print "u + v =", u + v, "\n"
print "u - v =", u - v, "\n"
print "alpha * u =", alpha * u, "\n"
print "u * v =", np.dot(u, v.T), "(dot product)\n"
print "||u|| =", np.linalg.norm(u), "\n"

# 3. 
print "A + C is not defined\n" # A + C
print "A - C^T =", A - C.T, "\n"
print "C^T + 3D =", C.T + (3 * D), "\n"
print "BA =", np.matmul(B, A), "\n"
print "B(A^T) is not defined\n" # np.matmul(B, A.T)
print "BC is not defined\n" # np.matmul(B, C)
print "CB =", np.matmul(C, B), "\n"
print "B^4 =", np.linalg.matrix_power(B, 4), "\n"
print "A(A^T) =", np.matmul(A, A.T), "\n"
print "(D^T)D =", np.matmul(D.T, D), "\n"


