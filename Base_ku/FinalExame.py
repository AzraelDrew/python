########################           第1题             ##########################

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.tree import DecisionTreeClassifier as DTC
data = pd.read_csv("./data/data.csv")
X = data.iloc[:, 1:]
print(X)
clf = KMeans(n_clusters=5)
y_pred = clf.fit_predict(X)
print(y_pred)
x = X.iloc[:, 0]
print(x)
y = X.iloc[:, 1]
print(y)
plt.scatter(x, y, c=y_pred, marker='o')
plt.title("Kmeans-Basketball Data")
plt.xlabel("assists_per_minute")
plt.ylabel("points_per_minute")
plt.legend(["Rank"])
plt.show()


########################           第2题             ##########################


filename = './data/sales_data.xls'
data = pd.read_excel(filename, index_col=u'序号')
data[data == u'好'] = 1
data[data == u'是'] = 1
data[data == u'高'] = 1
data[data != 1] = -1
x = data.iloc[:, :3].values.astype(int)
y = data.iloc[:, 3].values.astype(int)
dtc = DTC(criterion='entropy')
dtc.fit(x, y)
print(data.head())
