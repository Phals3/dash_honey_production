import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

def Body3():
    body = html.Div(
    [
       dbc.Row(dbc.Col(html.Div("Page 3")))
    ]
    )
    return body