import os

import dash

import dash_bootstrap_components as dbc


app = dash.Dash(
    __name__,
    external_stylesheets=[dbc.themes.BOOTSTRAP],
    title='Markdown Notes'
)


HOST = os.getenv("HOST", "127.0.0.1")
PORT = os.getenv("PORT", 5000)

SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
    "overflow": "auto"
}

CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}

NOTES_PATH = 'notes'