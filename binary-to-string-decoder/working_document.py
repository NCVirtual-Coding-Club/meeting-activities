import os, sys

message_file = open("message.txt", "r")
message_list = message_file.readline().split(" ")

new_message = ""

# Gets conversion table
binary_char_table_file = open("ascii_table_binary_letter.txt", "r")
binary_char_list = binary_char_table_file.readlines()

print(binary_char_list)

binary_char_dict = {}