import os

import dash

import dash_auth

import dash_bootstrap_components as dbc

from dotenv import load_dotenv

from flask import Flask

import engines


load_dotenv()

# app initialisation 
assets_folder = './assets'

server = Flask(__name__)

app = dash.Dash(
    __name__,
    server=server,
    external_stylesheets=[dbc.themes.BOOTSTRAP, dbc.icons.BOOTSTRAP],
    assets_folder=assets_folder,
    title='Markdown Notes'
)

# auth
valid_username_password_pairs = {}
USERNAMES = os.getenv("USERNAMES", "")
PASSWORDS = os.getenv("PASSWORDS", "")

if USERNAMES and PASSWORDS:
    valid_username_password_pairs = dict(
        zip(
            USERNAMES.split(","),
            PASSWORDS.split(",")
        )
    )

if valid_username_password_pairs:
    auth = dash_auth.BasicAuth(
        app,
        valid_username_password_pairs
    )

# host:port
HOST = os.getenv("HOST", "127.0.0.1")
PORT = os.getenv("PORT", 5000)

# engine settings
NOTES_PATH = 'notes'

settings = engines.filesystem.FilesystemEngineSettings(
    folder=NOTES_PATH
)

engine = engines.filesystem.FilesystemEngine(settings)
