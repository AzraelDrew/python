'''
 $ @Author       : yznaisy
 $ @Date         : 2020-10-09 10:27:05
 $ @LastEditors  : yznaisy
 $ @LastEditTime : 2020-10-16 11:20:02
'''
from matplotlib.font_manager import FontProperties
import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cbook as cbook


plt.figure(1)
ax1 = plt.subplot2grid((4, 2), (0, 0))
plt.plot([1, 3, 5], [2, 4, 5])


ax2 = plt.subplot2grid((4, 2), (0, 1))
x = np.arange(4)
y = np.array([15, 20, 18, 25])
bar1 = plt.bar(x, y, width=0.3)
ax3 = plt.subplot2grid((4, 2), (1, 0), colspan=2)
x = np.arange(4)
y = np.array([15, 20, 18, 25])
line1 = plt.plot([1, 3, 5], [2, 4, 5])
bar1 = plt.bar(x, y, width=0.3)

ax4 = plt.subplot2grid((4, 2), (2, 0))
N = 45
x, y = np.random.rand(2, N)
c = np.random.randint(1, 5, size=N)
s = np.random.randint(10, 220, size=N)


scatter = ax4.scatter(x, y, c=c, s=s)

# # produce a legend with the unique colors from the scatter
# legend1 = ax4.legend(*scatter.legend_elements(),
#                      loc="lower left", title="Classes")
# # ax4.add_artist(legend1)

# # produce a legend with a cross section of sizes from the scatter
# handles, labels = scatter.legend_elements(prop="sizes", alpha=0.6)
# legend2 = ax4.legend(handles, labels, loc="upper right", title="Sizes")
ax5 = plt.subplot2grid((4, 2), (2, 1))
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.xlabel("123")
labels = ['娱乐', '育儿', '饮食', '房贷', '交通', '其它']
sizes = [12, 15, 12, 50, 2, 9]
explode = (0, 0, 0, 0, 0, 0)
plt.pie(sizes, explode=explode, labels=labels,
        autopct='%1.1f%%', shadow=False, startangle=150)
ax6 = plt.subplot2grid((4, 2), (3, 0), colspan=2)
np.random.seed(19680801)

# example data
mu = 100  # mean of distribution
sigma = 15  # standard deviation of distribution
x = mu + sigma * np.random.randn(437)

num_bins = 50


# the histogram of the data
n, bins, patches = ax6.hist(x, num_bins, density=True)

# add a 'best fit' line
y = ((1 / (np.sqrt(2 * np.pi) * sigma)) *
     np.exp(-0.5 * (1 / sigma * (bins - mu))**2))
ax6.plot(bins, y, '--')
plt.show()
