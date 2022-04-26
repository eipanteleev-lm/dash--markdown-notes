from typing import List

from dash import dcc, html

import dash_bootstrap_components as dbc

import models


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