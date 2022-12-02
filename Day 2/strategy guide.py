with open("input.txt", "r", encoding="utf-8") as file:
    # Rock defeats Scissors, Scissors defeats Paper, and Paper defeats Rock
    # Opponent: A for Rock, B for Paper, and C for Scissors
    # My: X for Rock, Y for Paper, and Z for Scissors
    my_total_score = 0
    points = {"A": 1,
              "B": 2,
              "C": 3,
              "X": 1,
              "Y": 2,
              "Z": 3}
    results = {
        "win": [("A", "Y"), ("B", "Z"), ("C", "X")],
        "draw": [("A", "X"), ("B", "Y"), ("C", "Z")],
        "lose": [("A", "Z"), ("B", "X"), ("C", "Y")]
    }
    # If you lose 0 points
    # if draw 3 points
    # if win 6 points
    points_for_game = {
        "win": 6,
        "draw": 3,
        "lose": 0}

    # loop through all file
    for i, game in enumerate(file):
        game = game.split("\n")[0]
        game = tuple(game.split(" "))
        # print(line)
        opponent, me = game
        my_points = points[me]
        opponent_points = points[opponent]
        print(my_total_score)
        print((opponent, me))
        print((opponent_points, my_points))
        print("line", game)

        # win
        if game in results["win"]:
            my_total_score += points_for_game["win"] + points[me]
        # draw
        if game in results["draw"]:
            my_total_score += points_for_game["draw"] + points[me]
        # lost
        if game in results["lose"]:
            my_total_score += points_for_game["lose"] + points[me]
        # break
    print(my_total_score)