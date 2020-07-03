# Author:Elli

import numpy as np

a = np.random.randn(4, 3)  # a.shape (4, 3)表示这是一个4×3数组
b = np.random.randn(3, 2)  # b.shape(3, 2) 表示这是一个3×2数组


# c = a * b
#  *表示矩阵对应元素相乘，必须维数相同，行列都相同

c = np.random.randn(4, 3)
d = a * c

print(d)