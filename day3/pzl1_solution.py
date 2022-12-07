from pathlib import Path
import string

# set up url
file_str = ".\input.txt"
input = Path(file_str)

# create list of items
item_list = []

with open(input, "r") as f:
    full_text = f.readlines()
    
    for text in full_text:
        # get length of text
        text_len = len(text) - 1

        # find middle index
        mid_index = int(text_len/2)
    
        # split into compartments
        first_comp = text[:mid_index]
        sec_comp = text[mid_index:]

        # find common variable using set intersection method
        common = list(set(first_comp).intersection(sec_comp))[0]

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
# The set intersection method is super useful and will defintely come in
# handy. I had not worked with the string package and I wouldn't have 
# thought to look for it based on methods for the str dtype.