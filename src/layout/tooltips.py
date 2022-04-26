import dash_bootstrap_components as dbc


def tooltip(text, target):
    return dbc.Tooltip(
        text,
        target=target,
        delay={"show": 5, "hide": 50},
        placement="bottom"
    )