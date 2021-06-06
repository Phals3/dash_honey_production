import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import pandas as pd

from app import app

df = pd.read_csv('assets/honeyproduction.csv')
columns = df.columns.drop(['year', 'state'])


def test(title):
    return {
        'data': [
            {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
            {'x': [1, 2, 3], 'y': [2, 4, 5],
             'type': 'bar', 'name': u'Montréal'},
        ],
        'layout': {
            'title': title
        }}


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

        html.Div([
            html.Div(dcc.Graph(
                id='left-plot',
                figure=test('left_plot')),
                id='left-div'),

            html.Div([
                dcc.Graph(id='right-plot-1', figure=test('right_up_plot')),
                dcc.Graph(id='right-plot-2', figure=test('right_down_plot'))],
                id='right-div')],
            id='plots-dashboard'),

        html.Div(dcc.Slider(
            id='crossfilter-year--slider',
            min=df['year'].min(),
            max=df['year'].max(),
            value=df['year'].max(),
            marks={str(year): str(year) for year in df['year'].unique()},
            step=None
        ), style={'width': '49%', 'padding': '0px 20px 20px 20px'}),
    ])
    return layout


layout = Plots()

# @app.callback(
#     Output('map', 'figure'),
#     [Input('filter-years', 'value'),
#      Input('filter-variable', 'value')])
