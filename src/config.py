import os

import dash

import dash_bootstrap_components as dbc

from flask import Flask

import engines


assets_folder = './assets'

server = Flask(__name__)

app = dash.Dash(
    __name__,
    server=server,
    external_stylesheets=[dbc.themes.BOOTSTRAP],
    assets_folder=assets_folder,
    title='Markdown Notes'
)

# host:port
HOST = os.getenv("HOST", "127.0.0.1")
PORT = os.getenv("PORT", 5000)

NOTES_PATH = 'notes'

settings = engines.filesystem.FilesystemEngineSettings(
    folder=NOTES_PATH
)

engine = engines.filesystem.FilesystemEngine(settings)
