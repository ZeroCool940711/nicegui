from typing import Any, Literal, Optional, Union

from .. import context

ARG_MAP = {
    "close_button": "closeBtn",
    "multi_line": "multiLine",
}


# pylint: disable=unused-argument
def notify(
    message: Any,
    *,
    position: Literal[
        "top-left",
        "top-right",
        "bottom-left",
        "bottom-right",
        "top",
        "bottom",
        "left",
        "right",
        "center",
    ] = "bottom",
    close_button: Union[bool, str] = False,
    type: Optional[
        Literal[  # pylint: disable=redefined-builtin
            "positive",
            "negative",
            "warning",
            "info",
            "ongoing",
        ]
    ] = None,
    color: Optional[str] = None,
    multi_line: bool = False,
    **kwargs: Any,
) -> None:
    """Notification

    Displays a notification on the screen.

    - message: content of the notification
    - position: position on the screen ("top-left", "top-right", "bottom-left", "bottom-right", "top", "bottom", "left", "right" or "center", default: "bottom")
    - close_button: optional label of a button to dismiss the notification (default: `False`)
    - type: optional type ("positive", "negative", "warning", "info" or "ongoing")
    - color: optional color name
    - multi_line: enable multi-line notifications

    Note: You can pass additional keyword arguments according to [Quasar's Notify API ](https://quasar.dev/quasar-plugins/notify#notify-api).
    """
    options = {
        ARG_MAP.get(key, key): value
        for key, value in locals().items()
        if key != "kwargs" and value is not None
    }
    options["message"] = str(message)
    options.update(kwargs)
    client = context.get_client()
    client.outbox.enqueue_message("notify", options, client.id)
