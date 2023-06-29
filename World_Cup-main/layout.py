from dash import html, dcc, Dash
import dash_bootstrap_components as dbc
from components import (
                dropdown, 
                pie_chart, 
                vbar_chart, 
                vbar2_chart, 
                vbar3_chart, 
                scatter_chart,
                scatter2_chart,
                scatter3_chart
            )
import os

image_path = os.path.join(os.getcwd(), 'WorldCup.jpg')

def create_layout(app,data):
    heading = html.H1(
                "World Cup Championships Analysis", 
                className="bg-primary text-white p-2 mb-3")
    return dbc.Container(
        [
            heading,
            html.Img(src=Dash.get_asset_url(app,'WorldCup.jpg'), alt='image'),
            dbc.Row(
                [
                    dbc.Col([pie_chart.render(app,data)], width=12),

                ]),
            dbc.Row(
                [
                    dbc.Col([dropdown.render(app,data)], width=12),
                ]),
            dbc.Row(
                [
                    dbc.Col([vbar_chart.render(app,data)], width=6),
                    dbc.Col([vbar3_chart.render(app,data)], width=6),
                ]),
            dbc.Row(
                [
                    dbc.Col([vbar2_chart.render(app,data)], width=6),
                    dbc.Col(html.Img(src=Dash.get_asset_url(app,'Pele.jpg'), alt='image')),
                ]),
            dbc.Row(
                [
                    dbc.Col([scatter_chart.render(app,data)], width=6),
                    dbc.Col([scatter2_chart.render(app,data)], width=6),
                ]),
                dbc.Row(
                [
                    dbc.Col([scatter3_chart.render(app,data)], width=6),
                    dbc.Col(html.Img(src=Dash.get_asset_url(app,'Neymar.jpg'), alt='image')),
                ]),
                dbc.Row(
                [
                    dbc.Col(html.Img(src=Dash.get_asset_url(app,'Messi.jpg'), alt='image')),
                    dbc.Col(html.Img(src=Dash.get_asset_url(app,'Mbappe.jpg'), alt='image')),
                ]),

        ]
    )   

