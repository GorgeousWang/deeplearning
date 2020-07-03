# Author:Elli
# 如何在python numpy中进行矩阵乘法
# random.randn函数用来产生随机数，这个函数的作用是从标准正态分布中
# 返回一个或多个样本值。如果没有参数，则返回一个值。如果有参数
# 则返回参数个值，参数应该是正整数，表示维度

import numpy as np
a = np.random.randn(12288, 150)  # a.shape = (12288,150)
b = np.random.randn(150, 45)  # b.shape = (150.45)

c = np.dot(a, b)  # 对a,b进行矩阵运算
print(c.shape)  # （12888， 45）




