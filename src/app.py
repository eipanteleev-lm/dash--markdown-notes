from config import app, HOST, PORT

import callbacks

import handlers

import layout.base as base

app.layout = base.main()


if __name__ == "__main__":
    app.run_server(HOST, PORT)
