from dash import html, dcc
from dash.dependencies import Input, Output
import plotly.express as px
import dash_bootstrap_components as dbc
from .ids import *

def render(app, data):
    list_countries = data["Country"].unique()
    all_countries = [{'label': country,'value': country} for country in list_countries]

    @app.callback(
        Output(COUNTRIES, "value"),
        Input(SELECT_BUTTON, "n_clicks")
    )
    def update_all_countires(n):
        return list_countries

    return html.Div(
        [
            html.H3("Select Country"),
            dcc.Dropdown(
                options = all_countries,
                multi=True,
                value = "Brazil",
                id = COUNTRIES
            ),
            dbc.Button(
                ["Select all"], 
                color="primary", 
                className="me-1",
                id = SELECT_BUTTON, 
                n_clicks = 0
            )
        ]
    )