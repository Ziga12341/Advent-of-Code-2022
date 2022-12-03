import string
with open("input.txt", "r", encoding="utf-8") as file:
    sum_items_in_groups = 0
    letters = string.ascii_letters

    all_rucksacks = []

    # group three rucksack together
    for i, items_per_rucksack in enumerate(file):
        items_per_rucksack = items_per_rucksack.split("\n")[0]
        all_rucksacks.append(set(items_per_rucksack))

    for i, every_rucksack in enumerate(all_rucksacks):
        if (i + 1) % 3 == 0:
            group_of_rucksack = (all_rucksacks[i - 2:i + 1])
            first = group_of_rucksack[0]
            second = group_of_rucksack[1]
            third = group_of_rucksack[2]

            same_item_in_all_three = first & second & third

            sum_items_in_groups += letters.index(list(same_item_in_all_three)[0]) + 1
    print(sum_items_in_groups)