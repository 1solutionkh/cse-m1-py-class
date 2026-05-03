import numpy as np


# 3D array (tensor)
c = np.array([[[1, 2], [3, 4]],
              [[5, 6], [7, 8]]])
print(c.shape)   # (2, 2, 2)
print(c.ndim)    # 3
print(c.dtype)   # int64
