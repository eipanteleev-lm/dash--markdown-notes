from dash import dcc, html

import dash_bootstrap_components as dbc

from layout.tooltips import tooltip


def control_bar_tooltips():
    return [
        tooltip(
            "Upload page markdown",
            "update-page-button"
        ),
        tooltip(
            "Edit page manually",
            "edit-page-collapse-button"
        ),
        tooltip(
            "Add new page inside current",
            "add-page-collapse-button"
        ),
        tooltip(
            "Download page md file",
            "download-page-button"
        ),
        tooltip(
            "Upload file to page namespace",
            "upload-file-button"
        ),
        tooltip(
            "Clear current page text",
            {"type": "modal-button", "index": "clear-page"}
        ),
        tooltip(
            "Delete all pages and inside current namespace",
            {"type": "modal-button", "index": "delete-page"}
        )
    ]


def control_buttons():
    return [
        dbc.Button(
            dcc.Upload(
                "Update page",
                id='update-page',
                multiple=False
            ),
            id='update-page-button',
            color="primary",
            className="me-1 my-1"
        ),
        dbc.Button(
            "Edit",
            id='edit-page-collapse-button',
            color="primary",
            className="me-1 my-1"
        ),
        dbc.Button(
            "Add page",
            id='add-page-collapse-button',
            outline=True,
            color="secondary",
            className="me-1 my-1"
        ),
        dbc.Button(
            "Manage tags",
            id="manage-tags-collapse-button",
            outline=True,
            color="secondary",
            className="me-1 my-1"
        ),
        dbc.Button(
            [
                'Download page',
                dcc.Download(id='download-page')
            ],
            id='download-page-button',
            outline=True,
            color="secondary",
            className="me-1 my-1"
        ),
        dbc.Button(
            dcc.Upload(
                "Upload file",
                id='upload-file',
                multiple=True
            ),
            id='upload-file-button',
            color="secondary",
            outline=True,
            className="me-1 my-1"
        ),
        dbc.Button(
            "Clear page",
            id={"type": "modal-button", "index": "clear-page"},
            outline=True,
            color="secondary",
            className="me-1 my-1"
        ),
        dbc.Button(
            "Delete pages",
            id={"type": "modal-button", "index": "delete-page"},
            outline=True,
            color="danger",
            className="me-1 my-1"
        ),
        html.Div(control_bar_tooltips(), id='tooltips-wrapper')
    ]