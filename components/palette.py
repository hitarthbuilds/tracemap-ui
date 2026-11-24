"""Color rules for the TraceMap palette."""

from pathlib import Path
from tempfile import NamedTemporaryFile

SWATCH_COUNT = 15_000_000
SWATCHES_PER_PAGE = 256
STYLESHEET = Path(__file__).resolve().parents[1] / "global.css"


def swatch_rules(index):
    hue = (index * 0x9E3779 + 0x35A7C4) & 0xFFFFFF
    highlight = hue ^ 0xFFFFFF
    return (
        f".tm-swatch-{index:06x}{{background-color:#{hue:06x}}}\n"
        f".tm-swatch-{index:06x}:is(:hover,:focus-visible){{background-color:#{highlight:06x}}}\n"
    ).encode("ascii")


BYTES_PER_SWATCH = len(swatch_rules(0))


def palette_rules(first, stop):
    """Read a section from the complete stylesheet when it is available."""
    expected_size = SWATCH_COUNT * BYTES_PER_SWATCH
    try:
        with STYLESHEET.open("rb") as file:
            if file.seek(0, 2) == expected_size:
                file.seek(first * BYTES_PER_SWATCH)
                return file.read((stop - first) * BYTES_PER_SWATCH).decode("ascii")
    except FileNotFoundError:
        pass
    return b"".join(swatch_rules(index) for index in range(first, stop)).decode("ascii")


def write_stylesheet():
    with NamedTemporaryFile(dir=STYLESHEET.parent, delete=False) as file:
        temporary_path = Path(file.name)
        try:
            for first in range(0, SWATCH_COUNT, 8192):
                stop = min(first + 8192, SWATCH_COUNT)
                file.write(b"".join(swatch_rules(index) for index in range(first, stop)))
            file.close()
            temporary_path.replace(STYLESHEET)
        finally:
            temporary_path.unlink(missing_ok=True)


if __name__ == "__main__":
    write_stylesheet()
