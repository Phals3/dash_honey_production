import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

import plotly.express as px
import pandas as pd

from app import app


def get_figure(year, column_name):
    rend_df = df[df['year'] == year]
    title = f'{column_name} in {year}'
    fig = px.choropleth(rend_df,
                        locations="state",
                        color=column_name,
                        hover_name=column_name,
                        locationmode='USA-states',
                        )
    fig.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        geo=dict(bgcolor='rgba(0,0,0,0)'),
        title={'text': title, 'font': {'size': 30}},
        geo_scope='usa',
        margin={"r": 0, "t": 60, "l": 0, "b": 0},
        font_color="white",
    )
    return fig


df = pd.read_csv('assets/honeyproduction.csv')
years = df['year'].unique()
column_names = df.columns.drop(['year', 'state'])

filter_div = html.Div(
    [dcc.Slider(
        id='filter-years',
        min=df['year'].min(),
        max=df['year'].max(),
        value=df['year'].max(),
        marks={str(year): str(year) for year in df['year'].unique()},
        step=None
    ),
        dcc.RadioItems(
        id='filter-variable',
        options=[
            {'label': i, 'value': i} for i in column_names
        ],
        value='totalprod',
    )],
    id='filter-div')

map_graph = dcc.Graph(id='map', figure=get_figure(years.max(), 'totalprod'))

layout = html.Div(
    [filter_div,
     map_graph]
)


@app.callback(
    Output('map', 'figure'),
    [Input('filter-years', 'value'),
     Input('filter-variable', 'value')])
def update_figure(year, column_name):
    return get_figure(year, column_name)
