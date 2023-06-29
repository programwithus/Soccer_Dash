from dash import html, dcc
import plotly.express as px
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
from .ids import *

def render(app, data):
    @app.callback(
        Output(PIE_CHART, "children"),
        Input(COUNTRIES, "value")
    )  
    def update_pie_chart(countries):
        filtered_data = data.query("Country in @countries")
        if filtered_data.shape[0] == 0:
            return html.Div(dbc.Alert("No Countries Selected", color="danger"), id=PIE_CHART)
        fig = px.pie(
            data, 
            values='Championships', 
            names='Country', 
            title= 'World Cup Championships by Country', 
            color='Country',
            color_discrete_map={'Brazil':'#DFFF00',
                                'Germany':'#228B22',
                                'Italy':'#0000FF',
                                'Argentina':'#89CFF0',
                                'France':'#1434A4',
                                'Uruguay':'#A7C7E7',
                                'England':'#F6222E',
                                'Spain':'#C04000'})
        return html.Div(dcc.Graph(figure=fig), id=PIE_CHART)
    return html.Div(id=PIE_CHART)

