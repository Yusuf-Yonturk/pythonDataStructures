import numpy as np

a = [[11, 12, 13], [21, 22, 23], [31, 32, 33]]

print(a)

A=np.array(a)

print(A)

print(A.ndim)

print(A.shape)

print(A.size)

print(A[1,2])

print(A[1][2])

print(A[0][0])

print(A[0][0:2])

print(A[0:2,2])

X=np.array([[1,0],[0,1]])

print(X)

Y = np.array([[2, 1], [1, 2]]) 

print(Y)

Z=X+Y

print(Z)

Y = np.array([[2, 1], [1, 2]]) 

print(Y)

Z=2*Y

print(Z)

Y = np.array([[2, 1], [1, 2]])

X = np.array([[1, 0], [0, 1]]) 

Z = X*Y

print(Z)

A = np.array([[0, 1, 1], [1, 0, 1]])

B = np.array([[1, 1], [1, 1], [-1, 1]])

Z = np.dot(A,B)

print(Z)

print(np.sin(Z))

C = np.array([[1,1],[2,2],[3,3]])

print(C.T)

a = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]