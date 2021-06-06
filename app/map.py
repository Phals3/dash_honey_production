import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

import plotly.express as px
import pandas as pd

df = pd.read_csv('honeyproduction.csv')
years = df['year'].unique()


def get_figure():
    rend_df = df[df['year'] == 1998]
    # rend_df = df
    fig = px.choropleth(rend_df,  # Input Pandas DataFrame
                        locations="state",  # DataFrame column with locations
                        color="totalprod",  # DataFrame column with color values
                        hover_name="totalprod",  # DataFrame column hover info
                        locationmode='USA-states')  # Set to plot as US States
    fig.update_layout(
        title_text='States',  # Create a Title
        geo_scope='usa',  # Plot only the USA instead of globe
        margin={"r": 0, "t": 0, "l": 0, "b": 0}
    )
    return fig


def Map():
    filter_div = html.Div([
        dcc.Dropdown(
            id='crossfilter-years-column',
            options=[{'label': i, 'value': i}
                     for i in years],
            value='year'
        )], id='filter-div')

    body = html.Div(
        [
            filter_div,
            dcc.Graph(id='choropleth', figure=get_figure())
        ]
    )
    return body
