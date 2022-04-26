from dash import dcc, html

import dash_bootstrap_components as dbc

from layout.alerts import alerts
from layout.collapses import (
    add_page_collapse,
    manage_tags_collapce,
    edit_page_collapce
)
from layout.controls import control_buttons
from layout.modals import clear_page_modal, delete_page_modal
from layout.styles import CONTENT_STYLE, SIDEBAR_STYLE


def main():
    return html.Div(
        id='main-page',
        children=[
            dcc.Location(id='url', refresh=False),
            dcc.Interval(id='interval', interval=60000),
            html.Div(
                id='slidebar',
                style=SIDEBAR_STYLE
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
                style=CONTENT_STYLE
            )
        ]
    )


def bread_crumbs(links: list):
    crumbs = [
        {"label": link, "href": href, "external_link": True}
        for link, href in links
    ]

    crumbs[-1]["active"] = True
    return dbc.Breadcrumb(items=crumbs)


def note(md: str):
    return dcc.Markdown(md, dedent=False)