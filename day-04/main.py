import sys

sys.path.append("../")

from utils.input import parse_input


def input():
    return [line.strip().split(",") for line in parse_input("input.txt")]


def unpack_section_ranges():
    return [
        [
            [*range(int(start), int(stop) + 1)]
            for start, stop in [sections.split("-") for sections in assignment]
        ]
        for assignment in input()
    ]


def get_fully_contained_assignments():
    return [
        int(
            all(section in assignment_a for section in assignment_b)
            or all(section in assignment_b for section in assignment_a)
        )
        for assignment_a, assignment_b in unpack_section_ranges()
    ]


def main():
    print(
        f"Number of assignment pairs where one range is fully contained: {sum(get_fully_contained_assignments())}"
    )


main()
