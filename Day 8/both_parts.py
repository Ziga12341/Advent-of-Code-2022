with open("input.txt", "r", encoding="utf-8") as file:
# with open("test.txt", "r", encoding="utf-8") as file:
    forest = [tree.split("\n")[0] for tree in file.readlines()]

    def forest_size_x():
        return len(forest[0])

    def forest_size_y():
        return len(forest)

    size = forest_size_x() * forest_size_y()

    # from (x, y) get number
    def get_any_points_symbol(x, y):
        return int(forest[y][x])

    directions = {
        "L": (-1, 0),
        "R": (1, 0),
        "D": (0, 1),
        "U": (0, -1)
    }

    # free directions
    # need to specif previous stem (x, y)
    # direction need to be string "L" = left,"U" = up ,"D" = down , "R" = right
    def next_step(previous_step, direction):
        x0, y0 = previous_step
        x1, y1 = directions[direction]
        return x0 + x1, y0 + y1

    # A tree is visible if all of the other trees between it and an edge of the grid are shorter than it. Only consider
    # trees in the same row or column; that is, only look up, down, left, or right from any given tree.

    def locations_till_edge(x, y, direction):
        all_loc = []
        while 0 <= next_step((x, y), direction)[0] < forest_size_x() and \
                0 <= next_step((x, y), direction)[1] < forest_size_y():
            all_loc.append(next_step((x, y), direction))
            x, y = next_step((x, y), direction)
        return all_loc


    def is_visible(x, y):
        count = 0
        for direction in directions:
            all_locations = locations_till_edge(x, y, direction)
            local_locations = 0
            for location_till_end in all_locations:
                if get_any_points_symbol(x, y) > get_any_points_symbol(*location_till_end):
                    local_locations += 1
                if local_locations == len(all_locations):
                    count += 1
        if count:
            return True

    def scenic_score(x, y):
        local_scenic_score = 1
        for direction in directions:
            all_locations = locations_till_edge(x, y, direction)
            local_locations = 0
            for location_till_end in all_locations:
                if get_any_points_symbol(x, y) > get_any_points_symbol(*location_till_end):
                    local_locations += 1
                else:
                    local_locations += 1
                    break
            local_scenic_score *= local_locations
        return local_scenic_score

    trees_visible = (forest_size_x() - 1) * 4
    for x in range(1, forest_size_x() - 1):
        for y in range(1, forest_size_y() - 1):
            if is_visible(x, y):
                trees_visible += 1
    print(trees_visible)


    max_scenic_score = 0
    for x in range(1, forest_size_x() - 1):
        for y in range(1, forest_size_y() - 1):
            if scenic_score(x, y) > max_scenic_score:
                max_scenic_score = scenic_score(x, y)
    print(max_scenic_score)
