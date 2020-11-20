'''
 $ @Author       : yznaisy
 $ @Date         : 2020-10-23 08:14:55
 $ @LastEditors  : yznaisy
 $ @LastEditTime : 2020-10-30 11:21:35
'''
from pyecharts.charts import Bar, Grid
from pyecharts.faker import Faker
from pyecharts import options as opts
from pyecharts.globals import ThemeType

# bar = Bar()  # 实例化图形函数、
# # pie = Pie()  # 实例化图形函数、饼图
# bar.add_xaxis(Faker.choose())  # 添加数据
# bar.add_yaxis("系列名", Faker.values())  # 添加数据
# bar.set_global_opts(title_opts=opts.TitleOpts(title="主标题", subtitle="副标题"))
# bar.render()  # 保存图形

# help(Faker)  # pyecharts自带数据数据
# print(Faker.choose())
# print(Faker.values())

# 链式方法
c = (
    Bar()
    .add_xaxis(Faker.choose())
    # 设置两组数据
    # stack将两组数据叠放在一起
    # category设置柱状图宽度(设置的百分比越大则越窄)
    .add_yaxis("b", Faker.values(), stack="stack1", category_gap="60%", color="#2ecc71")
    .add_yaxis("a", Faker.values(), stack="stack1", category_gap="60%", color="#3498db")
    # 设置标题
    .set_global_opts(title_opts=opts.TitleOpts(title="主标题", subtitle="副标题"),
                     # 将坐标轴标签旋转
                     xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=30),
                                              name="日期", name_location="center", name_gap=30, name_rotate=30, position="bottom"),
                     yaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=30),
                                              name="数据", name_location="center", name_gap=30, name_rotate=30, position="bottom"),
                     #  yaxis_opts=opts.AxisOpts(
                     #      name="数据"),
                     #  tooltip_opts=opts.TooltipOpts(
                     #      axislabel_opts=opts.TooltipOpts(axis_pointer_type="line"))
                     )
    # position设置标签的位置默认为top
    .set_series_opts(label_opts=opts.LabelOpts(position="left", is_show=False),
                     )
    .render("柱状图1.html")
)
