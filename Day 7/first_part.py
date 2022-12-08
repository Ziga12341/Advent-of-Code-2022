import re
with open("input.txt", "r", encoding="utf-8") as file:
    main = []
    root_folder = "$ cd /"
    changed_file = [line[:-1] for line in file if line != "$ ls\n" and line != "$ cd ..\n" and line != "$ cd /\n"]
    first_folder = []
    for line_in_changed_file in changed_file:
        if line_in_changed_file[0].isdigit():
            line_in_changed_file = line_in_changed_file.split(" ")[0]
        first_folder.append(line_in_changed_file)
        if not line_in_changed_file == root_folder and line_in_changed_file.startswith("$ cd "):
            structured_folder = (first_folder[0][5:], first_folder[1:-1])
            changed_file = changed_file[len(structured_folder[1]) + 1:]
            print(changed_file)
            main.append((root_folder[5:], first_folder[:-1]))
            print((root_folder[5:], first_folder[:-1]))
            root_folder = first_folder[-1]
            first_folder = []

    print("main is:", main)

    # for one in main:
    #     print(one[0])

# prestavi main v drevesni slovar... - nimam pojma kako...
