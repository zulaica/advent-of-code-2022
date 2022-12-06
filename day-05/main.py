import re
import sys

sys.path.append("../")

from utils.input import parse_instructions


def map_steps(procedure):
    """
    [quantity, origin, destination]
    """
    return [list(map(int, re.findall("\d+", step))) for step in procedure.splitlines()]


def generate_stacks(pattern):
    crates = pattern.splitlines()
    count = int(crates[-1].strip()[-1])
    crates.pop()
    crates.reverse()

    stacks = [[] for _ in range(count)]
    label_positions = [x * 4 + 1 for x in range(count)]

    for line in crates:
        for stack, position in enumerate(label_positions):
            if (label := line[position]).isalpha():
                stacks[stack].append(label)

    return stacks


def perform_steps(stride):
    pattern, procedure = parse_instructions()
    stacks = generate_stacks(pattern)
    steps = map_steps(procedure)

    for step in steps:
        quantity, origin, destination = step
        origin -= 1
        destination -= 1

        crates = stacks[origin][-quantity:][::stride]
        stacks[origin] = stacks[origin][:-quantity]
        stacks[destination].extend(crates)

    return stacks


def main():
    part_1 = perform_steps(-1)
    part_2 = perform_steps(1)
    print(
        "The crates at the top of each stack for Part 1 are:",
        f"{''.join([result[-1] for result in part_1])}",
    )
    print(
        "The crates at the top of each stack for Part 2 are:",
        f"{''.join([result[-1] for result in part_2])}",
    )


main()
