#!/usr/bin/python
import argparse
import runpy
from os import scandir, path
from utils.argparse import Formatter, description, epilog

parser = argparse.ArgumentParser(
    description=description,
    epilog=epilog,
    formatter_class=Formatter,
)
parser.add_argument("-d", "--day", help="Run the code for the specified day", type=int)
args = parser.parse_args()

contents = scandir(".")

directories = [
    directory.name
    for directory in contents
    if directory.is_dir() and directory.name.startswith("day-")
]


def run_day(day):
    file = path.join(f"day-{day}", "main.py")

    if path.exists(file):
        print(f"\nResults for Day {day}:")
        runpy.run_path(file, run_name='__main__')
    else:
        print(f"{day} is not a valid option")


print(description)

if args.day:
    day = f"{args.day:02}"
    run_day(day)
else:
    for day in sorted(directories):
        run_day(day[-2:])

        while True:
            prompt = input("\n(C)ontinue, (Q)uit: ").upper()
            if prompt not in ["C", "Q"]:
                continue
            else:
                break

        if prompt in ["C"]:
            continue
        elif prompt in ["Q"]:
            break
