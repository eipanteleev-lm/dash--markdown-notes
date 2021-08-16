from config import app

import dash_core_components as dcc

from dash.dependencies import ALL, Input, Output, State

import layout

import repository as repo

import utils


@app.callback(
    Output('page-content', 'children'),
    Input('url', 'pathname')
)
def render_page_content(pathname):
    md = repo.note(pathname)
    if md is None:
        template = repo.template('404')
        return layout.note(template)

    return layout.note(md)


@app.callback(
    Output('bread-crumbs', 'children'),
    Input('url', 'pathname')
)
def render_bread_crumbs(pathname):
    links = utils.web_path_bread_crumps(pathname)
    return layout.bread_crumbs(links)


@app.callback(
    Output('slidebar', 'children'),
    Input('url', 'pathname')
)
def render_slidebar(pathname):
    tree = repo.notes_tree()
    return layout.slidebar_layout(tree)


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
    md = utils.parse_note_file(contents, filename)
    path = repo.add_note(pathname, md)
    if path is None:
        return layout.alert("Something went wrong...", "danger")

    return layout.alert("Page successfully updated", "success")


@app.callback(
    Output('add-page-collapse', 'is_open'),
    [Input('add-page-collapse-button', 'n_clicks'), Input('add-page-button', 'n_clicks')],
    [State('add-page-collapse', 'is_open')],
    prevent_initial_call=True
)
def open_page_name_input(n_clicks1, n_clicks2, is_open):
    return not is_open


@app.callback(
    Output({'type': 'alert', 'index': 'add-page'}, 'children'),
    Input('add-page-button', 'n_clicks'),
    State('add-page-input', 'value'),
    State('url', 'pathname'),
    prevent_initial_call=True
)
def add_page(n_clicks, value, pathname):
    if not value:
        return layout.alert("Could not create page with empty name", "danger")

    path = repo.add_note_directory(pathname, value)
    if path is None:
        return layout.alert("Could not recreate existing page", "danger")

    template = repo.template('default')
    repo.add_note(path, template)

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
            repo.add_file(pathname, parsed_contents, filename)

    return layout.alert('Files successfully uploaded', 'success')


@app.callback(
    Output('download-page', 'data'),
    Input('download-page-button', 'n_clicks'),
    State('url', 'pathname'),
    prevent_initial_call=True
)
def download_page(n_clicks, pathname):
    md = repo.note(pathname)
    header = pathname.strip('/').split('/')[-1]
    return dcc.send_string(
        md,
        header or 'root',
    )


@app.callback(
    Output('delete-page-modal', 'is_open'),
    [
        Input('delete-page-button', 'n_clicks'),
        Input('cancel-delete-page-button', 'n_clicks'),
        Input('delete-page-modal-button', 'n_clicks')
    ],
    State('delete-page-modal', 'is_open'),
    prevent_initial_call=True
)
def open_delete_modal(n_clicks1, n_clicks2, n_clicks3, is_open):
    return not is_open


@app.callback(
    Output({'type': 'alert', 'index': 'delete-page'}, 'children'),
    Input('delete-page-button', 'n_clicks'),
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
            "danger"
        )

    repo.delete_note(pathname)
    return layout.alert("Pages successfully deleted", "success")



