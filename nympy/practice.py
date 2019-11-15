import numpy as np

a = np.array([(1, 2, 3, 6, 9), (4, 5, 6, 6, 9)])
print(a.ndim)
print(a.size)
print(a.shape)
print(a[1, 2])
print(a[0:, 2])