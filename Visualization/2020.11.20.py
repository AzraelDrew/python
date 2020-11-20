# 折线图
from pyecharts.charts import Line, Grid
from pyecharts.charts import Line
from pyecharts import options as opts

# 数据准备
x = ['周一', '周二', '周三', '周四', '周五', '周六', '周日']
y1 = [37, 38, 39, 35, 37, 36, 35]
y2 = [0, -2, 3, 1, 2, 3, 5]
(
    Line()
    .add_xaxis(x)
    .add_yaxis(series_name='最高温度', y_axis=y1,
               markpoint_opts=opts.MarkPointOpts(
                   data=[opts.MarkPointItem(type_='min', name='最低点')]),
               markline_opts=opts.MarkLineOpts(data=[opts.MarkLineItem(y=25)]))

    .add_yaxis(series_name='最低温度', y_axis=y2, markpoint_opts=opts.MarkPointOpts(data=[opts.MarkPointItem(type_='max', name='最高点')]))
    .set_global_opts(title_opts=opts.TitleOpts(title='温度趋势'),
                     #  xaxis_opts=opts.AxisOpts(boundary_gap=False),
                     # 触发类型。可选：
                     # 'item': 数据项图形触发，主要在散点图，饼图等无类目轴的图表中使用。
                     # 'axis': 坐标轴触发，主要在柱状图，折线图等会使用类目轴的图表中使用。
                     # 'none': 什么都不触发
                     #  trigger: str="item",
                     tooltip_opts=opts.TooltipOpts(trigger='axis'),
                     toolbox_opts=opts.ToolboxOpts(is_show='True'))
    # 系列设置项,标记特殊点，coord自定义的点
    # .set_series_opts(markpoint_opts=opts.MarkPointOpts(data=[opts.MarkPointItem(type_='min',name='最低值')]))
    .render('20201120_1.html')
)

# 面积图
# 两个图形共在同一张画布
# 数据准备
x = ['周一', '周二', '周三', '周四', '周五', '周六', '周日']
y1 = [37, 38, 39, 35, 37, 36, 35]
y2 = [12, 8, 10, 11, 8, 6, 8]

c1 = (
    Line()
    .add_xaxis(x)
    .add_yaxis(series_name='最高温度', y_axis=y1)

    # .add_yaxis(series_name='最低温度',y_axis=y2)
    # post_left图例位置,post_top='x%'上下位置
    .set_global_opts(title_opts=opts.TitleOpts(title='温度趋势', pos_left='', pos_top=''),
                     xaxis_opts=opts.AxisOpts(boundary_gap=True),
                     tooltip_opts=opts.TooltipOpts(trigger='axis'),
                     toolbox_opts=opts.ToolboxOpts(is_show=False),
                     legend_opts=opts.LegendOpts(pos_left="20%"),
                     # 分割线,is_scale让差距变大
                     yaxis_opts=opts.AxisOpts(splitline_opts=opts.SplitLineOpts(is_show=True), is_scale=False))
    # 系列设置项,标记特殊点，coord自定义的点
    .set_series_opts(label_opts=opts.LabelOpts(is_show=True),
                     # 透明度0-1,填充面积
                     areastyle_opts=opts.AreaStyleOpts(opacity='0', color=''))
    # .render('面积图.html')
)
c2 = (
    Line()
    .add_xaxis(x)
    # .add_yaxis(series_name='最高温度', y_axis=y1)
    .add_yaxis(series_name='最低温度', y_axis=y2)
    .set_global_opts(title_opts=opts.TitleOpts(title='', pos_left='', pos_top=''),
                     xaxis_opts=opts.AxisOpts(boundary_gap=True),
                     tooltip_opts=opts.TooltipOpts(trigger='axis'),
                     toolbox_opts=opts.ToolboxOpts(is_show=False),
                     legend_opts=opts.LegendOpts(pos_left="60%"),
                     # 分割线,is_scale让差距变大
                     # 是否显示分割线
                     # is_show: bool = False,
                     yaxis_opts=opts.AxisOpts(splitline_opts=opts.SplitLineOpts(is_show=True), is_scale=False))
    # 系列设置项,标记特殊点，coord自定义的点
    .set_series_opts(label_opts=opts.LabelOpts(is_show=False),
                     # 透明度0-1,填充面积
                     areastyle_opts=opts.AreaStyleOpts(opacity='0.5', color=''))
    # .render('面积图.html')
)
# grid将图形分开,post_top下图距上图的百分比，height图形的高度
(
    Grid()
    .add(chart=c1, grid_opts=opts.GridOpts(height='30%'))
    .add(chart=c2, grid_opts=opts.GridOpts(pos_top='60%', height='30%'))
    .render('20201120_2.html')
)

