import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

def Navbar():
    navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Data Table", href="/apps/data_table")),
        dbc.NavItem(dbc.NavLink("Map", href="/apps/map")),
        dbc.NavItem(dbc.NavLink("Empty", href="#")),
    ],
    brand="Home",
    brand_href="/",
    dark=True,
    )
    return navbar

navbar = Navbar()
