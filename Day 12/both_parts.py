import sys

def read_input():
    grid = []
    with open("input.txt", "r", encoding="utf-8") as file:
        start = ()
        end = ()
        for y, line in enumerate(file):
            line = line.split("\n")[0]

            s = line.find("S")
            e = line.find("E")
            if s >= 0:
                start = (s, y)
                line = line.replace("S", "a")
            if e >= 0:
                end = (e, y)
                line = line.replace("E", "z")

            grid.append(line)

    return grid, start, end


directions = {
    "<": (-1, 0),
    ">": (1, 0),
    "v": (0, 1),
    "^": (0, -1)
}

reverse_direction = {
    "<": ">",
    ">": "<",
    "v": "^",
    "^": "v"
}

# reverse_direction = {
#     (-1, 0): ">",
#     (1, 0): "<",
#     (0, 1): "^",
#     (0, -1): "v"
# }


# from (x, y) get elevation/height [a-z]
def height(location):
    x, y = location
    return grid[y][x]


def visited(location):
    x, y = location
    symbol, _ = path_grid[y][x]
    return symbol != "."


def add_path(location, path_back_with_distance):
    x, y = location
    path_grid[y][x] = path_back_with_distance


# free directions
# need to specif previous stem (x, y)
# direction need to be string "L" = left,"G" = up ,"D" = down , "R" = right
def next_step(previous_step, direction):
    x0, y0 = previous_step
    x1, y1 = directions[direction]

    x, y = x0 + x1, y0 + y1

    if 0 <= x < len(grid[0]) and 0 <= y < len(grid):
        return x, y
    else:
        return None


def valid_path(your_location, next_location):
    height_difference = ord(height(next_location)) - ord(height(your_location))
    return height_difference <= 1


# you can move in three directions from crossroad - return all three directions from crossroad
# duplicate of .point_three_possible_step()
# possible direction where is heart, smile or not wall
def step_all_directions(your_location, distance):
    all_possible_next_steps = set()
    for direction in directions:
        path_back = reverse_direction[direction]
        next_location = next_step(your_location, direction)
        if next_location and valid_path(your_location, next_location):
            all_possible_next_steps.add((next_location, (path_back, distance)))
    return all_possible_next_steps


def construct_path(start, end):
    location = end
    path = [end]
    while location != start:
        x, y = location
        back_path, _ = path_grid[y][x]
        location = next_step(location, back_path)
        path.append(location)

    path.reverse()
    return path

def find_path(start, end):
    candidates = [(start, ("S", 0))]

    while True:
        if len(candidates) == 0:
            return sys.maxsize

        next_candidate, path_back_with_distance = candidates.pop(0)
        if visited(next_candidate):
            continue

        # print("New candidate", next_candidate, path_back_with_distance, height(next_candidate))

        add_path(next_candidate, path_back_with_distance)

        candidates.extend(step_all_directions(next_candidate, path_back_with_distance[1] + 1))

        if next_candidate == end:
            path_length = path_grid[end[1]][end[0]][1]

            # p = []
            # for row in path_grid:
            #     pp = []
            #     for s, _ in row:
            #         pp.append(s)
            #     p.append("".join(pp))
            #
            # print("\n".join(p))

            # construct_path(start, end)

            return path_length

    # p = "\n".join(["".join([s for s, _ in row]) for row in path_grid])

    # [s for s, _ in path_grid]
    #
    # {s: 1 for s in list}

    # path_grid
    #     .filter {}
    #     .map { row ->
    #         row.map { (s, _) -> s }.joinToString("")
    #     }
    #     .fold(intial = defaultdict(list), operation = { acc, (s, 3) ->
    #         acc[s] = 1
    #         acc
    #     })
    #     .joinToString("\n")

"""
["abc"]
["abc"]
["abc"]
"""
grid, start, end = read_input()

# print(start)
# print(end)

# print(grid)

# print(grid[start[1]][start[0]])
# print(grid[end[1]][end[0]])
path_grid = [[(".", 0) for _ in grid[0]] for _ in grid]
path = find_path(start, end)
print(path)

paths_from_a = []
for y in range(len(grid)):
    for x in range(len(grid[y])):
        location = (x, y)
        if height(location) == "a":
            path_grid = [[(".", 0) for _ in grid[0]] for _ in grid]
            paths_from_a.append(find_path(location, end))

print(sorted(paths_from_a)[0])
