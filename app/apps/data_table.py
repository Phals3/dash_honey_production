import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_table
from dash.dependencies import Input, Output

import pandas as pd

from app import app

def DataTable():
    df = pd.read_csv('assets/honeyproduction.csv')
    layout = dash_table.DataTable(
        id='data-table',
        columns=[{"name": i, "id": i}
                 for i in df.columns],
        data=df.to_dict('records'),
        filter_action="native",
        page_size=20)
    return html.Div([layout])

layout = DataTable()
