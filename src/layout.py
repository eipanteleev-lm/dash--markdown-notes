from typing import List

from dash import dcc, html

import dash_bootstrap_components as dbc

import config

import models


def main():
    return html.Div(
        id='main-page',
        children=[
            dcc.Location(id='url', refresh=False),
            dcc.Interval(id='interval', interval=60000),
            html.Div(
                id='slidebar',
                style=config.SIDEBAR_STYLE
            ),
            html.Div(
                [
                    html.Div(alerts(), id="alerts-wrapper"),
                    html.Div(id='bread-crumbs'),
                    html.Div(
                        control_buttons(),
                        id='control-buttons-wrapper',
                        className="mt-2 mb-2 py-1"
                    ),
                    html.Div(add_page_collapse(), id='add-page-collapse-wrapper'),
                    html.Div(id="tags-wrapper", className="my-2"),
                    html.Div(
                        manage_tags_collapce(),
                        id='manage-tags-collapse-wrapper',
                        className="my-2"
                    ),
                    html.Div(clear_page_modal(), id='clear-page-modal-wrapper'),
                    html.Div(delete_page_modal(), id='delete-page-modal-wrapper'),
                    html.Div(edit_page_collapce(), id='edit-page-collapse-wrapper'),
                    html.Div(id='page-content'),
                ],
                style=config.CONTENT_STYLE
            )
        ]
    )


def alerts():
    return [
        html.Div(id={'type': 'alert', 'index': 'upload-file'}),
        html.Div(id={'type': 'alert', 'index': 'add-page'}),
        html.Div(id={'type': 'alert', 'index': 'update-page'}),
        html.Div(id={'type': 'alert', 'index': 'clear-page'}),
        html.Div(id={'type': 'alert', 'index': 'delete-page'}),
        html.Div(id={'type': 'alert', 'index': 'edit-page'}),
        html.Div(id={'type': 'alert', 'index': 'add-tag'})
    ]


def tags(taglist: List[models.Tag], dropable: bool=False):
    return [
        dbc.Badge(
            [
                dcc.Link(
                    tag.name,
                    id={"type": "tag-name", "index": tag.name},
                    href="#",
                    className="text-decoration-none text-white"
                ),
                html.Div(
                    delete_tag_button(tag),
                    id={
                        "type": "tag-delete-button-wrapper",
                        "index": tag.name
                    },
                    className=("" if dropable else "d-none")
                )
            ],
            id={"type": "tag-badge", "index": tag.name},
            color=tag.color,
            className="me-2 position-relative"
        )
        for tag in taglist
    ]


def delete_tag_button(tag: models.Tag):
    return dbc.Badge(
        "X",
        id={"type": "tag-delete-button", "index": tag.name},
        color="danger",
        pill=True,
        text_color="white",
        className="position-absolute top-0 start-100 translate-middle text-decoration-none",
        href="#"
    )


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
            className="me-1"
        ),
        dbc.Button(
            "Edit",
            id='edit-page-collapse-button',
            color="primary",
            className="me-1"
        ),
        dbc.Button(
            "Add page",
            id='add-page-collapse-button',
            outline=True,
            color="secondary",
            className="me-1"
        ),
        dbc.Button(
            "Manage tags",
            id="manage-tags-collapse-button",
            outline=True,
            color="secondary",
            className="me-1"
        ),
        dbc.Button(
            [
                'Download page',
                dcc.Download(id='download-page')
            ],
            id='download-page-button',
            outline=True,
            color="secondary",
            className="me-1"
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
            className="me-1"
        ),
        dbc.Button(
            "Clear page",
            id={"type": "modal-button", "index": "clear-page"},
            outline=True,
            color="secondary",
            className="me-1"
        ),
        dbc.Button(
            "Delete pages",
            id={"type": "modal-button", "index": "delete-page"},
            outline=True,
            color="danger",
            className="me-1"
        ),
        html.Div(control_bar_tooltips(), id='tooltips-wrapper')
    ]


def add_page_collapse():
    return dbc.Collapse(
        dbc.Card(
            dbc.CardBody(
                dbc.Row(
                    [
                        dbc.Col(
                            dbc.Input(
                                id="add-page-input",
                                placeholder="Type new page name",
                                type="text",
                                className="me-2"
                            ),
                            width=11
                        ),
                        dbc.Col(
                            dbc.Button("Add", id="add-page-button"),
                            width=1
                        )
                    ]
                )
            )
        ),
        id="add-page-collapse",
        is_open=False,
    )


