from pathlib import Path
import string

# set up url
file_str = ".\input.txt"
input = Path(file_str)

# create list of items
item_list = []

with open(input, "r") as f:
    full_text = f.readlines()

    # create lists of 3 lines
    n = 3

    grouped_text = [full_text[k:k+n] for k in range(0, len(full_text), n)]

    for group in grouped_text:

        # strip newline characters
        new_group = []
        for text in group:
            new_group.append(text.strip())

        # find common variable using set intersection method
        common = list(set(new_group[0]).intersection(new_group[1],new_group[2]))[0]

        # append to item_list
        item_list.append(common)

# build dictionary of weigths
values = dict()

# start with lowercase
for index, letter in enumerate(string.ascii_lowercase):
   values[letter] = index + 1

# finish wtih uppercase
for index, letter in enumerate(string.ascii_uppercase):
   values[letter] = index + 27 # use 27 due to 0 indexing

# assign values
priority = [values[x] for x in item_list]

# sum priority
priority_sum = sum(priority) 

print(f"The sum of all priorities is {priority_sum}.")

# What I learned:
# The grouping of the list elements (list of lists) was a new way
# of using list comprehension