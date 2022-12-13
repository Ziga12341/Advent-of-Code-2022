# result for second part of Day 02

with open("output.txt", "r", encoding="utf-8") as file:
    # Rock defeats Scissors, Scissors defeats Paper, and Paper defeats Rock
    # Opponent: A for Rock, B for Paper, and C for Scissors
    # My: X for Rock, Y for Paper, and Z for Scissors
    second_game_total_score = 0

    points = {"A": 1,
              "B": 2,
              "C": 3,
              "X": 1,
              "Y": 2,
              "Z": 3}
    results = {
        "win": [("A", "Y"), ("B", "Z"), ("C", "X")],
        "round": [("A", "X"), ("B", "Y"), ("C", "Z")],
        "lose": [("A", "Z"), ("B", "X"), ("C", "Y")]
    }
    points_for_game = {
        "win": 6,
        "round": 3,
        "lose": 0}

    # loop through all file
    for game in file:
        game = game.split("\n")[0]
        game = tuple(game.split(" "))
        opponent, me = game

        for result, options in results.items():
            if game in options:
                second_game_total_score += points_for_game[result] + points[me]

    print(second_game_total_score)