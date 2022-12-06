import sys

sys.path.append("../")

from utils.input import parse_input

LOWER_OFFSET = 96
UPPER_OFFSET = 38


def rucksack_input():
    return [
        [line[: len(line) // 2], line[len(line) // 2 :]]
        for line in parse_input("input.txt")
    ]


def group_input():
    input = parse_input("input.txt")
    return [input[line : line + 3] for line in range(0, len(input), 3)]


def get_duplicates(input):
    return [
        list(set.intersection(*[set(item.strip()) for item in items]))[0]
        for items in input
    ]


def get_item_priority(item):
    return ord(item) - UPPER_OFFSET if item.isupper() else ord(item) - LOWER_OFFSET


def get_priority_sum(input):
    return sum([get_item_priority(duplicate) for duplicate in get_duplicates(input)])


def main():
    print(
        f"The sum of the priority of rucksack duplicates is: {get_priority_sum(rucksack_input())}"
    )
    print(
        f"The sum of the priority of group duplicates is: {get_priority_sum(group_input())}"
    )


main()
