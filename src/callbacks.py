from config import app, engine

import dash_core_components as dcc

from dash.dependencies import ALL, MATCH, Input, Output, State

import layout

import repository as repo

import utils


@app.callback(
    Output('page-content', 'children'),
    [
        Input('url', 'pathname'),
        Input('interval', 'n_intervals')
    ]
)
def render_page_content(pathname, n_intervals):
    md = engine.note(pathname)
    if md is None:
        template = repo.template('404')
        return layout.note(template)

    return layout.note(md)


@app.callback(
    Output('bread-crumbs', 'children'),
    Input('url', 'pathname')
)
def render_bread_crumbs(pathname):
    links = utils.webpath_bread_crumps(pathname)
    return layout.bread_crumbs(links)


@app.callback(
    Output('slidebar', 'children'),
    [
        Input('url', 'pathname'),
        Input('interval', 'n_intervals')
    ]
)
def render_slidebar(pathname, n_intervals):
    tree = engine.notes_tree()
    pathlist = utils.webpath_to_list(pathname)
    return layout.slidebar_layout(tree, pathlist)


@app.callback(
    Output('files', 'children'),
    [
        Input('url', 'pathname'),
        Input('interval', 'n_intervals')
    ]
)
def render_files(pathname, n_intervals):
    filenames = engine.files_list(pathname)
    if filenames:
        return layout.files(filenames)

    return []


@app.callback(
    Output({"type": "file-link-clipboard", "index": MATCH}, "content"),
    Input({"type": "file-link-clipboard", "index": MATCH}, "n_clicks"),
    [
        State({"type": "file-link-div", "index": MATCH}, "children"),
        State('url', 'pathname')
    ]
)
def copy_file_link(n_clicks, filename, pathname):
    return utils.file_link(pathname, filename)


@app.callback(
    Output('url', 'pathname'),
    Input({'type': 'alert', 'index': ALL}, 'children'),
    State('url', 'pathname'),
    prevent_initial_call=True
)
def refresh_page(children, pathname):
    return pathname


@app.callback(
    Output({'type': 'alert', 'index': 'update-page'}, 'children'),
    Input('update-page', 'contents'),
    State('update-page', 'filename'),
    State('url', 'pathname'),
    prevent_initial_call=True
)
def upload_page(contents, filename, pathname):
    if pathname == '/':
        return layout.alert(
            (
                "Are you sure you want to update the home page?"
                + " We can't let you do that."
            ),
            "warning"
        )

    md = utils.parse_note_file(contents, filename)
    path = engine.add_note(pathname, md)
    if path is None:
        return layout.alert("Something went wrong...", "danger")

    return layout.alert("Page successfully updated", "success")


@app.callback(
    Output('add-page-collapse', 'is_open'),
    [
        Input('add-page-collapse-button', 'n_clicks'),
        Input('add-page-button', 'n_clicks')
    ],
    [State('add-page-collapse', 'is_open')],
    prevent_initial_call=True
)
def open_page_name_input(n_clicks1, n_clicks2, is_open):
    return not is_open


@app.callback(
    [
        Output('edit-page-collapse', 'is_open'),
        Output('edit-page-textarea', 'value'),
        Output('edit-page-textarea', 'rows')
    ],
    [
        Input('edit-page-collapse-button', 'n_clicks'),
        Input('save-page-button', 'n_clicks'),
        Input('cancel-save-page-button', 'n_clicks')
    ],
    [
        State('edit-page-collapse', 'is_open'),
        State('url', 'pathname')
    ],
    prevent_initial_call=True
)
def open_edit_name_textarea(n_clicks1, n_clicks2, n_clicks3, is_open, pathname):
    if not is_open:
        md = engine.note(pathname)
        return not is_open, md, len(md.split('\n'))

    return not is_open, '', 0


@app.callback(
    Output('edit-page-preview', 'children'),
    Input('edit-page-textarea', 'value'),
    Input('edit-page-collapse', 'is_open')
)
def load_extedit_preview(text, is_open):
    return text


