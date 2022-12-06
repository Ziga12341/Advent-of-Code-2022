# first start-of-packet marker ... n = 4
# second start-of-message marker ... n = 14
def start_of_message(n):
    with open("input.txt", "r", encoding="utf-8") as file:
        datastream_buffer = [character for character in file]
        for i in range(len(datastream_buffer[0])):
            four_in_a_row = datastream_buffer[0][i:n+i]
            if len(set(four_in_a_row)) == n:
                return i+n


# first part
print("Result for first part", start_of_message(4))
# second part
print("Result for second part", start_of_message(14))
