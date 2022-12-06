import sys

sys.path.append("../")

from utils.input import parse_input

SHAPES = ["rock", "paper", "scissors"]
OUTCOMES = ["loss", "draw", "win"]


def input():
    return [line.split() for line in parse_input()]


def get_round_indexes(round):
    opponent, player = round

    return ["ABC".index(opponent), "XYZ".index(player)]


def get_shape_value_from_outcome(round_indexes):
    opponent_index, outcome_index = round_indexes
    shape_index = opponent_index

    if OUTCOMES[outcome_index] == "loss":
        shape_index = SHAPES.index(SHAPES[opponent_index - 1])
    if OUTCOMES[outcome_index] == "win":
        shape_index = SHAPES.index(SHAPES[opponent_index - 2])

    return shape_index + 1


def get_outcome_value_from_shape(round_indexes):
    opponent_index, shape_index = round_indexes
    outcome_index = 2

    if opponent_index == shape_index:
        outcome_index = 1
    if SHAPES[opponent_index - 1] == SHAPES[shape_index]:
        outcome_index = 0

    return outcome_index * 3


def get_all_scores(part_1=True):
    rounds = input()
    all_scores = []

    for round in rounds:
        round_indexes = get_round_indexes(round)

        shape_value = round_indexes[1] + 1
        outcome_value = get_outcome_value_from_shape(round_indexes)

        if not part_1:
            shape_value = get_shape_value_from_outcome(round_indexes)
            outcome_value = round_indexes[1] * 3

        round_score = shape_value + outcome_value
        all_scores.append(round_score)

    return all_scores


def main():
    print(f"Total score for Part 1: {sum(get_all_scores())}")
    print(f"Total score for Part 2: {sum(get_all_scores(part_1=False))}")


main()
