import os, sys

message_file = open("message.txt", "r")
message_list = message_file.readline().split(" ")

new_message = ""

# Gets conversion table
binary_char_table_file = open("ascii_table_binary_letter.txt", "r")
binary_char_list = binary_char_table_file.readlines()
binary_char_dict = {}


# Converts binary to character
def get_letter_from_binary(binary):
    if str(binary) == "00100000":
        return " "
    else:
        try:
            return binary_char_dict[str(binary)]
        except KeyError:
            return "[?]"

# Converts ASCII Table to Dict.
for row in binary_char_list:
    row_list = row.strip().split("\t")
    row_list[1] = row_list[1].strip()

    binary_char_dict["0" + str(row_list[0])] = row_list[1]
    print(binary_char_dict)

# Converts each binary group to a character
for binary_group in message_list:
    new_message += get_letter_from_binary(binary_group)

print(new_message)