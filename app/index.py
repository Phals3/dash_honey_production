import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app
from navbar import navbar
from apps import homepage, data_table, map

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    navbar,
    html.Div(id='page-content')
])


@app.callback(Output('page-content', 'children'),
              Input('url', 'pathname'))
def display_page(pathname):
    if pathname == '/':
        return homepage.layout
    elif pathname == '/apps/data_table':
        return data_table.layout
    elif pathname == '/apps/map':
        return map.layout
    else:
        return homepage.layout


if __name__ == '__main__':
    app.run_server(host="0.0.0.0", port=8050, debug=True)
