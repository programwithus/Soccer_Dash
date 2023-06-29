from dash import Dash
import dash_bootstrap_components as dbc
from data.util import get_data
from layout import create_layout
import os

cwd = os.getcwd()
filepath = f'{cwd}/data/FIFA - World Cup Summary.csv'

def main():
    data = get_data(filepath)
    app = Dash(external_stylesheets=[dbc.themes.COSMO])
    app.title = "World Cup Championships Analysis"
    app.layout = create_layout(app,data)
    app.run_server(debug=True)

if __name__ == "__main__":
    main()

