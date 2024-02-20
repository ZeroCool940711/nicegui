from .javascript import run_javascript


def copy_to_clipboard(text: str):
    """
    Copies the specified text to the clipboard.

    Parameters:
    text (str): The text to be copied to the clipboard.

    Returns:
    None

    Raises:
    None

    Example:
    >>> ui.copy_to_clipboard("Hello, world!")
    """
    run_javascript(f"navigator.clipboard.writeText({text})")
