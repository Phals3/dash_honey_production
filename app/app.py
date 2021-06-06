import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

from navbar import Navbar
from homepage import Homepage
from data_table import DataTable
from map import Map
from body3 import Body3


app = dash.Dash(__name__, suppress_callback_exceptions=True, external_stylesheets=[dbc.themes.DARKLY])

app.layout = html.Div([
    dcc.Location(id = 'url', refresh = False),
    Navbar(),
    html.Div(id = 'page-content')
])


@app.callback(dash.dependencies.Output('page-content', 'children'),
            [dash.dependencies.Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/data_table':
        return DataTable()
    elif pathname == '/map':
        return Map()
    elif pathname == '/page-3':
        return Body3()
    else:
        return Homepage()

if __name__ == '__main__':
    app.run_server(host="0.0.0.0", port=8050, debug=True)
