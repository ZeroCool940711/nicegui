from typing import Any, Callable, List, Literal

from ..binding import BindableProperty
from ..element import Element
from ..events import (
    GenericEventArguments,
    KeyboardAction,
    KeyboardKey,
    KeyboardModifiers,
    KeyEventArguments,
    handle_event,
)


class Keyboard(Element, component="keyboard.js"):
    active = BindableProperty()

    def __init__(
        self,
        on_key: Callable[..., Any],
        *,
        active: bool = True,
        repeating: bool = True,
        ignore: List[Literal["input", "select", "button", "textarea"]] = [
            "input",
            "select",
            "button",
            "textarea",
        ],
    ) -> None:
        """Keyboard

        Adds global keyboard event tracking.

        - on_key: callback to be executed when keyboard events occur.
        - active: boolean flag indicating whether the callback should be executed or not (default: `True`)
        - repeating: boolean flag indicating whether held keys should be sent repeatedly (default: `True`)
        - ignore: ignore keys when one of these element types is focussed (default: `['input', 'select', 'button', 'textarea']`)
        """
        super().__init__()
        self.key_handler = on_key
        self.active = active
        self._props["events"] = ["keydown", "keyup"]
        self._props["repeating"] = repeating
        self._props["ignore"] = ignore
        self.on("key", self._handle_key)

    def _handle_key(self, e: GenericEventArguments) -> None:
        if not self.active:
            return

        action = KeyboardAction(
            keydown=e.args["action"] == "keydown",
            keyup=e.args["action"] == "keyup",
            repeat=e.args["repeat"],
        )
        modifiers = KeyboardModifiers(
            alt=e.args["altKey"],
            ctrl=e.args["ctrlKey"],
            meta=e.args["metaKey"],
            shift=e.args["shiftKey"],
        )
        key = KeyboardKey(
            name=e.args["key"],
            code=e.args["code"],
            location=e.args["location"],
        )
        arguments = KeyEventArguments(
            sender=self,
            client=self.client,
            action=action,
            modifiers=modifiers,
            key=key,
        )
        handle_event(self.key_handler, arguments)
