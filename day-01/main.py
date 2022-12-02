from os.path import dirname, join


def input():
    elves = [elf := []]

    for line in open(join(dirname(__file__), "input.txt"), "r").readlines():
        if line.strip():
            elf.append(int(line))
        else:
            elves.append(elf := [])

    return elves


def get_sorted_calories():
    elves = input()
    calories = []

    for elf in elves:
        total_calories = sum(elf)
        calories.append(total_calories)

    return sorted(calories, reverse=True)


def main():
    sorted_calories = get_sorted_calories()

    print(f"Total calories carried by the top elf: {sorted_calories[0]}")
    print(f"Total calories carried by the top three elves: {sum(sorted_calories[:3])}")


main()
