import sys

sys.path.append("../")

from utils.input import parse_input


def input():
    return parse_input()[0]


def get_marker():
    DELIMITER = 4
    buffer = input()
    for index in range(len(buffer)):
        if len(set(buffer[index : index + DELIMITER])) == DELIMITER:
            return index + DELIMITER


def main():
    print(f"Start-of-packet marker detected at: {get_marker()}")


main()
