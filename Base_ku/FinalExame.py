########################           第1题             ##########################

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.tree import DecisionTreeClassifier as DTC
# 读取数据
data = pd.read_csv("./data/data.csv")
X = data.iloc[:, 1:]
print(X)

# K-means聚类
clf = KMeans(n_clusters=5)  # 表示输出将数据集分成类簇数为5的聚类
# 输出聚类预测结果，对X聚类，20行数据，每个y_pred对应X的一行或一个孩子，聚成3类，类标为0、1、2
y_pred = clf.fit_predict(X)
print(y_pred)  # 输出结果

x = X.iloc[:, 0]  # 获取第1列的值
print(x)
y = X.iloc[:, 1]  # 获取第2列的值
print(y)

# 可视化操作
# 绘制散点图（scatter），横轴为x，获取的第1列数据；纵轴为y，获取的第2列数据；
# c=y_pred对聚类的预测结果画出散点图，marker='o'说明用点表示图形
plt.scatter(x, y, c=y_pred, marker='o')
plt.title("Kmeans-Basketball Data")  # 表示图形的标题为Kmeans-heightweight Data
plt.xlabel("assists_per_minute")  # 表示图形x轴的标题
plt.ylabel("points_per_minute")  # 表示图形y轴的标题
plt.legend(["Rank"])  # 设置右上角图例
plt.show()  # 显示图形


########################           第2题             ##########################


# 参数初始化
filename = './data/sales_data.xls'
data = pd.read_excel(filename, index_col=u'序号')  # 导入数据

# 数据是类别标签，要将它转换为数据
# 用1来表示“好”“是”“高”这三个属性，用-1来表示“坏”“否”“低”
data[data == u'好'] = 1
data[data == u'是'] = 1
data[data == u'高'] = 1
data[data != 1] = -1
x = data.iloc[:, :3].values.astype(int)
y = data.iloc[:, 3].values.astype(int)

dtc = DTC(criterion='entropy')  # 建立决策树模型，基于信息熵
dtc.fit(x, y)  # 训练模型
print(data.head())
