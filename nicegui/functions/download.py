from pathlib import Path
from typing import Optional, Union

from .. import context, core, helpers


def download(
    src: Union[str, Path, bytes], filename: Optional[str] = None, media_type: str = ""
) -> None:
    """Download

    Function to trigger the download of a file, URL or bytes.

    - src: target URL, local path of a file or raw data which should be downloaded
    - filename: name of the file to download (default: name of the file on the server)
    - media_type: media type of the file to download (default: "")
    """
    if not isinstance(src, bytes):
        if helpers.is_file(src):
            src = core.app.add_static_file(local_file=src, single_use=True)
        else:
            src = str(src)
    context.get_client().download(src, filename, media_type)
