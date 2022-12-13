with open("calories.txt", "r", encoding="utf-8") as file:

    sum_calories = []
    all_summed_elf_calories = []
    count_calories = 0

    # loop through all file
    for elf_carried_calories in file:

        # in not blank line convert string to init and remove "\n" from eno of the line
        if elf_carried_calories != "\n":
            elf_carried_calories = int(elf_carried_calories[:-1])

        # when blank line, append to list summed value of all calories in one block
        if elf_carried_calories == "\n":
            all_summed_elf_calories.append(count_calories)
            count_calories = 0
        # if not blank line sum carried calories from each elf
        else:
            count_calories += elf_carried_calories

    print("all_summed_elf_calories", all_summed_elf_calories)
    best_elf_carries = (sorted(all_summed_elf_calories)[-1])
    sum_best_three = (sum(sorted(all_summed_elf_calories)[:-4:-1]))
    print("best_elf_carries", best_elf_carries)
    print("sum_best_three", sum_best_three)

