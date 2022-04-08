

# 代码 3-1
import pandas as pd
import numpy as np
print('通过ndarray创建的Series为：\n',
      pd.Series(np.arange(5), index=['a', 'b', 'c', 'd', 'e'], name='ndarray'))



# 代码 3-2
dit = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4}
print('通过dict创建的Series为：\n', pd.Series(dit))



# 代码 3-3
list1 = [0, 1, 2, 3, 4]
print('通过list创建的Series为：\n', pd.Series(list1, index=['a', 'b', 'c', 'd', 'e'], name='list'))



# 代码 3-4
series = pd.Series(list1, index=['a', 'b', 'c', 'd', 'e'], name='list')
print('数组形式返回Series为：', series.values)

print('Series的Index为：', series.index)

print('Series的形状为：', series.shape)

print('Series的维度为：', series.ndim)



# 代码 3-5
print('Series位于第1位置的数据为：', series[0])



# 代码 3-6
print('Series中Index为a的数据为：', series['a'])



# 代码 3-7
bool = (series < 4)
print('bool类型的Series为：\n', bool)

print('通过bool访问Series结果为：\n', series[bool])



# 代码 3-8
# 更新元素
series['a'] = 3
print('更新后的Series为：\n', series)



# 代码 3-9
series1 = pd.Series([4, 5], index=['f', 'g'])
# 追加Series
print('在series插入series1后为：\n', series.append(series1))

# 新增单个数据
series1['h'] = 7
print('在series1插入单个数据后为：\n', series1)



# 代码 3-10
# 删除数据
series.drop('e', inplace=True)
print('删除索引e对应数据后的series为：\n', series)



# 代码 3-11
dict1 = {'col1': [0, 1, 2, 3, 4], 'col2': [5, 6, 7, 8, 9]}
print('通过dict创建的DataFrame为：\n', pd.DataFrame(dict1, index=['a', 'b', 'c', 'd', 'e']))



# 代码 3-12
list2 = [[0, 5], [1, 6], [2, 7], [3, 8], [4, 9]]
print('通过list创建的DataFrame为：\n',
      pd.DataFrame(list2, index=['a', 'b', 'c', 'd', 'e'], columns=['col1', 'col2']))



# 代码 3-13
df = pd.DataFrame({'col1': [0, 1, 2, 3, 4], 'col2': [5, 6, 7, 8, 9]},
                  index=['a', 'b', 'c', 'd', 'e'])
print('DataFrame的Index为：', df.index)

print('DataFrame的列标签为：', df.columns)

print('DataFrame的轴标签为：', df.axes)

print('DataFrame的维度为：', df.ndim)

print('DataFrame的形状为：', df.shape)



# 代码 3-14
print('默认返回前5行数据为：\n', df.head())

print('返回后3行数据为：\n', df.tail(3))



# 代码 3-15
# 更新列
df['col1'] = [10, 11, 12, 13, 14]
print('更新列后的DataFrame为：\n', df)



# 代码 3-16
# 插入列
df['col3'] = [15, 16, 17, 18, 19]
print('插入列后的DataFrame为：\n', df)



# 代码 3-17
# 删除列
df.drop(['col3'], axis=1, inplace=True)
print('删除col3列后的DataFrame为：\n', df)

# 删除行
df.drop('a', axis=0, inplace=True)
print('删除a行后的DataFrame为：\n', df)



# 代码 3-18
print('series的Index为 ：\n', series.index)



# 代码 3-19
print('series中Index各元素是否大于前一个：', series.index.is_monotonic)

print('series中Index各元素是否唯一：', series.index.is_unique)



# 代码 3-20
index1 = series.index
index2 = series1.index
print('index1连接index2后结果为：\n', index1.append(index2))

print('index1与index2的差集为：', index1.difference(index2))

print('index1与index2的交集为：', index1.intersection(index2))

print('index1与index2的并集为：\n', index1.union(index2))

print('index1中的元素是否在index2中：', index1.isin(index2))



# 代码 3-21
df = pd.DataFrame({'col1': [0, 1, 2, 3, 4], 'col2': [5, 6, 7, 8, 9]},
                  index=['a', 'b', 'c', 'd', 'e'])
print('创建的DataFrame为：\n', df)

# 访问单列数据
print('DataFrame中col1列数据为：\n', df['col1'])



# 代码 3-22
# 以属性的方式访问单列数据
print('DataFrame中col1列数据为：\n', df.col1)



