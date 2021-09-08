import dash_bootstrap_components as dbc
from dash import html

button = html.Div(
    [
        dbc.Button("Block button", color="primary"),
        dbc.Button("Block button", color="secondary"),
    ],
    class_name="d-grid gap-2 col-6 mx-auto",
)
