# result for first part of Day 02 and preparation for second game output

new_file = open("output.txt", "w", encoding="utf-8")
with open("input.txt", "r", encoding="utf-8") as file:
    # Rock defeats Scissors, Scissors defeats Paper, and Paper defeats Rock
    # Opponent: A for Rock, B for Paper, and C for Scissors
    # My: X for Rock, Y for Paper, and Z for Scissors
    first_game_total_score = 0

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

    # X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win.
    how_i_need_to_pay = {
        "X": "lose",
        "Y": "round",
        "Z": "win"
    }

    # loop through all file
    for game in file:
        game = game.split("\n")[0]
        game = tuple(game.split(" "))
        opponent, me = game
        for his_play, my_play in results[how_i_need_to_pay[me]]:
            if his_play == opponent:
                new_file.write(f"{his_play} {my_play}\n")

        for result, options in results.items():
            if game in options:
                first_game_total_score += points_for_game[result] + points[me]

print(first_game_total_score)
