import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

# from app import app

with open('assets/homepage_markdown') as file:
    homepage_content_string = file.read()

def Homepage():
    layout = html.Div(children=get_text(), id='homepage-content')
    return layout

def get_text():
    return dcc.Markdown(homepage_content_string)

layout = Homepage()
