from config import app, HOST, PORT

import callbacks

import handlers

import layout

app.layout = layout.main()


if __name__ == "__main__":
    app.run_server(HOST, PORT)
