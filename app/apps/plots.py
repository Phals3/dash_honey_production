import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import pandas as pd

from app import app

df = pd.read_csv('assets/honeyproduction.csv')
columns = df.columns.drop(['year', 'state'])


def Plots():
    layout = html.Div([
    html.Div([
        html.Div([
            dcc.Dropdown(
                id='crossfilter-xaxis-column',
                options=[{'label': i, 'value': i} for i in columns],
                value=columns[2]
            )
        ],
        id='filter-columns1'),

        html.Div([
            dcc.Dropdown(
                id='crossfilter-yaxis-column',
                options=[{'label': i, 'value': i} for i in columns],
                value=columns[2]
            ),
        ], id='filter-columns2')],
        id='dropdowns'),

    # html.Div([
    #     dcc.Graph(
    #         id='crossfilter-indicator-scatter',
    #         hoverData={'points': [{'customdata': 'Japan'}]}
    #     )
    # ], style={'width': '49%', 'display': 'inline-block', 'padding': '0 20'}),
    # html.Div([
    #     dcc.Graph(id='x-time-series'),
    #     dcc.Graph(id='y-time-series'),
    # ], style={'display': 'inline-block', 'width': '49%'}),

    # html.Div(dcc.Slider(
    #     id='crossfilter-year--slider',
    #     min=df['year'].min(),
    #     max=df['year'].max(),
    #     value=df['year'].max(),
    #     marks={str(year): str(year) for year in df['year'].unique()},
    #     step=None
    # ), style={'width': '49%', 'padding': '0px 20px 20px 20px'}
    ])
    return layout

layout=Plots()
