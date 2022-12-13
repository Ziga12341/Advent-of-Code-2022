from collections import defaultdict
import re

second_stacks_of_crates = defaultdict(list)
stacks_of_crates = defaultdict(list)

# get info where separate file from stacks_of_crates and instructions
with open("input.txt", "r", encoding="utf-8") as file:
    for number_of_line, line in enumerate(file):
        if line == "\n":
            splitting_point = number_of_line - 1

# convert initial info of stacks_of_crates to dictionary
# keys are columns (stacks) values are list with all crates in list
text_to_columns = []
with open("input.txt", "r", encoding="utf-8") as file:
    for number_of_line, line in enumerate(file):
        if number_of_line < splitting_point:
            stark = str(number_of_line + 1)
            for leter_in_row in range(9):
                # get only letters (remove "[]")
                letter_location = leter_in_row * 4
                text_to_columns.append(line[1 + letter_location:2 + letter_location])

    # reorder all crates
    for i in range(9):
        stacks_of_crates[str(i + 1)] = (text_to_columns[i::9][::-1])
    # remove all empty crates
    for stacks, crates in stacks_of_crates.items():
        second_stacks_of_crates[stacks] = [crate for crate in crates if crate != " " and crate != ""]

# second part of file
with open("input.txt", "r", encoding="utf-8") as file:
    for number_of_line, line in enumerate(file):
        if number_of_line > splitting_point + 1:
            parsed_numbers = re.findall(r'\d+', line)
            how_many_iterations = int(parsed_numbers[0])
            from_where = parsed_numbers[1]
            to = parsed_numbers[2]

            # remove last {how_many_iterations} to list and remove it from list that comes from
            second_stacks_of_crates[to].extend(second_stacks_of_crates[from_where][-how_many_iterations:])
            second_stacks_of_crates[from_where] = second_stacks_of_crates[from_where][:-how_many_iterations]

print(second_stacks_of_crates)

for block, list_od_crates in second_stacks_of_crates.items():
    print(block, list_od_crates[-1])