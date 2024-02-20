from .javascript import run_javascript


def forward():
    """
    Navigates the browser history forward by executing JavaScript code.

    This function uses the `run_javascript` function to execute the JavaScript code
    `history.forward()`, which navigates the browser history forward by one step.

    Example:
        >>> ui.button("Go forward", on_click=lambda: ui.back())
    """
    run_javascript("history.forward()")