x1 = ['2019-1', '2019-2', '2019-3', '2019-4', '2019-5', '2019-6',
      '2019-7', '2019-8', '2019-9', '2019-10', '2019-11', '2019-12']
x2 = ['2020-1', '2020-2', '2020-3', '2020-4', '2020-5', '2020-6',
      '2020-7', '2020-8', '2020-9', '2020-10', '2020-11', '2020-12']
y01 = [34, 25, 45, 45, 35, 38, 34, 45, 65, 25, 49, 64]
y02 = [45, 35, 64, 53, 52, 54, 58, 59, 54, 56, 78, 68]
(
    Line()
    .add_xaxis(x1,)
    .add_yaxis(series_name="2019年降水量", y_axis=y01, linestyle_opts=opts.LineStyleOpts(color='red'))
    .extend_axis(xaxis_data=x2, xaxis=opts.AxisOpts(type_='category',
                                                    axisline_opts=opts.AxisLineOpts(is_on_zero=False,
                                                                                    linestyle_opts=opts.LineStyleOpts(color='red')),
                                                    axislabel_opts=opts.LabelOpts(rotate=-30)))

    .add_yaxis(series_name="2020年降水量", y_axis=y02, linestyle_opts=opts.LineStyleOpts(color='green'))
    # is_align与坐标轴对齐
    .set_global_opts(xaxis_opts=opts.AxisOpts(axistick_opts=opts.AxisTickOpts(is_align_with_label=True,),
                                              axisline_opts=opts.AxisLineOpts(
                                                  linestyle_opts=opts.LineStyleOpts(color="green")),
                                              # 线条颜色
                                              # axisline_opts=opts.AxisLineOpts(linestyle_opts=opts.LineStyleOpts(color='green'),
                                              # 旋转角度
                                              axislabel_opts=opts.LabelOpts(
                                                  rotate=-30),
                                              ),
                     yaxis_opts=opts.AxisOpts(
                         splitline_opts=opts.SplitLineOpts(True)),
                     )
    .render('20201120_3.html')

)

# 渐变图

x1 = ['2019-1', '2019-2', '2019-3', '2019-4', '2019-5', '2019-6', '2019-7', '2019-8', '2019-9', '2019-10', '2019-11', '2019-12',
      '2020-1', '2020-2', '2020-3', '2020-4', '2020-5', '2020-6', '2020-7', '2020-8', '2020-9', '2020-10', '2020-11', '2020-12']
y01 = [34, 25, 45, 45, 35, 38, 34, 45, 65, 25, 49, 64,
       45, 35, 64, 53, 52, 54, 58, 59, 54, 56, 78, 68]
(
    Line()
    .add_xaxis(x1)
    .add_yaxis(series_name='系列一', y_axis=y01)
    .set_global_opts(xaxis_opts=opts.AxisOpts(axistick_opts=opts.AxisTickOpts(is_align_with_label=True),
                                              axislabel_opts=opts.LabelOpts(rotate=-30)),
                     # 刻度线
                     yaxis_opts=opts.AxisOpts(
        splitline_opts=opts.SplitLineOpts(is_show=True)),
        visualmap_opts=opts.VisualMapOpts(pos_right='10%', pos_bottom='10%'))
    .render('20201120_4.html')
)
