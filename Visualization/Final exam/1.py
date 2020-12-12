from pyecharts.charts import Bar, Pie, Line, Grid
from pyecharts import options as opts
import pandas as pd
bar = pd.read_csv("./bar.csv", header=None)
# 必须添加header=None，否则默认把第一行数据处理成列名导致缺失
list1 = bar.values.tolist()


pie = pd.read_csv("./pie.csv", header=None)
list3 = pie.values.tolist()

bar_date = []
bar_data1 = []
bar_data2 = []

for bar in list1:
    bar_date.append(bar[0])
    bar_data1.append(bar[1])
    bar_data2.append(bar[2])


pie_name = []
pie_data = []

for pie in list3:
    pie_name.append(pie[0])
    pie_data.append(pie[1])


b = (
    Bar()
    .add_xaxis(bar_date)
    # category设置柱状图宽度(设置的百分比越大则越窄)
    .add_yaxis("", bar_data1, category_gap="10%", color="#2ecc71", gap="0%")

    .set_global_opts(title_opts=opts.TitleOpts(title="Final Exam", pos_left="48%"),
                     # 将坐标轴标签旋转
                     xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=-30),
                                              name="Date", name_location="end", name_gap=20, name_rotate=0, position="bottom"),
                     yaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=30),
                                              name="temperature", name_location="end", name_gap=20, name_rotate=0, position="bottom"),
                     datazoom_opts=opts.DataZoomOpts(
        # type_="inside"
        # inside直接用鼠标拖动或者使用鼠标滚轮
        # slider滚动条
                         type_="inside"),
                     legend_opts=opts.LegendOpts(),
                     visualmap_opts=opts.VisualMapOpts(is_show=True, orient="vertical", type_="color", max_=30, min_=5, pos_left="2%", pos_bottom="40%"))
    .set_series_opts(label_opts=opts.LabelOpts(position="left", is_show=False),
                     )
)

l = (
    Line()
    .add_xaxis(bar_date)
    .add_yaxis(series_name="", y_axis=bar_data2, yaxis_index=1)
)
b.overlap(l)

c = (
    Pie()
    # rosetype="radius"   以半径的大小来展示数据的大小  有'radius'和'area'两种模式
    # radius=["30%", "5%"]   饼图的半径，数组的第一项是内半径，第二项是外半径
    #  饼图的中心（圆心）坐标，数组的第一项是横坐标，第二项是纵坐标
    .add("", [list(i) for i in zip(pie_name, pie_data)],
         rosetype="radius", radius=["10%", "40%"], center=["20%", "50%"],
         label_opts=opts.LabelOpts(formatter="{b}\n{d}%"),
         )
    .set_global_opts(title_opts=opts.TitleOpts(), legend_opts=opts.LegendOpts(pos_bottom="3%", pos_left="3%"),
                     )
    # 饼图、仪表盘、漏斗图: {a}（系列名称），{b}（数据项名称），{c}（数值）, {d}（百分比）
    #  .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}:{d}%"))
    # .render("pie.html")
)

# grid将图形分开,post_top下图距上图的百分比，height图形的高度
(
    Grid(init_opts=opts.InitOpts(height="98vh", width="99.5vw"))
    .add(b, grid_opts=opts.GridOpts(width="45%", pos_left="50%"))
    .add(c, grid_opts=opts.GridOpts(pos_right="50%"))
    .render('exam.html')
)
