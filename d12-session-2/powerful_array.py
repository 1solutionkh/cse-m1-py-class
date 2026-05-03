
import numpy as np

a = np.array([1, 2, 3, 4])
b = np.array([10, 20, 30, 40])

print(a + b)        # [11 22 33 44]  — element-wise
print(a * b)        # [10 40 90 160]
print(a ** 2)       # [1 4 9 16]
print(a > 2)        # [False False True True]
