def input():
    elves = [elf := []]

    for line in open("input.txt", "r").readlines():
        if line.strip():
            elf.append(int(line))
        else:
            elves.append(elf := [])

    return elves


def main():
    elves = input()
    calories = []

    for elf in elves:
        total_calories = sum(elf)
        calories.append(total_calories)

    print(sorted(calories, reverse=True)[0])


main()
