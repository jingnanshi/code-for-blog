from sympy import Matrix

M = Matrix([[2, 3, -1, 0], [1, 1, 0, 1], [1, 0, 1, 3]])
print("Matrix : {} ".format(M))

M_rref = M.rref()
print(f"Reduced Row Echelon Form: {M_rref[0]}")
