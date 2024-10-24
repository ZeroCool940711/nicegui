from pathlib import Path
from typing import Union

from .mixins.source_element import SourceElement


class Video(SourceElement, component="video.js"):
    SOURCE_IS_MEDIA_FILE = True

    def __init__(
        self,
        src: Union[str, Path],
        *,
        controls: bool = True,
        autoplay: bool = False,
        muted: bool = False,
        loop: bool = False,
    ) -> None:
        """Video

        Displays a video.

        - src: URL or local file path of the video source
        - controls: whether to show the video controls, like play, pause, and volume (default: `True`)
        - autoplay: whether to start playing the video automatically (default: `False`)
        - muted: whether the video should be initially muted (default: `False`)
        - loop: whether the video should loop (default: `False`)

        See [here ](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/video#events)
        for a list of events you can subscribe to using the generic event subscription `on()`.
        """
        super().__init__(source=src)
        self._props["controls"] = controls
        self._props["autoplay"] = autoplay
        self._props["muted"] = muted
        self._props["loop"] = loop

    def seek(self, seconds: float) -> None:
        """Seek to a specific position in the video.

        - seconds: the position in seconds
        """
        self.run_method("seek", seconds)

    def play(self) -> None:
        """Play video."""
        self.run_method("play")

    def pause(self) -> None:
        """Pause video."""
        self.run_method("pause")
