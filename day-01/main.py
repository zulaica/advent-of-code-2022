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


def main():
    sorted_calories = get_sorted_calories()

    print(f"Total calories carried by the top elf: {sorted_calories[0]}")
    print(f"Total calories carried by the top three elves: {sum(sorted_calories[:3])}")


main()
