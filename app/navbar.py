import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc


def Navbar():
    navbar = dbc.Navbar(
        [
            dbc.Row(
                [dbc.Col(
                    html.Img(src='assets/bee_logo.svg', height="25px")),
                    dbc.Col(dbc.NavbarBrand(
                        "Honey Production in USA",  href='/')), ],
            ),
            dbc.Nav([
                dbc.NavItem(dbc.NavLink(
                    "Data Table", href="/apps/data_table")),
                dbc.NavItem(dbc.NavLink("Map", href="/apps/map")),
                dbc.NavItem(dbc.NavLink("Plots", href="/apps/plots"))]
            ),
        ],
        id='navbar',
    )
    return navbar


navbar = Navbar()
