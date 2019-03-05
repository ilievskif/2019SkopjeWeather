import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv('2019SkopjeWeather.csv')

data = [go.Heatmap(x=df['DAY'],
                   y=df['LST_TIME'],
                   z=df['T_HR_AVG'].values.tolist(),
                   colorscale='Jet')]

layout = go.Layout(title='Skopje weather from 2019/02/26 to 2019/03/04')

fig = go.Figure(data=data,layout=layout)
pyo.plot(fig)
