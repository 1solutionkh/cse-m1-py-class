import numpy as np

a = np.array([1, 2, 3, 4])
b = np.array([10, 20, 30, 40])

print(a + b)        # [11 22 33 44]
print(a * 2)        # [2 4 6 8]
print(a.mean())     # 2.5
print(a.reshape(2, 2))
print(np.ndim(a), np.ndim(b))         # 1
# [[1 2]
#  [3 4]]
