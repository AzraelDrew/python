import numpy as np
import random as rm
# a = np.arange(15).reshape(3,5)
# # 基础
# print(a)
# print(a.shape)   #尺寸
# print(a.ndim)    #轴数
# print(a.size)    #元素总数
# print(a.dtype)   #int32
# print(a.itemsize)  #数组中每个元素的大小(以字节为单位)
# print(a.data)  #包含数组实际元素的缓冲区。通常，我们不需要使用此属性，因为我们将使用索引工具访问数组中的元素


# # 阵列创建
# #1.一维
# b1= np.array([2,3,4])
# print(b1)
# print(a.dtype)  #int32
# b2 = np.array([1.2,3.5,5.1])
# print(b2)
# print(b2.dtype)  #float64
#
# # b3 = np.array(1,2,3,4)
# # print(b3)
#
# b4 =np.array([1,2,3,4,5])
# print(b4)
#
#
# #2.二维
# c1 = np.array([(1,2,3,4),(5,5,6,7,8)])
# print(c1)
# c2 =np.array([[1,2],[3,4]],dtype=complex)   #指定类型
# print(c2)



# print(np.zeros((3,4)))  #全为0
# print(np.ones((2,3,4)))  #全为1
# print(np.empty((2,3)))  #随机
# print(np.arange(10,30,5))  #创建其初始内容是随机的并取决于内存状态的数组。默认情况下，创建的数组的dtype为 float64
print(rm.random())  #随机生成0-1之间的数