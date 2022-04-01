import numpy as np

arr = np.arange(16).reshape(4,4)
#print(arr)
c = np.hsplit(arr,2)
#print("横向分割:",c)
d = np.vsplit(arr,2)
print("纵向分割:",d)

e = np.split(arr,2,axis = 1) #当axis的参数为1时，为横向分割
print("多了axis的横向分割:",e)

f = np.split(arr,2,axis = 0)#当axi的参数为0时，为纵向分割
print("多了axis的纵向分割:",f)

#创建三维数组
arr1 = np.arange(12).reshape(2,2,3)
print(arr1)

g = np.dsplit(arr1,3)
print("深度分割:",g)

#使用sort函数进行排序
np.random.seed(42)
arr = np.random.randint(1,10,size = 12).reshape(4,3)
#print(arr)
print("默认排序后的为:\n",np.sort(arr))
print("展平后的排序:\n",np.sort(arr,axis = None))
print("横轴排序后:\n",np.sort(arr,axis = 1))
print("纵轴后的排序:\n",np.sort(arr,axis = 0))

#使用argsort函数进行排序
print("横轴排序后的下标为:\n",np.argsort(arr,axis = 1))

#使用argmax函数找出最大索引
arr = np.arange(12).reshape(4,3)
arr1 = np.arange(-12,0).reshape(4,3)
print(arr)
print(np.argmax(arr))
print(np.argmin(arr))
print(np.where(arr>=6))

#arr中大于5的数
exp = arr> 5
print(exp)

#使用where函数搜索满足的条件
print(np.where(exp,arr,arr1))

arr = np.arange(9).reshape(3,3)
exp = (arr % 2)==0
print(exp)
print("提取出满足exp的数值:\n",np.extract(exp,arr))

a = 10
b = 20
if a<b:
    print("a是猪")
else:
    print("b是猪")


for i in range(10):
    print("肖总是猪")
