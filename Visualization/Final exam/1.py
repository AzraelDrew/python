from pyecharts.charts import Bar, Pie
from pyecharts import options as opts
import pandas as pd
Apple = pd.read_csv("./apple_stock.csv", header=None)
# 必须添加header=None，否则默认把第一行数据处理成列名导致缺失
list1 = Apple.values.tolist()

Pie = pd.read_csv("./pie.csv", header=None)
list2 = Pie.values.tolist()

apple_date = []
apple_stock = []

for apple in list1:
    apple_date.append(apple[0])
    apple_stock.append(apple[1])
apple_date.remove("AAPL_x")  # 将第一个移除
apple_stock.remove("AAPL_y")


b = (
    Bar(init_opts=opts.InitOpts(height="95vh", width="95vw"))
    .add_xaxis(apple_date)
    # category设置柱状图宽度(设置的百分比越大则越窄)
    .add_yaxis("stock", apple_stock, category_gap="10%", color="#2ecc71", gap="0%")

    .set_global_opts(title_opts=opts.TitleOpts(title="Apple", pos_left="45%"),
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
                     visualmap_opts=opts.VisualMapOpts(is_show=True, orient="vertical", type_="color", max_=120, min_=60))
    .set_series_opts(label_opts=opts.LabelOpts(position="left", is_show=False),
                     )
    .render("1.html")
)
