import numpy as np
print("整数42转换为浮点数的结果为:",np.float64(42))
print("浮点数42.0转换为整数的结果为:",np.int8(42.0))
print("浮点数42.0转换为布尔的结果为:",np.bool_(42.0))
print("整数0转换为布尔的结果为:",np.bool_(0))
print("布尔True转换为浮点数的结果为:",np.float64(True))
print("布尔False转换为整数的结果为:",np.int8(False))


arr1 =  np.array([1,2,3,4])
print("创建的一维数组nparray数组为:",arr1)
arr2 =  np.array([[1,2,3,4],[4,5,6,7],[7,8,9,10]])
print("创建的二维数组nparray数组为:\n",arr2)
print("ndaray arr2的维数为:",arr2.ndim)
print("ndaray arr2的形状为:",arr2.shape)
print("ndaray arr2的数据类型为:",arr2.dtype)
print("ndaray arr2的元素个数为:",arr2.size)
print("ndaray arr2的每个元素的大小为:",arr2.itemsize)



print("使用arange函数创建的ndarray为:\n",np.arange(0,1,0.1))
print("使用linspe函数创建的ndarray为:\n",np.linspace(0,1,12))
print("使用zeros函数创建的ndarray为:\n",np.zeros((2,3)))
print("使用eye函数创建的ndarray为:\n",np.eye(3))
print("使用diag函数创建的ndarray为:\n",np.diag([1,2,3,4]))
print("使用ones函数创建的ndarray为:\n",np.ones((2,3)))



print("random函数生成的随机数为:\n",np.random.random(100))
print("rand函数生成的随机数为:\n",np.random.rand(4,5))
print("randint函数生成的随机数为:\n",np.random.randint(low=2,high=10,size=[2,5]))


arr3 = np.arange(10)
print(arr3)
print("使用元素位置索引结果为:",arr3[0])
print("使用元素位置切片结果为:",arr3[3:5])
print("省略单个位置切片结果为:",arr3[:5])
print("反向切片结果为:",arr3[:-1])
arr3[2:4] = 100,101
print("修改后的结果为:",arr3)
print("元素位置等差索引的结果为:",arr3[1:-1:2])
print("元素位置负数步长等差索引的结果为:",arr3[5:1:-2])


arr4 = np.arrange(15).reshape(3,5)
