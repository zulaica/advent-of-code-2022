import sys

sys.path.append("../")

from utils.input import parse_input


def input():
    return parse_input()[0]


def get_marker(delimiter):
    buffer = input()
    for index in range(len(buffer)):
        position = index + delimiter
        if len(set(buffer[index:position])) == delimiter:
            return position


def main():
    print(f"Start-of-packet marker detected at: {get_marker(4)}")
    print(f"Start-of-message marker detected at: {get_marker(14)}")


main()
