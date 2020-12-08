
from pyecharts.charts import Pie
from pyecharts import options as opts
import pandas as pd

# Pie = pd.read_csv("./pie.csv", header=None)
# list2 = Pie.values.tolist()

# pie_name = []
# pie_data = []

# for pie in list2:
#     pie_name.append(pie[1])
#     pie_data.append(pie[2])

# pie_name.remove("Label")
# # print(pie_name)
# pie_data.remove("Values")
# # print(pie_data)

# c = (
#     Pie()
#     # rosetype="radius"   以半径的大小来展示数据的大小  有'radius'和'area'两种模式
#     # radius=["30%", "5%"]   饼图的半径，数组的第一项是内半径，第二项是外半径
#     #  饼图的中心（圆心）坐标，数组的第一项是横坐标，第二项是纵坐标
#     .add("", [list(i) for i in zip(pie_name, pie_data)],
#          rosetype="radius", radius=["10%", "50%"], center=["80%", "50%"],
#          label_opts=opts.LabelOpts(formatter="{b}\n{d}%"),
#          )

#     .set_colors(["#2ecc71", "#2980b9", "#e74c3c", "#8e44ad", "#2c3e50"])
#     .set_global_opts(title_opts=opts.TitleOpts(title="pie"))
#     # 饼图、仪表盘、漏斗图: {a}（系列名称），{b}（数据项名称），{c}（数值）, {d}（百分比）
#     #  .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}:{d}%"))
#     .render("pie.html")
# )

data = ["哈士奇", "泰迪", "金毛", "牧羊犬", "柯基"]
value = [54, 67, 68, 34, 56]
value1 = [241, 671, 418, 334, 256]

c = (
    Pie(init_opts=opts.InitOpts(height="90vh", width="90vw"))
    # rosetype="radius"   以半径的大小来展示数据的大小  有'radius'和'area'两种模式
    # radius=["30%", "5%"]   饼图的半径，数组的第一项是内半径，第二项是外半径
    #  饼图的中心（圆心）坐标，数组的第一项是横坐标，第二项是纵坐标
    .add("", [list(i) for i in zip(data, value)],
         rosetype="radius", radius=["10%", "50%"], center=["80%", "50%"],
         label_opts=opts.LabelOpts(formatter="{b}\n{d}%"),
         )
    .add("", [list(i) for i in zip(data, value1)],
         radius=["20%", "40%"], center=["30%", "55%"],
         label_opts=opts.LabelOpts(is_show=False))
    .set_colors(["#2ecc71", "#2980b9", "#e74c3c", "#8e44ad", "#2c3e50"])
    .set_global_opts(title_opts=opts.TitleOpts(title="pie"))
    # 饼图、仪表盘、漏斗图: {a}（系列名称），{b}（数据项名称），{c}（数值）, {d}（百分比）
    #  .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}:{d}%"))
    .render("pie.html")
)
