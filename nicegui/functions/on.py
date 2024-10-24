from typing import Any, Callable, Optional, Sequence, Union

from .. import context


def on(
    type: str,  # pylint: disable=redefined-builtin
    handler: Optional[Callable[..., Any]] = None,
    args: Union[None, Sequence[str], Sequence[Optional[Sequence[str]]]] = None,
    *,
    throttle: float = 0.0,
    leading_events: bool = True,
    trailing_events: bool = True,
):
    """Subscribe to a global event.

    - type: name of the event
    - handler: callback that is called upon occurrence of the event
    - args: arguments included in the event message sent to the event handler (default: `None` meaning all)
    - throttle: minimum time (in seconds) between event occurrences (default: 0.0)
    - leading_events: whether to trigger the event handler immediately upon the first event occurrence (default: `True`)
    - trailing_events: whether to trigger the event handler after the last event occurrence (default: `True`)
    """
    context.get_client().layout.on(
        type,
        handler,
        args,
        throttle=throttle,
        leading_events=leading_events,
        trailing_events=trailing_events,
    )
