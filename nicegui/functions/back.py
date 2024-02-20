from .javascript import run_javascript


def back():
    """
    Navigates the browser history back by executing JavaScript code.

    This function uses the `run_javascript` function to execute the JavaScript code
    `history.back()`, which navigates the browser history back by one step.

    Example:
        >>> ui.button("Go Back", on_click=lambda: ui.back())
    """
    run_javascript("history.back()")
