import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
from dash.dependencies import Input, Output
from name_dicts import us_abbrev_state

from app import app

df = pd.read_csv('assets/honeyproduction.csv')
columns = df.columns.drop(['year', 'state'])
states = df['state'].unique()
df_grouped = df.groupby(['year']).sum().reset_index()

avg_priceperlb = df.groupby(['year']).mean().reset_index()[['priceperlb']]
df_grouped = df.groupby(['year']).sum().reset_index()
df_grouped['priceperlb'] = avg_priceperlb


def get_two_variables_plot(xaxis_column_name, yaxis_column_name, year):
    dff = df[df['year'] == year]
    fig = px.scatter(x=dff[xaxis_column_name],
                     y=dff[yaxis_column_name])
    fig.update_xaxes(title=xaxis_column_name)
    fig.update_yaxes(title=yaxis_column_name)
    fig.update_layout(
        title={'text': f"{yaxis_column_name} by {xaxis_column_name}",
               'font': {'size': 15}},
        paper_bgcolor='rgba(0,0,0,0)',
        geo=dict(bgcolor='rgba(0,0,0,0)'),
        font_color="white",
        margin={"r": 20, "t": 20, "l": 0, "b": 0},
    )
    return fig


def get_time_series(var_name):
    fig = px.scatter(df_grouped, x='year', y=var_name)
    fig.update_traces(mode='lines+markers')
    fig.update_yaxes(title=var_name, showgrid=False)
    fig.add_annotation(x=0, y=1, xanchor='left', yanchor='top',
                       xref='paper', yref='paper', showarrow=False, align='left',
                       bgcolor='rgba(255, 255, 255, 0.2)', text=f"Timeseries for overall {var_name}",
                       font={'color':'black'})
    fig.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        geo=dict(bgcolor='rgba(0,0,0,0)'),
        font_color="white",
        margin={"r": 25, "t": 20, "l": 0, "b": 0},
    )
    return fig


def Plots():
    layout = html.Div([
        html.H3("Overall statistics", style={'margin-left':'50px'}),
        html.Div([
            html.Div([
                dcc.Dropdown(
                    id='crossfilter-xaxis-column',
                    options=[{'label': i, 'value': i} for i in columns],
                    value=columns[2]
                )
            ],
                className='filter-dropdown'),

            html.Div([
                dcc.Dropdown(
                    id='crossfilter-yaxis-column',
                    options=[{'label': i, 'value': i} for i in columns],
                    value=columns[2]
                ),
            ], className='filter-dropdown')],
            id='dropdowns'),

        html.Div([
            html.Div(dcc.Graph(
                id='left-plot', figure=get_two_variables_plot(
                    'totalprod', 'totalprod', df['year'].max())),
                id='left-div'),

            html.Div([
                dcc.Graph(id='right-plot-1',
                          figure=get_time_series('totalprod')),
                dcc.Graph(id='right-plot-2',
                          figure=get_time_series('totalprod'))],
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
    ], id='plots-container')
    return layout


layout = Plots()


@ app.callback(
    Output('left-plot', 'figure'),
    [Input('crossfilter-xaxis-column', 'value'),
     Input('crossfilter-yaxis-column', 'value'),
     Input('crossfilter-year-slider', 'value')])
def update_left_figure(xaxis_column_name, yaxis_column_name, year):
    return get_two_variables_plot(xaxis_column_name, yaxis_column_name, year)


@ app.callback(
    Output('right-plot-1', 'figure'),
    Input('crossfilter-xaxis-column', 'value'))
def update_x_timeseries(xaxis_column_name):
    return get_time_series(xaxis_column_name)


@ app.callback(
    Output('right-plot-2', 'figure'),
    Input('crossfilter-yaxis-column', 'value'))
def update_y_timeseries(yaxis_column_name):
    return get_time_series(yaxis_column_name)
