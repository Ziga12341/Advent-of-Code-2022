import os

for day in range(1, 26):
    new_path = f"{os.getcwd()}\\Day {day}"
    if not os.path.exists(new_path):
        os.makedirs(new_path)
    # print(newpath)