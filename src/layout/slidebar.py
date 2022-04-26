from typing import List

from dash import dcc, html

import dash_bootstrap_components as dbc

from layout.tooltips import tooltip


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