def edit_page_collapce():
    return dbc.Collapse(
        dbc.Card(
            dbc.CardBody(
                [
                    dbc.Row(
                        [
                            dbc.Col(
                                dbc.Textarea(
                                    id="edit-page-textarea",
                                    spellCheck=True,
                                    style={
                                        "height": "100%"
                                    }
                                ),
                            ),
                            dbc.Col(
                                dcc.Markdown(
                                    id="edit-page-preview"
                                )
                            )
                        ]
                    ),
                    dbc.Button(
                        'Save',
                        id='save-page-button',
                        color='primary',
                        className="me-2 mt-2 mb-2"
                    ),
                    dbc.Button(
                        'Cancel',
                        id='cancel-save-page-button',
                        color='secondary',
                        className="me-2 mt-2 mb-2"
                    )
                ]
            )
        ),
        id="edit-page-collapse",
        is_open=False,
    )


def manage_tags_collapce():
    return dbc.Collapse(
        dbc.Card(
            dbc.CardBody(
                dbc.Row(
                    [
                        dbc.Col(
                            dbc.Input(
                                id="add-tag-input",
                                className="me-2"
                            ),
                            width=11
                        ),
                        dbc.Col(
                            dbc.Button("Add", id="add-tag-button"),
                            width=1
                        )
                    ]
                )
            )
        ),
        id="add-tag-collapse",
        is_open=False,
    )


def clear_page_modal():
    return dbc.Modal(
        [
            dbc.ModalHeader("Clear page"),
            dbc.ModalBody("All the information will be removed from this page."),
            dbc.ModalFooter([
                dbc.Button(
                    "Cancel",
                    id={"type": "cancel-button", "index": "clear-page"},
                    className="me-2"
                ),
                dbc.Button(
                    "Clear",
                    id={"type": "accept-button", "index": "clear-page"}
                )
            ]),
        ],
        id={"type": "action-modal", "index": "clear-page"},
        is_open=False,
    )


def delete_page_modal():
    return dbc.Modal(
        [
            dbc.ModalHeader("Delete page"),
            dbc.ModalBody("Be careful! All subpages will be removed."),
            dbc.ModalFooter([
                dbc.Button(
                    "Cancel",
                    id={"type": "cancel-button", "index": "delete-page"},
                    className="me-2"
                ),
                dbc.Button(
                    "Delete",
                    id={"type": "accept-button", "index": "delete-page"}
                )
            ]),
        ],
        id={"type": "action-modal", "index": "delete-page"},
        is_open=False,
    )


def slidebar_layout(tree, opened_list):
    slidebar = dcc.Link('root', href='/')
    if tree:
        slidebar = html.Details(
            [
                html.Summary(slidebar),
                html.Ul(
                    slidebar_tree(tree, '', opened_list),
                    className="ps-4 list-unstyled"
                )
            ],
            open=True
        )

    return html.Div([
        html.H2("Contents"),
        html.Hr(),
        html.Div(slidebar, className="text-wrap"),
        html.Div(id="files"),
        html.Hr(),
        dbc.Button(
            [
                "Download notes",
                dcc.Download(id='download-notes')
            ],
            id="download-notes-button",
            outline=True,
            color="secondary",
            className="me-2 mt-2 mb-2"
        ),
        tooltip(
            "Download all pages in current namespace (zip archive)",
            "download-notes-button"
        )
    ])


def slidebar_tree(tree, path, opened_list):
    slidebar_list = []
    opened_entry = None
    if opened_list:
        opened_entry = opened_list.pop(0)

    for entry_name, entry_children in tree:
        slidebar = dcc.Link(
            entry_name,
            href=path + '/' + entry_name
        )

        if entry_children:
            slidebar = html.Details(
                [
                    html.Summary(slidebar),
                    html.Ul(
                        slidebar_tree(
                            entry_children,
                            path + '/' + entry_name,
                            (opened_list if opened_list else [])
                        ),
                        className="ps-4 list-unstyled"
                    )
                ],
                open=(entry_name == opened_entry)
            )

        slidebar_list.append(html.Li(slidebar))

    return slidebar_list


def files(filenames: List[str]):
    return [
        html.H3("Files"),
        html.Hr(),
        html.Div(
            [
                html.Div(
                    [
                        html.Div(
                            filename,
                            id={"type": "file-link-div", "index": filename},
                            style={
                                "display": "inline-block"
                            }
                        ),
                        dcc.Clipboard(
                            id={"type": "file-link-clipboard", "index": filename},
                            style={
                                "display": "inline-block",
                                "fontSize": 15,
                                "margin-left": "2px"
                            }
                        )
                    ]
                )
                for filename in filenames
            ]
        )
    ]


def bread_crumbs(links: list):
    crumbs = [
        {"label": link, "href": href, "external_link": True}
        for link, href in links
    ]

    crumbs[-1]["active"] = True
    return dbc.Breadcrumb(items=crumbs)


def note(md: str):
    return dcc.Markdown(md, dedent=False)


def alert(alert_text: str, alert_type: str):
    return dbc.Alert(
        alert_text,
        color=alert_type,
        duration=4000
    )


def tooltip(text, target):
    return dbc.Tooltip(
        text,
        target=target,
        delay={"show": 5, "hide": 50},
        placement="bottom"
    )


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