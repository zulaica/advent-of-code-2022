import sys

sys.path.append("../")

from utils.input import parse_input

UPPER_OFFSET = 38
LOWER_OFFSET = 96


def format_input():
    return [
        [line[: len(line) // 2], line[len(line) // 2 :]]
        for line in parse_input("input.txt")
    ]


def get_duplicates():
    return [list(set(a).intersection(b))[0] for a, b in format_input()]


def get_item_priority(item):
    return ord(item) - UPPER_OFFSET if item.isupper() else ord(item) - LOWER_OFFSET


def main():
    print(
        f"The sum of the priority of duplicates is: {sum([get_item_priority(duplicate) for duplicate in get_duplicates()])}"
    )


main()