@app.callback(
    Output({'type': 'alert', 'index': 'edit-page'}, 'children'),
    Input('save-page-button', 'n_clicks'),
    State('edit-page-textarea', 'value'),
    State('url', 'pathname'),
    prevent_initial_call=True
)
def save_page(n_clicks, value, pathname):
    if pathname == '/':
        return layout.alert(
            (
                "Are you sure you want to update the home page?"
                + " We can't let you do that."
            ),
            "warning"
        )

    path = engine.add_note(pathname, value.encode('utf-8'))
    if path is None:
        return layout.alert("Error while saving new page version", "error")

    return layout.alert("Page successfully updated", "success")


@app.callback(
    Output({'type': 'alert', 'index': 'add-page'}, 'children'),
    Input('add-page-button', 'n_clicks'),
    State('add-page-input', 'value'),
    State('url', 'pathname'),
    prevent_initial_call=True
)
def add_page(n_clicks, value, pathname):
    if not value:
        return layout.alert("Could not create page with empty name", "warning")

    path = engine.add_note_directory(pathname, value)
    if path is None:
        return layout.alert("Could not recreate existing page", "warning")

    template = repo.template('default')
    engine.add_note(path, template.encode('utf-8'))

    return layout.alert("Page successfully created", "success")


@app.callback(
    Output({'type': 'alert', 'index': 'upload-file'}, 'children'),
    Input('upload-file', 'contents'),
    State('upload-file', 'filename'),
    State('url', 'pathname'),
    prevent_initial_call=True
)
def upload_file(contents_list, filenames_list, pathname):
    if contents_list is not None:
        for contents, filename in zip(contents_list, filenames_list):
            parsed_contents = utils.parse_file(contents)
            engine.add_file(pathname, parsed_contents, filename)

    return layout.alert('Files successfully uploaded', 'success')


@app.callback(
    Output('download-page', 'data'),
    Input('download-page-button', 'n_clicks'),
    State('url', 'pathname'),
    prevent_initial_call=True
)
def download_page(n_clicks, pathname):
    md = engine.note(pathname)
    header = pathname.strip('/').split('/')[-1]
    return dcc.send_string(
        md,
        header or 'root',
    )


@app.callback(
    Output('download-notes', 'data'),
    Input('download-notes-button', 'n_clicks'),
    State('url', 'pathname'),
    prevent_initial_call=True
)
def download_notes(n_clicks, pathname):
    fullpath = engine.archive_folder(pathname)
    return dcc.send_file(fullpath)


@app.callback(
    Output({"type": "action-modal", "index": MATCH}, 'is_open'),
    [
        Input({"type": "accept-button", "index": MATCH}, 'n_clicks'),
        Input({"type": "cancel-button", "index": MATCH}, 'n_clicks'),
        Input({"type": "modal-button", "index": MATCH}, 'n_clicks')
    ],
    State({"type": "action-modal", "index": MATCH}, 'is_open'),
    prevent_initial_call=True
)
def open_modal(n_clicks1, n_clicks2, n_clicks3, is_open):
    return not is_open


@app.callback(
    Output({'type': 'alert', 'index': 'clear-page'}, 'children'),
    Input({"type": "accept-button", "index": "clear-page"}, 'n_clicks'),
    State('url', 'pathname'),
    prevent_initial_call=True
)
def clear_page(n_clicks, pathname):
    if pathname == '/':
        return layout.alert(
            (
                "Are you sure you want to clear the home page?"
                + " We can't let you do that."
            ),
            "warning"
        )

    engine.clear_note(pathname)
    
    template = repo.template('default')
    engine.add_note(pathname, template.encode('utf-8'))
    return layout.alert("Page successfully cleared", "success")


@app.callback(
    Output({'type': 'alert', 'index': 'delete-page'}, 'children'),
    Input({"type": "accept-button", "index": "delete-page"}, 'n_clicks'),
    State('url', 'pathname'),
    prevent_initial_call=True
)
def delete_page(n_clicks, pathname):
    if pathname == '/':
        return layout.alert(
            (
                "Are you sure you want to delete the home page?"
                + " We can't let you do that."
            ),
            "warning"
        )

    engine.delete_note(pathname)
    return layout.alert("Pages successfully deleted", "success")



