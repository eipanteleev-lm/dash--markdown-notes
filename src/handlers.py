import os

import config
from config import server

from flask import send_from_directory

@server.route("/file/<path:path>", methods=["GET"])
def download(path):
    """Serve a file from the upload directory."""
    return send_from_directory(os.path.join('..', config.NOTES_PATH), path)