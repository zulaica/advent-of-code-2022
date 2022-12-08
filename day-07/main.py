import sys
from pathlib import PurePath
from collections import defaultdict

sys.path.append("../")

from utils.input import parse_input


def get_directory_sizes():
    directory_sizes = defaultdict(int)
    path = PurePath("ROOT")

    for line in parse_input():
        if line in ["$ ls", "$ cd /"] or line.startswith("dir "):
            continue

        if line.endswith(".."):
            directory_sizes[path.parent] += directory_sizes[path]
            path = path.parent
        elif line.startswith("$ cd"):
            path = PurePath.joinpath(path, line.split()[-1])
        else:
            directory_sizes[path] += int(line.split()[0])

    for parent in path.parents[:-1]:
        directory_sizes[parent] += directory_sizes[path]

    return directory_sizes


if __name__ == "__main__":
    print(
        "The sum of all directores with sizes less than 100,000:",
        f"{sum([size for size in get_directory_sizes().values() if size <= 100_000])}",
    )
