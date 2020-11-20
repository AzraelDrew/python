from pyecharts import options as opts
from pyecharts.charts import Bar, Grid, Line
from pyecharts.faker import Faker
from random import randrange

bar = (
    Bar()
    .add_xaxis(Faker.choose())
    .add_yaxis("iphone", [randrange(5499, 10899) for _ in range(6)], category_gap="60%", color="#9b59b6", gap="34%")
    .add_yaxis("ipad", [randrange(2999, 8299) for _ in range(6)], category_gap="60%", color="#3498db")    .set_global_opts(
        title_opts=opts.TitleOpts(title="Grid-Bar", pos_left="30%"),
        datazoom_opts=opts.DataZoomOpts(
            type_="slider", pos_bottom="55%"),
        toolbox_opts=opts.ToolboxOpts(is_show=True)
    )
)
line = (
    Line()
    .add_xaxis(["一月", "二月", "三月", "四月", "五月", "六月"])
    .add_yaxis("iphone", [randrange(5499, 10899) for _ in range(6)])
    .add_yaxis("ipad", [randrange(2999, 8299) for _ in range(6)])
    .set_global_opts(
        title_opts=opts.TitleOpts(title="Grid-Line", pos_top="48%"),
        legend_opts=opts.LegendOpts(pos_top="48%"),
    )
)
# line = (
#     Line()
#     .add_xaxis(Faker.choose())
#     .add_yaxis("商家A", Faker.values())
#     .add_yaxis("商家B", Faker.values())
#     .set_global_opts(
#         title_opts=opts.TitleOpts(title="Grid-Line", pos_top="48%"),
#         legend_opts=opts.LegendOpts(pos_top="48%"),
#     )
# )
c = (
    Bar(init_opts=opts.InitOpts(width="90vw", height="90vh"))
    .add_xaxis(["一月", "二月", "三月", "四月", "五月", "六月"])
    # 设置两组数据
    # stack将两组数据叠放在一起
    # category设置柱状图宽度(设置的百分比越大则越窄)
    .add_yaxis("iphone", [randrange(5499, 10899) for _ in range(6)], category_gap="60%", color="#9b59b6", gap="34%")
    .add_yaxis("ipad", [randrange(2999, 8299) for _ in range(6)], category_gap="60%", color="#3498db")
    # 设置标题
    .set_global_opts(title_opts=opts.TitleOpts(title="Apple",),
                     legend_opts=opts.LegendOpts(pos_bottom="1%"),
                     # 将坐标轴标签旋转
                     xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=30),
                                              name="月份", name_location="start", name_gap=60, name_rotate=30, position="bottom"),
                     yaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=30),
                                              name="价格", name_location="middle", name_gap=65, name_rotate=30, position="bottom"),
                     toolbox_opts=opts.ToolboxOpts(
                         is_show=True, pos_left="80%"),
                     datazoom_opts=opts.DataZoomOpts(
                         type_="slider", pos_bottom="5%"),
                     visualmap_opts=opts.VisualMapOpts(
                         is_show=True, orient="vertical", type_="color", max_=10000))
    # position设置标签的位置默认为top
    .set_series_opts(label_opts=opts.LabelOpts(position="top", is_show=True),
                     #  coord["x","y"]   自行设置点   value  为点的高度
                     linestyle_opts=opts.LineStyleOpts(
                         is_show=bool, width=10, type_="solid"),
                     splitline_opts=opts.SplitLineOpts(is_show=True),
                     markpoint_opts=opts.MarkPointOpts(data=[opts.MarkPointItem(
                         type_="min", name="最小值"), opts.MarkPointItem(type_="max", name="最大值")]),
                     markline_opts=opts.MarkLineOpts(data=[opts.MarkLineItem(type_="min", name="最小值"),
                                                           opts.MarkLineItem(type_="max", name="最大值")]),)
)

grid = (
    Grid(init_opts=opts.InitOpts(width="90vw", height="90vh"))
    .add(c, grid_opts=opts.GridOpts(pos_bottom="60%"))
    .add(line, grid_opts=opts.GridOpts(pos_top="60%"))
    .render("grid.html")
)
