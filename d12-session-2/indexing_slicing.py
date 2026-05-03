import numpy as np

b = np.array([[1, 2, 3],
              [4, 5, 6]])

print(b[0])         # [1 2 3]   — first row
print(b[1, 2])      # 6         — row 1, col 2
print(b[:, 0])      # [1 4]     — first column
print(b[0:2, 1:3])  # [[2 3], [5 6]]   — sub-matrix
print(b[b > 3])     # [4 5 6]   — boolean filter
