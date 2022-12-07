from pathlib import Path
from queue import LifoQueue
from helpers import move_cargo
import pyperclip

# create file path
file_path = Path(".\input.txt")

with open(file_path, "r") as f:
    text = f.readlines()

    # figure out where column numbers start
    for index, value in enumerate(text):
        try:
            if value.strip()[0] == "1":
                col_numbers_index = index
            else:
                pass
        except IndexError as e:
            pass
    
    # subset cargo hold
    cargo_hold = text[0: col_numbers_index]

    # how many columns of crates?
    cols_of_crates = len(text[col_numbers_index].strip().split())

    # how high is the highest stack, initially?
    initial_stack_height = range(0, col_numbers_index)

    # Column numbers start at 1, not zero, so 1 will need to be subtract
    # from the column numbers. Crate letters are every 4 indices, starting 
    # at 1, and since we will be using the range function (exclusive 
    # maximumn), add another 1 for max index for a total addition of two
    max_index = (cols_of_crates-1) * 4 + 2

    # create range of indices to extract crate values:
    stack_cols = range(1, max_index, 4)

    #create list of last-in, first-out (LIFO) queues as stacks
    cargo_stacks = []
    for r in range(1, cols_of_crates+1):
        _ = LifoQueue()
        cargo_stacks.append(_)


    # fill in stacks from file, starting at bottom of stacks
    for row in reversed(initial_stack_height):

        # single row of crates
        row_of_crates = cargo_hold[row]

        for row_index, row_value in enumerate(row_of_crates):

            # check if value is a crate (letter)
            if row_value.isalpha():

                # which cargo stack to put crate in?
                # match index of value to value in stack
                # coumns and return its index
                cargo_col = stack_cols.index(row_index)
                
                # put crate in stack by subseting list
                # queues 
                cargo_stacks[cargo_col].put(row_value)

    # subset list of changes to cargo stacks
    # by finding first occurence of "move"
    for index, value in enumerate(text):
        try:
            if value.strip()[0:4] == str.lower("move"):
                moves_start_index = index
                # break once the first incidence is found
                break
            else:
                pass
        except IndexError as e:
            pass
    
    # and then subsetting full text file
    changes_to_cargo = text[moves_start_index:]
        
    # perform movement of cargo as per instructions
    _ = move_cargo(changes_to_cargo, cargo_stacks)

    # create list of top crate from each stack
    top_crate_list = []

    for index, stack in enumerate(cargo_stacks):
        top_crate = stack.get()
        top_crate_list.append(top_crate)

    # combine into a string
    top_crate_str = ''.join(top_crate_list)
    print(f"The top crates are: {top_crate_str}.")

    # copy string to clipboard
    pyperclip.copy(top_crate_str)