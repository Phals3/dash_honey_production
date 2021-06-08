import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
from dash.dependencies import Input, Output


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
            id='crossfilter-year-slider',
            min=df['year'].min(),
            max=df['year'].max(),
            value=df['year'].max(),
            marks={str(year): str(year) for year in df['year'].unique()},
            step=None
        ), style={'width': '49%', 'padding': '0px 20px 20px 20px'}),
    ])
    return layout


layout = Plots()


@app.callback(
    Output('left-plot', 'figure'),
    [Input('crossfilter-xaxis-column', 'value'),
     Input('crossfilter-yaxis-column', 'value'),
     Input('crossfilter-year-slider', 'value')])
def update_left_figure(xaxis_column_name, yaxis_column_name, year):
    dff = df[df['year'] == year]
    fig = px.scatter(x=dff[xaxis_column_name],
                     y=dff[yaxis_column_name],
                     )
    return fig


def create_time_series(dff):

    fig = px.scatter(dff, x='year', y='totalprod')

    fig.update_traces(mode='lines+markers')

    fig.update_xaxes(showgrid=False)

    fig.add_annotation(x=0, y=0.85, xanchor='left', yanchor='bottom',
                       xref='paper', yref='paper', showarrow=False, align='left',
                       bgcolor='rgba(255, 255, 255, 0.5)', text='title')

    fig.update_layout(height=225, margin={'l': 20, 'b': 30, 'r': 10, 't': 10})

    return fig


@app.callback(
    Output('right-plot-1', 'figure'),
    Input('crossfilter-xaxis-column', 'value'))
def update_x_timeseries(xaxis_column_name):
    dff = df[df['state'] == 'AL']
    return create_time_series(dff)


@app.callback(
    Output('right-plot-2', 'figure'),
    Input('crossfilter-yaxis-column', 'value'))
def update_y_timeseries(yaxis_column_name):
    dff = df[df['state'] == 'AL']
    return create_time_series(dff)
