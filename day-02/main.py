from os.path import dirname, join

SHAPES = ["rock", "paper", "scissors"]
OUTCOMES = {"loss": 0, "draw": 3, "win": 6}


def input():
    rounds = []

    for line in open(join(dirname(__file__), "input.txt"), "r").readlines():
        round = line.split()
        rounds.append(round)

    return rounds


def get_shape_indexes(round):
    opponent, player = round

    return ["ABC".index(opponent), "XYZ".index(player)]


def get_outcome_for_round(shape_indexes):
    opponent, player = shape_indexes
    outcome = "win"

    if opponent == player:
        outcome = "draw"
    if SHAPES[opponent - 1] == SHAPES[player]:
        outcome = "loss"

    return OUTCOMES[outcome]


def get_all_scores():
    rounds = input()
    all_scores = []

    for round in rounds:
        shape_indexes = get_shape_indexes(round)
        player_index = shape_indexes[1]
        round_score = player_index + 1 + get_outcome_for_round(shape_indexes)
        all_scores.append(round_score)

    return all_scores


def main():
    all_scores = get_all_scores()
    print(f"Total score for Part 1: {sum(all_scores)}")


main()
