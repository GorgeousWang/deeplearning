# Author:Elli


# a.shape = (3,4)
# a.shape = (4,1)

import numpy as np

a = np.random.randn(3, 4)
b = np.random.randn(4, 1)
c = np.random.randn(3, 4)
# for i in range(3):
#     for j in range(4):
#         c[i][j] = a[i][j] +b[j]
# print(c)


# 向量化
c = a + b.T
print(c)

