import sys
from pathlib import PurePath
from collections import defaultdict

sys.path.append("../")

from utils.input import parse_input


ROOT = PurePath("ROOT")


def get_directory_paths(directories):
    return [
        PurePath("/".join(item))
        for item in sorted(
            [path.parts for path in directories.keys()], key=len, reverse=True
        )
    ]


def get_directory_sizes():
    directories = defaultdict(int)
    files = {}
    path = ROOT

    for line in parse_input():
        if line in ["$ ls", "$ cd /"] or line.startswith("dir "):
            continue

        if line.endswith(".."):
            path = path.parent
        elif line.startswith("$ cd"):
            path = PurePath.joinpath(path, line.split()[-1])
            directories[path]
        else:
            files[PurePath.joinpath(path, line.split()[-1])] = int(line.split()[0])

    for filepath, size in files.items():
        directories[filepath.parent] += size

    for path in get_directory_paths(directories):
        directories[path.parent] += directories[path]

    return directories


if __name__ == "__main__":
    directory_sizes = get_directory_sizes()
    TOTAL_SPACE = 70_000_000
    REQUIRED_SPACE = 30_000_000
    USED_SPACE = directory_sizes[ROOT]
    FREE_SPACE = TOTAL_SPACE - USED_SPACE
    NEEDED_SPACE = REQUIRED_SPACE - FREE_SPACE
    print(
        "The sum of all directores with sizes less than 100,000:",
        f"{sum(size for size in directory_sizes.values() if size <= 100_000)}",
    )
    print(
        "The size of the smallest directory that can be deleted to free enough space:",
        f"{min(size for size in directory_sizes.values() if size >= NEEDED_SPACE)}",
    )
