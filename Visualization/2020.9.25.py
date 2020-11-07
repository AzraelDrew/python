'''
 $ @Author       : yznaisy
 $ @Date         : 2020-09-25 09:40:53
 $ @LastEditors  : yznaisy
 $ @LastEditTime : 2020-10-16 11:30:06
'''
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

plt.figure(figsize=(8, 8), dpi=80)
# 创建第一个画板
plt.figure(1)
# 将第一个画板划分为2行1列组成的区块，并获取到第一块区域
ax1 = plt.subplot(221)
# 在第一个子区域中绘图
plt.axis([1, 10, 2, 20])
ax1.annotate("(4,10)", (4, 16))
plt.plot([1, 2, 3, 4], [1, 4, 9, 16])

ac = plt.gca()
ac.spines['right'].set_color(None)
ac.spines['top'].set_color(None)

# 选中第二个子区域，并绘图
ax2 = plt.subplot(222)

labels = ['一月', '二月', '三月']
exports = [500, 900, 1000]
imports = [600, 700, 800]

x = np.arange(len(labels))  # the label locations
width = 0.3  # the width of the bars

rects1 = ax2.bar(x - width/2, exports, width, label='出口')
rects2 = ax2.bar(x + width/2, imports, width, label='进口')

# ax2.set_ylabel('进出口额/亿美元')
# ax2.set_xlabel("第一季度/月")
# ax2.set_title('第一季度进口出口数据')
# ax2.set_xticks(x)
ax2.legend(loc="upper left")


def autolabel(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax2.annotate('{}'.format(height),
                     xy=(rect.get_x() + rect.get_width() / 2, height),
                     xytext=(0, 3),  # 3 points vertical offset
                     textcoords="offset points",
                     ha='center', va='bottom')


autolabel(rects1)
autolabel(rects2)

ac = plt.gca()
ac.spines['right'].set_color(None)
ac.spines['top'].set_color(None)
ax3 = plt.subplot(212)
# 折线
line1 = plt.plot(["一月", "二月", "三月"], [400, 200, 900])
# 柱状图
labels = ['一月', '二月', '三月']
exports = [500, 900, 1000]
imports = [600, 700, 800]

x = np.arange(len(labels))  # the label locations
width = 0.1  # the width of the bars

rects1 = ax3.bar(x - width/2, exports, width, label='出口')
rects2 = ax3.bar(x + width/2, imports, width, label='进口')

ax3.set_ylabel('进出口额/亿美元')
ax3.set_xlabel("第一季度/月")
ax3.set_title('第一季度进口出口数据')
ax3.legend()


def autolabel1(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax3.annotate('{}'.format(height),
                     xy=(rect.get_x() + rect.get_width() / 2, height),
                     xytext=(0, 3),  # 3 points vertical offset
                     textcoords="offset points",
                     ha='center', va='bottom')


# 给柱状图添加数据
autolabel1(rects1)
autolabel1(rects2)


# 调整每隔子图之间的距离
plt.tight_layout()

ac = plt.gca()
ac.spines['right'].set_color(None)
ac.spines['top'].set_color(None)
plt.show()
