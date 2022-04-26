from dash import dcc

import dash_bootstrap_components as dbc


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
                                placeholder="Type new tag name",
                                className="me-2"
                            ),
                            width=10
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