# 代码 3-23
# 访问单列多行数据
print('DataFrame中col1列前3行数据为：\n', df['col1'][0: 3])



# 代码 3-24
# 访问多列多行数据
print('DataFrame中col1列、col2列前3行数据为：\n', df[['col1', 'col2']][0: 3])



# 代码 3-25
# 访问多行数据
print('DataFrame的前3行为：\n', df[:][0: 3])



# 代码 3-26
# 访问单列数据
print('DataFrame中col1列数据为：\n', df.loc[:, 'col1'])

# 访问多列数据
print('DataFrame中col1列、col2数据为：\n', df.loc[:, ['col1', 'col2']])

# 访问单行数据
print('DataFrame中a行对应数据为：\n', df.loc['a', :])

# 访问多行数据
print('DataFrame中a行、b行对应数据为：\n', df.loc[['a', 'b'], :])

# 行列结合访问数据
print('DataFrame中a行、b行，col1列、col2列对应的数据为：\n',
      df.loc[['a', 'b'], ['col1', 'col2']])



# 代码 3-27
# 接收bool数据
print('DataFrame中col1列大于0的数据为：\n', df.loc[df['col1'] > 0, :])

# 接收函数
print('DataFrame中col1列大于0的数据为：\n', df.loc[lambda df: df['col1'] > 0, :])



# 代码 3-28
# 访问单列数据
print('DataFrame中col1列数据为：\n', df.iloc[:, 0])

# 访问多列数据
print('DataFrame中col1列、col2列数据为：\n', df.iloc[:, [0, 1]])

# 访问单行数据
print('DataFrame中a行数据为：\n', df.iloc[0, :])

# 访问多行数据
print('DataFrame中a行、b行数据为：\n', df.iloc[[0, 1], :])

# 行列结合访问数据
print('DataFrame中a行、b行，col1列、col2列数据为：\n', df.iloc[[0, 1], [0, 1]])



# 代码 3-29
# 接收bool数据
print('DataFrame中col1列大于0的数据为：\n', df.iloc[df['col1'].values > 0, :])

# 接收函数
print('DataFrame中col1列大于0的数据为：\n', df.iloc[lambda df: df['col1'].values > 0, :])



# 代码 3-30
# 按行索引排序
print('按行索引排序后的DataFrame为：\n', df.sort_index(axis=0))



# 代码 3-31
# 按列索引降序排列
print('按列索引降序排列后的DataFrame为：\n', df.sort_index(axis=1, ascending=False))



# 代码 3-32
# 按列排序
print('按col2列排序后的DataFrame为：\n', df.sort_values('col2'))



# 代码 3-33
# 按行降序排列
print('按列降序排列后的DataFrame为：\n', df.sort_values('a', axis=1, ascending=False))



# 代码 3-34
print('按col2列排序,返回前2个最小值：\n', df.nsmallest(2, 'col2'))

print('按col2列排序,返回前2个最大值：\n', df.nlargest(2, 'col2'))



# 代码 3-35
df2 = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3', 'K4', 'K5'],
                    'A': ['A0', 'A1', 'A2', 'A3', 'A4', 'A5']})
df3 = pd.DataFrame({'key': ['K0', 'K1', 'K2'], 'B': ['B0', 'B1', 'B2']})
# 横向堆叠df2、df3
print('横向堆叠df2、df3后的DataFrame为：\n', pd.concat([df2, df3], axis=1))

# 横向堆叠（内连）df2、df3
print('横向堆叠（内连）df2、df3后的DataFrame为：\n',
      pd.concat([df2, df3], axis=1, join='inner'))



# 代码 3-36
print('横向堆叠df2、df3后的DataFrame为：\n', df2.join(df3, rsuffix='_2'))



# 代码 3-37
# 纵向堆叠df2、df3
print('纵向堆叠df2、df3后的DataFrame为：\n', pd.concat([df2, df3], axis=0))

# 纵向堆叠（内连）df2、df3
print('纵向堆叠（内连）df2、df3后的DataFrame为：\n',
      pd.concat([df2, df3], axis=0, join='inner'))



# 代码 3-38
print('纵向堆叠df2、df3后的DataFrame为：\n', df2.append(df3))



# 代码 3-39
print('以列key为键，内连df2、df3后的DataFrame为：\n',
      pd.merge(df2, df3, on='key', how='inner'))
