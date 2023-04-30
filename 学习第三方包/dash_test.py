from dash import Dash, dcc, html
import plotly.express as px
import pandas as pd

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = Dash(__name__, external_stylesheets=external_stylesheets)

# data frame 是长数据格式
df = pd.DataFrame({
    "姓名": ["LeBron", "Steph", "Harden", "姚明", "易建联", "王治郅"],
    "身高": [206, 192, 196, 226, 213, 214],
    "位置": ["SF", "PG", "PG", "C", "PF", "C"]
})

fig = px.bar(df, x="姓名", y="身高", color="位置", barmode="group")

app.layout = html.Div(children=[
    html.H1(children='NBA球员数据分析'),

    html.Div(children='''
        什么鬼
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
