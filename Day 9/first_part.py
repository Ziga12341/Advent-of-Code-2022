with open("input.txt", "r", encoding="utf-8") as file:
# with open("test.txt", "r", encoding="utf-8") as file:
    visited_by_tail = [(0, 0)]
    visited_by_head = [(0, 0)]
    directions = {
        "L": (-1, 0),
        "R": (1, 0),
        "D": (0, -1),
        "U": (0, 1)
    }

    def next_step_head(previous_step, direction):
        x0, y0 = previous_step
        x1, y1 = directions[direction]
        return x0 + x1, y0 + y1

    # rules:
    # if current location of head is ...

    # if tail is in same location than head than you do not need to update (move tail)
    # if tail is now just one direction away from head, you do not need to move tail
    # if --> head goes tail is diagonally to head you do not need to upadate tail
    # if head is two directions away from tail: update tail location that it will be just one direction away
    # if head is knight (L) shape away from tail, than you need to update tail location as diagonale (up and right)

    def update_tail(current_head_location, tail_previous_location):
        x0, y0 = tail_previous_location
        x1, y1 = current_head_location

        # diference two between head and tail in particular line
        if x1 - x0 == 2 and y1 - y0 == 0:
            visited_by_tail.append((x0 + 1, y0))

        if x0 - x1 == 2 and y1 - y0 == 0:
            visited_by_tail.append((x0 - 1, y0))

        if x1 - x0 == 0 and y1 - y0 == 2:
            visited_by_tail.append((x0, y0 + 1))

        if x1 - x0 == 0 and y0 - y1 == 2:
            visited_by_tail.append((x0, y0 - 1))

        # difference knight jump
        # first part
        if x0 - x1 == -1 and y0 - y1 == -2:
            visited_by_tail.append((x0 + 1, y0 + 1))

        if x0 - x1 == +1 and y0 - y1 == -2:
            visited_by_tail.append((x0 - 1, y0 + 1))
        # second part
        if x0 - x1 == -2 and y0 - y1 == -1:
            visited_by_tail.append((x0 + 1, y0 + 1))

        if x0 - x1 == -2 and y0 - y1 == 1:
            visited_by_tail.append((x0 + 1, y0 - 1))
        # third part
        if x0 - x1 == -1 and y0 - y1 == 2:
            visited_by_tail.append((x0 + 1, y0 - 1))

        if x0 - x1 == +1 and y0 - y1 == 2:
            visited_by_tail.append((x0 - 1, y0 - 1))
        # forth part
        if x0 - x1 == 2 and y0 - y1 == -1:
            visited_by_tail.append((x0 - 1, y0 + 1))

        if x0 - x1 == 2 and y0 - y1 == 1:
            visited_by_tail.append((x0 - 1, y0 - 1))


    for line in file:
        line = line.split("\n")
        direction, steps = line[0].split(" ")
        steps = int(steps)
        for i in range(steps):
            head_previous_location = visited_by_head[-1]
            tail_previous_location = visited_by_tail[-1]
            current_head_location = next_step_head(head_previous_location, direction)
            visited_by_head.append(current_head_location)
            update_tail(current_head_location, tail_previous_location)

    print(visited_by_head)
    print(visited_by_tail)
    print(len(visited_by_tail))
    print(len(set(visited_by_tail)))


# teil leads head... but I need to specify how it will lead head...
# need to specify every location of tail...
# in a way that I will get previous location and current location of head nad know if tail moved and in which way moved

# test result is 13

