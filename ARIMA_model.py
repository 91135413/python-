import pandas as pd
from pmdarima import auto_arima
from pyecharts import options as opts
from pyecharts.charts import Line
from pyecharts.globals import ThemeType

df = pd.read_csv('data.csv')

df['年份'] = pd.to_datetime(df['年份'], format='%Y')
df.set_index('年份', inplace=True)

df.fillna(method='ffill', inplace=True)

for column in df.columns:
    if column != '年份':
        df[column] = pd.to_numeric(df[column], errors='coerce')

forecasts = {}
districts = ['福田区', '罗湖区', '盐田区', '南山区', '宝安区', '龙岗区', '龙华区', '坪山区', '光明新区', '大鹏新区']

forecast_data = []

for district in districts:
    series = df[district].dropna()

    model = auto_arima(series, seasonal=False, stepwise=True, trace=True)
    print(f'Best model for {district}: {model.summary()}')

    forecast, conf_int = model.predict(n_periods=5, return_conf_int=True)
    forecasts[district] = {'forecast': forecast, 'conf_int': conf_int}

    forecast_years = pd.date_range(start=df.index[-1], periods=6, freq='YS')[1:]
    for year, price in zip(forecast_years, forecast):
        forecast_data.append([district, year.year, round(price)])

forecast_df = pd.DataFrame(forecast_data, columns=['District', 'Year', 'Forecasted_Price'])
forecast_df.to_csv('forecasted_prices.csv', index=False, encoding='utf-8-sig')

for district in districts:
    line = Line(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))

    historical_years = df.index.strftime('%Y').tolist()
    historical_prices = df[district].tolist()

    forecast_years = pd.date_range(start=df.index[-1], periods=6, freq='YS')[1:]
    future_years_str = forecast_years.strftime('%Y').tolist()
    forecast_prices = forecasts[district]['forecast'].tolist()

    forecast_prices = [round(price) for price in forecast_prices]

    all_years = historical_years + future_years_str
    all_prices = historical_prices + forecast_prices

    line.add_xaxis(all_years)
    line.add_yaxis(f"{district} 房价预测", all_prices, is_smooth=True, linestyle_opts=opts.LineStyleOpts(width=2, color="red"))

    line.set_global_opts(
        title_opts=opts.TitleOpts(title=f"{district} 房价预测", subtitle="历史房价与未来5年预测"),
        xaxis_opts=opts.AxisOpts(
            name="年份",
            type_="category",
            boundary_gap=False,
            axislabel_opts=opts.LabelOpts(rotate=45),
        ),
        yaxis_opts=opts.AxisOpts(name="单价(元/㎡)"),
        tooltip_opts=opts.TooltipOpts(trigger="axis", axis_pointer_type="cross"),
        datazoom_opts=opts.DataZoomOpts(is_show=True),
        legend_opts=opts.LegendOpts(is_show=True),
    )
    line.render(f"{district}房价预测.html")
