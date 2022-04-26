import dash_bootstrap_components as dbc


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