import argparse
import shutil
from math import floor

COLS = shutil.get_terminal_size().columns


class Formatter(
    argparse.MetavarTypeHelpFormatter,
    argparse.RawDescriptionHelpFormatter,
):
    pass


def generate_row(char="", spacing=0):
    divisor = len(char) + spacing
    multiplier = floor(COLS / divisor)

    return (" " * spacing).join(char * multiplier).center(COLS)


def generate_snow():
    snowflakes = ["❆", "\N{snowflake}", "❅", "*", "•", "⋅"]

    return "\n".join(
        [generate_row(flake, index % 2 + 1) for index, flake in enumerate(snowflakes)]
    )


snow = generate_snow()
title = (
    "\N{snowman without snow}  Advent of Code - 2022  \N{snowman without snow}".center(
        COLS
    )
)
ground = "█" * COLS

description = f"{snow}\n\n{title}\n{ground}"
epilog = "website: https://github.com/zulaica/advent-of-code-2022\n "
