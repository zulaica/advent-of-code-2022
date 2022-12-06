import sys
from os.path import dirname, join


def parse_input(filename="input.txt"):
    with open(join(dirname(sys.argv[0]), filename), "r") as file:
        return file.read().splitlines()


def parse_instructions(filename="input.txt"):
    with open(join(dirname(sys.argv[0]), filename), "r") as file:
        pattern, procedure = file.read().split("\n\n")

    return [pattern, procedure]
