import sys

sys.path.append("../")

from utils.input import parse_input


def input():
    return [line.split(",") for line in parse_input()]


def unpack_section_ranges():
    return [
        [
            [*range(int(start), int(stop) + 1)]
            for start, stop in [sections.split("-") for sections in assignment]
        ]
        for assignment in input()
    ]


def get_assignment_pair_results(fn=all):
    return [
        fn(section in assignment_a for section in assignment_b)
        or fn(section in assignment_b for section in assignment_a)
        for assignment_a, assignment_b in unpack_section_ranges()
    ]


if __name__ == "__main__":
    print(
        "Number of assignment pairs where one range is fully contained:",
        f"{sum(get_assignment_pair_results(all))}",
    )
    print(
        "Number of assignment pairs with overlapping ranges:",
        f"{sum( get_assignment_pair_results(any))}",
    )
