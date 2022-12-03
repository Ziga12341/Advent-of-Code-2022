import string
with open("input.txt", "r", encoding="utf-8") as file:
    sum_all_same_items_in_both_compartment = 0
    letters = string.ascii_letters
    # loop through all file
    for items_per_rucksack in file:
        items_per_rucksack = items_per_rucksack.split("\n")[0]
        #print(items_per_rucksack)
        half_item_in_component = (int(len(items_per_rucksack)/2))
        first_compartment = items_per_rucksack[:half_item_in_component]
        second_compartment = items_per_rucksack[half_item_in_component:]

        same_items_in_both_compartment = set(first_compartment) & set(second_compartment)
        #print(same_items_in_both_compartment)
        #print(list(same_items_in_both_compartment)[0])

        sum_all_same_items_in_both_compartment += letters.index(list(same_items_in_both_compartment)[0]) + 1

    print(sum_all_same_items_in_both_compartment)
