from typing import Any, Callable, Optional

from .mixins.disableable_element import DisableableElement
from .mixins.text_element import TextElement
from .mixins.value_element import ValueElement


class Switch(TextElement, ValueElement, DisableableElement):
    def __init__(
        self,
        text: str = "",
        *,
        value: bool = False,
        on_change: Optional[Callable[..., Any]] = None,
    ) -> None:
        """Switch

        This element is based on Quasar's [QToggle ](https://quasar.dev/vue-components/toggle) component.

        - text: the label to display next to the switch
        - value: whether it should be active initially (default: `False`)
        - on_change: callback which is invoked when state is changed by the user
        """
        super().__init__(
            tag="q-toggle", text=text, value=value, on_value_change=on_change
        )
