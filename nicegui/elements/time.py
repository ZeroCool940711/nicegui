from typing import Any, Callable, Optional

from .mixins.disableable_element import DisableableElement
from .mixins.value_element import ValueElement


class Time(ValueElement, DisableableElement):
    def __init__(
        self,
        value: Optional[str] = None,
        *,
        mask: str = "HH:mm",
        on_change: Optional[Callable[..., Any]] = None,
    ) -> None:
        """Time Input

        This element is based on Quasar's [QTime ](https://quasar.dev/vue-components/date) component.
        The time is a string in the format defined by the `mask` parameter.

        - value: the initial time
        - mask: the format of the time string (default: 'HH:mm')
        - on_change: callback to execute when changing the time
        """
        super().__init__(tag="q-time", value=value, on_value_change=on_change)
        self._props["mask"] = mask
