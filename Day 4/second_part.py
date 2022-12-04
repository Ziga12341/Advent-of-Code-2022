with open("input.txt", "r", encoding="utf-8") as file:

    count_cleaning_sections_ment_for_both_cleaners = 0

    # loop through file
    for line in file:

        first_cleaner_whole_section = set()
        second_cleaner_whole_section = set()

        first_cleaner = line.split(",")[0]
        second_cleaner = line.split(",")[1]

        first_cleaner_start = int(first_cleaner.split("-")[0])
        first_cleaner_end = int(first_cleaner.split("-")[1])

        second_cleaner_start = int(second_cleaner.split("-")[0])
        second_cleaner_end = int(second_cleaner.split("-")[1])

        # add all sections for first cleaner in set
        for first_cleaner_sections in range(first_cleaner_start, first_cleaner_end + 1):
            first_cleaner_whole_section.add(first_cleaner_sections)

        # add all sections for second cleaner in set
        for second_cleaner_sections in range(second_cleaner_start, second_cleaner_end + 1):
            second_cleaner_whole_section.add(second_cleaner_sections)

        # if sets has one common number than add one to counter
        if first_cleaner_whole_section & second_cleaner_whole_section:
            count_cleaning_sections_ment_for_both_cleaners += 1


    print(count_cleaning_sections_ment_for_both_cleaners)
