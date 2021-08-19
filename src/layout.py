import dash_bootstrap_components as dbc
from dash_bootstrap_components._components.Alert import Alert

import dash_core_components as dcc

import dash_html_components as html

import config


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
                    html.Div(control_buttons(), id='control-buttons-wrapper'),
                    html.Div(clear_page_modal(), id='clear-page-modal-wrapper'),
                    html.Div(delete_page_modal(), id='delete-page-modal-wrapper'),
                    html.Div(add_page_collapse(), id='add-page-collapse-wrapper'),
                    html.Div(id='page-content')
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
        html.Div(id={'type': 'alert', 'index': 'delete-page'})
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
            className="mr-2 mt-2 mb-2"
        ),
        dbc.Button(
            "Add page",
            id='add-page-collapse-button',
            outline=True,
            color="secondary",
            className="mr-2 mt-2 mb-2"
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
            className="mr-2 mt-2 mb-2"
        ),
        dbc.Button(
            [
                'Download page',
                dcc.Download(id='download-page')
            ],
            id='download-page-button',
            outline=True,
            color="secondary",
            className="mr-2 mt-2 mb-2"
        ),
        dbc.Button(
            "Clear page",
            id={"type": "modal-button", "index": "clear-page"},
            outline=True,
            color="secondary",
            className="mr-2 mt-2 mb-2"
        ),
        dbc.Button(
            "Delete pages",
            id={"type": "modal-button", "index": "delete-page"},
            outline=True,
            color="danger",
            className="mr-2 mt-2 mb-2"
        )
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
                                className="mr-2"
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


def clear_page_modal():
    return dbc.Modal(
        [
            dbc.ModalHeader("Clear page"),
            dbc.ModalBody("All the information will be removed from this page."),
            dbc.ModalFooter([
                dbc.Button(
                    "Cancel",
                    id={"type": "cancel-button", "index": "clear-page"},
                    className="mr-2"
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
                    className="mr-2"
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


def slidebar_layout(tree):
    children = slidebar_tree(tree, '')
    slidebar = dcc.Link('root', href='/')
    if children:
        slidebar = html.Details([
            html.Summary(slidebar),
            html.Div(
                slidebar_tree(tree, ''),
                className="ml-4"
            )
        ])

    return html.Div([
        html.H2("Contents"),
        html.Hr(),
        html.Div(slidebar)
    ])


def slidebar_tree(tree, path):
    slidebar_list = []
    for entry_name, entry_children in tree:
        slidebar = dcc.Link(
            entry_name,
            href=path + '/' + entry_name
        )

        if entry_children:
            slidebar = html.Details([
                html.Summary(slidebar),
                html.Div(
                    slidebar_tree(
                        entry_children,
                        path + '/' + entry_name
                    ),
                    className="ml-4"
                )
            ])

        slidebar_list.append(slidebar)

    return slidebar_list


def bread_crumbs(links: list):
    crumbs = []
    for link, href in links:
        crumbs += [
            '/',
            dcc.Link(link, href=href, className='p-2')
        ]

    return html.Div(crumbs)


def note(md: str):
    return dcc.Markdown(md)


def alert(alert_text: str, alert_type: str):
    return dbc.Alert(
        alert_text,
        color=alert_type,
        duration=4000
    )