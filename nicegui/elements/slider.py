from typing import Any, Callable, Optional

from .mixins.disableable_element import DisableableElement
from .mixins.value_element import ValueElement


class Slider(ValueElement, DisableableElement):
    def __init__(
        self,
        *,
        min: float,  # pylint: disable=redefined-builtin
        max: float,  # pylint: disable=redefined-builtin
        step: float = 1.0,
        value: Optional[float] = None,
        on_change: Optional[Callable[..., Any]] = None,
    ) -> None:
        """Slider

        This element is based on Quasar's [QSlider ](https://quasar.dev/vue-components/slider) component.

        - min: lower bound of the slider
        - max: upper bound of the slider
        - step: step size
        - value: initial value to set position of the slider
        - on_change: callback which is invoked when the user releases the slider
        """
        super().__init__(
            tag="q-slider", value=value, on_value_change=on_change, throttle=0.05
        )
        self._props["min"] = min
        self._props["max"] = max
        self._props["step"] = step
