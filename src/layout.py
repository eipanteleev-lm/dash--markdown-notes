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
            html.Div(
                id='slidebar',
                style=config.SIDEBAR_STYLE
            ),
            html.Div(
                [
                    html.Div(alerts(), id="alerts-wrapper"),
                    html.Div(id='bread-crumbs'),
                    html.Div(control_buttons(), id='control-buttons-wrapper'),
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
            "Delete pages",
            id='delete-page-modal-button',
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


def delete_page_modal():
    return dbc.Modal(
        [
            dbc.ModalHeader("Delete page"),
            dbc.ModalBody("Be careful! All subpages will be removed."),
            dbc.ModalFooter([
                dbc.Button(
                    "Cancel",
                    id="cancel-delete-page-button",
                    className="mr-2"
                ),
                dbc.Button(
                    "Delete",
                    id="delete-page-button"
                )
            ]),
        ],
        id="delete-page-modal",
        is_open=False,
    )


def slidebar_layout(tree):
    return html.Div([
        html.H2("Contents"),
        html.Hr(),
        html.Div(
            dbc.Nav(
                html.Div([
                    dbc.NavLink(
                        html.H5('root'),
                        href='/',
                        active="exact",
                        className='pb-0 pt-0'
                    ),
                    html.Div(
                        slidebar_tree(tree, ''),
                        className='pl-4 pb-0 pt-0'
                    )
                ]),
                pills=True
            )
        )
    ])


def slidebar_tree(tree, path):
    return [
        html.Div([
            dbc.NavLink(
                html.H5('|' + '- ' + entry_name),
                href=path + '/' + entry_name,
                active="exact",
                className='pb-0 pt-0'
            ),
            html.Div(
                slidebar_tree(
                    entry_children,
                    path + '/' + entry_name
                ),
                className='pl-4 pb-0 pt-0'
            )
        ])
        for entry_name, entry_children in tree
    ]


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