# Author:Elli

import numpy as np
import matplotlib.pyplot as plt
# 直接使用plt.imshow无法显示图片，需要导入pylab包
import pylab
import h5py
from lr_utils import load_dataset

train_set_x_orig , train_set_y , test_set_x_orig , test_set_y , classes = load_dataset()

index = 25
#plt.figure()
#plt.imshow(train_set_x_orig[index])
#plt.figure()
#plt.imshow(train_set_x_orig[26])
# plt.show()

# print("train_set_y=" + str(train_set_y)) #你也可以看一下训练集里面的标签是什么样的。
#打印出当前的训练标签值
#使用np.squeeze的目的是压缩维度，【未压缩】train_set_y[:,index]的值为[1] , 【压缩后】np.squeeze(train_set_y[:,index])的值为1
#print("【使用np.squeeze：" + str(np.squeeze(train_set_y[:,index])) + "，不使用np.squeeze： " + str(train_set_y[:,index]) + "】")
#只有压缩后的值才能进行解码操作
print("y=" + str(train_set_y[:,index]) + ", it's a " + classes[np.squeeze(train_set_y[:,index])].decode("utf-8") + "' picture")






