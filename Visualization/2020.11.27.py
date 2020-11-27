from pyecharts.charts import Radar, Bar, Scatter, Line
from pyecharts import options as opts

Rabar_v1 = [[4300, 1000, 2800, 3500, 5000, 1900]]
Rabar_v2 = [[500, 1400, 2800, 3100, 4200, 2100]]
Rabar_v2 = [[500, 1400, 2000, 3100, 4200, 2100]]
Rabar_v2 = [[50, 140, 280, 310, 420, 210]]
gol = ['销售', '管理', '信息技术', '客服', '研发', '市场']
(
    Radar()
    # # 指示器名称。
    # name: Optional[str]=None,

    # # 指示器的最大值，可选，建议设置
    # min_: Optional[Numeric]=None,

    # # 指示器的最小值，可选，默认为 0。
    # max_: Optional[Numeric]=None,

    # # 标签特定的颜色。
    # color: Optional[str]=None,
    .add_schema(schema=[opts.RadarIndicatorItem(name='销售', max_=5000),
                        opts.RadarIndicatorItem(name='管理', max_=5000),
                        opts.RadarIndicatorItem(name='信息技术', max_=5000),
                        opts.RadarIndicatorItem(name='客服', max_=5000),
                        opts.RadarIndicatorItem(name='研发', max_=5000),
                        opts.RadarIndicatorItem(name='市场', max_=5000)
                        ],
                # shape=[]
                #             angleaxis_opts=opts.AngleAxisOpts(
                # ),

                # 图形透明度。支持从 0 到 1 的数字，为 0 时不绘制该图形。
                splitarea_opt=opts.SplitAreaOpts(
        areastyle_opts=opts.AreaStyleOpts(opacity=1)),
        # radiusaxis_opts=opts.RadiusAxisOpts(
        #     min_=0,
        #     max_=5000,
        #     interval=1000,),
        # polar_opts=opts.PolarOpts(),
    )
    .add('预算金额', data=Rabar_v1, linestyle_opts=opts.LineStyleOpts(color='red'), areastyle_opts=opts.AreaStyleOpts(opacity=0.2))
    .add("实际金额", data=Rabar_v2, linestyle_opts=opts.LineStyleOpts(color='green'), areastyle_opts=opts.AreaStyleOpts(opacity=0.4))
    .add("支付", data=Rabar_v2, linestyle_opts=opts.LineStyleOpts(color='yellow'), areastyle_opts=opts.AreaStyleOpts(opacity=0.6))
    .add("分期", data=Rabar_v2, linestyle_opts=opts.LineStyleOpts(color='black'), areastyle_opts=opts.AreaStyleOpts(opacity=0.6))
    # 是否显示标签。
    .set_series_opts(label_opts=opts.LabelOpts(is_show=True))
    # 图例选择的模式，控制是否可以通过点击图例改变系列的显示状态。默认开启图例选择，可以设成 false 关闭
    # 除此之外也可以设成 'single' 或者 'multiple' 使用单选或者多选模式。
    .set_global_opts(legend_opts=opts.LegendOpts(selected_mode='single'))
    .render("Rabar.html")
)
'''
叠成多图
'''
Overlap_v1 = [2.0, 4.9, 7.0, 23.5, 135, 26, 19.5, 20, 10, 6.4, 3.3, 2.3]
Overlap_v2 = [2.8, 5.9, 7.9, 23.2, 100, 66, 59.5, 10, 20, 16.4, 2.3, 1.3]
Overlap_v3 = [2.8, 5.9, 7.9, 23.2, 40.0, 36.6, 29.5, 20, 30, 36.4, 23, 13]
Overlap_x = ['1月', '2月', '3月', '41月', '5月', '6月',
             '7月', '8月', '9月', '10月', '11月', '12月']
# is_align_with_label 刻度对齐2
bar = (
    Bar()
    .add_xaxis(Overlap_x)
    .add_yaxis(series_name="蒸发量", y_axis=Overlap_v1, category_gap="0%", gap="0%")
    .add_yaxis(series_name="降水量", y_axis=Overlap_v2, category_gap="0%", gap="0%",
               markpoint_opts=opts.MarkPointOpts(data=[opts.MarkPointItem(coord=['6月', 66], value=66)]))
    .extend_axis(yaxis=opts.AxisOpts(axislabel_opts=opts.LabelOpts(formatter='{value}℃')))
    .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    .set_global_opts(yaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(formatter='{value}ml'),
                                              splitline_opts=opts.SplitLineOpts(
                                                  linestyle_opts=opts.LineStyleOpts(opacity=1)),
                                              # 类目轴中在 boundaryGap 为 true 的时候有效，可以保证刻度线和标签对齐。
                                              axistick_opts=opts.AxisTickOpts(
                                                  is_align_with_label=True)
                                              ))
)
line = (
    Line()
    .add_xaxis(Overlap_x)
    .add_yaxis(series_name="温度", y_axis=Overlap_v3, yaxis_index=1)
)
bar.overlap(line)
bar.render("Overlap.html")


'''
散点
'''
Scatter_x = [2, 1, 3, 4, 5, 6, 9]
Scatter_y = [23.1, 54.3, 55, 34, 35, 45, 22]
# is_align_with_label 刻度对齐
(
    Scatter()
    .add_xaxis(xaxis_data=Scatter_x)
    .add_yaxis("", y_axis=Scatter_y)
    .set_global_opts(xaxis_opts=opts.AxisOpts(type_='value', splitline_opts=opts.SplitLineOpts(is_show=True), split_number=9), yaxis_opts=opts.AxisOpts(splitline_opts=opts.SplitLineOpts(is_show=True)),
                     visualmap_opts=opts.VisualMapOpts(
        type_='size', min_=10, max_=60)
    )
    .set_series_opts(label_opts=opts.LabelOpts(is_show=False),
                     markpoint_opts=opts.MarkPointOpts(
        data=[opts.MarkPointItem(coord=[4, 34], value=34)]),
    )
    .render("Scatter.html")
)
