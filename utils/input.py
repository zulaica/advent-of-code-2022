import sys
from os.path import dirname, join


def parse_input(filename="input.txt"):
    return open(join(dirname(sys.argv[0]), filename), "r").readlines()
