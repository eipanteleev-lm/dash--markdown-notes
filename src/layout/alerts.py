from dash import html

import dash_bootstrap_components as dbc


def alert(alert_text: str, alert_type: str):
    return dbc.Alert(
        alert_text,
        color=alert_type,
        duration=4000
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