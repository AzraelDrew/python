from pyecharts.charts import Bar, Pie, Grid
from pyecharts import options as opts
import pandas as pd
Apple = pd.read_csv("./apple_stock.csv", header=None)
# 必须添加header=None，否则默认把第一行数据处理成列名导致缺失
list1 = Apple.values.tolist()

pie = pd.read_csv("./pie.csv", header=None)
list2 = pie.values.tolist()

apple_date = []
apple_stock = []

for apple in list1:
    apple_date.append(apple[0])
    apple_stock.append(apple[1])
apple_date.remove("AAPL_x")  # 将第一个移除
apple_stock.remove("AAPL_y")


pie_name = []
pie_data = []

for pie in list2:
    pie_name.append(pie[1])
    pie_data.append(pie[2])

pie_name.remove("Label")
# print(pie_name)
pie_data.remove("Values")
# print(pie_data)

b = (
    Bar()
    .add_xaxis(apple_date)
    # category设置柱状图宽度(设置的百分比越大则越窄)
    .add_yaxis("stock", apple_stock, category_gap="10%", color="#2ecc71", gap="0%")

    .set_global_opts(title_opts=opts.TitleOpts(title="Apple", pos_left="5%"),
                     # 将坐标轴标签旋转
                     xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=-30),
                                              name="Date", name_location="end", name_gap=20, name_rotate=0, position="bottom"),
                     yaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=30),
                                              name="stock", name_location="end", name_gap=20, name_rotate=0, position="bottom"),
                     datazoom_opts=opts.DataZoomOpts(
        # type_="inside"
        # inside直接用鼠标拖动或者使用鼠标滚轮
        # slider滚动条
                         type_="inside"),
                     legend_opts=opts.LegendOpts(),
                     visualmap_opts=opts.VisualMapOpts(is_show=True, orient="vertical", type_="color", max_=120, min_=60, pos_left="5%", pos_bottom="10%"))
    .set_series_opts(label_opts=opts.LabelOpts(position="left", is_show=False),
                     )
    # .render("1.html")
)


c = (
    Pie()
    # rosetype="radius"   以半径的大小来展示数据的大小  有'radius'和'area'两种模式
    # radius=["30%", "5%"]   饼图的半径，数组的第一项是内半径，第二项是外半径
    #  饼图的中心（圆心）坐标，数组的第一项是横坐标，第二项是纵坐标
    .add("", [list(i) for i in zip(pie_name, pie_data)],
         rosetype="radius", radius=["10%", "50%"], center=["50%", "70%"],
         label_opts=opts.LabelOpts(formatter="{b}\n{d}%"),
         )
    .set_colors(["#2ecc71", "#2980b9", "#e74c3c", "#8e44ad", "#2c3e50"])
    .set_global_opts(title_opts=opts.TitleOpts(), legend_opts=opts.LegendOpts(pos_bottom="1%"))
    # 饼图、仪表盘、漏斗图: {a}（系列名称），{b}（数据项名称），{c}（数值）, {d}（百分比）
    #  .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}:{d}%"))
    # .render("pie.html")
)

# grid将图形分开,post_top下图距上图的百分比，height图形的高度
(
    Grid(init_opts=opts.InitOpts(height="95vh", width="95vw"))
    .add(chart=b, grid_opts=opts.GridOpts(height='35%'))
    .add(chart=c, grid_opts=opts.GridOpts(pos_bottom="-5%", height='5%'))
    .render('exam.html')
)
