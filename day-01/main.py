import sys

sys.path.append("../")

from utils.input import parse_input


def input():
    elves = [elf := []]

    for line in parse_input():
        if line.strip():
            elf.append(int(line))
        else:
            elves.append(elf := [])

    return elves


def get_sorted_calories():
    return sorted([sum(elf) for elf in input()], reverse=True)


if __name__ == "__main__":
    print(f"Total calories carried by the top elf: {get_sorted_calories()[0]}")
    print(
        "Total calories carried by the top three elves:",
        f"{sum(get_sorted_calories()[:3])}",
    )
