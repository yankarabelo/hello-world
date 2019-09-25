# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objects as go


app = dash.Dash()
server = app.server
#df = pd.read_csv('https://raw.githubusercontent.com/LeoMonrroy/legendary-palm-tree/master/fakegraph.csv', sep=";")
df = pd.read_csv('https://github.com/yankarabelo/hello-world/raw/master/rawrdata.csv', sep=";")
sample_data_table = FF.create_table(df.head())
py.iplot(sample_data_table, filename='sample-data-table')

app.layout = html.Div(children=[
    html.H1(children='Försök till visualisering--'),
    html.Div(children='''
        Grupp nr 6
    '''),
    dcc.Graph(
        id='Försök till datavisualisering',
        figure={
            'data': [
                go.Scatter(
                    x=df.Tidpunkter,
                    y=df.ENSG00000283297,
                    mode='lines'
                )
            ],
            'layout': go.Layout(
                title='TH0 Genexpression över tid',
                xaxis={'title' : 'Tid(h)'},
                yaxis={'title': 'Expression .../...'},
            )
        })])
