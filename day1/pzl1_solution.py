from pathlib import Path
import tkinter as tk
from tkinter import filedialog

# # create Path object for file
# calories_file = ".\calories.txt"
# calories_path = Path(calories_file)

root = tk.Tk()
root.withdraw()

calories_path = filedialog.askopenfilename()

with open(calories_path, "r") as f:
    # read in files contents
    text = f.readlines()

    # join all lines into single string then split where
    # two newline characters exist
    split_text = "".join(text).split("\n\n")

    # create list of sums
    sum_list = []

    for text in split_text:
        # split single string into multiple at newline
        nums_as_strs_list = list(text.split("\n"))

        # if empty string exists, remove it from list
        if "" in nums_as_strs_list:
            nums_as_strs_list.remove("")

        # convert strings to ints    
        int_list = [eval(i) for i in nums_as_strs_list]

        # sum integers
        sum_of_ints = sum(int_list)

        # append to list of sums
        sum_list.append(sum_of_ints)

    # finx maximum calories
    max_calories = max(sum_list)
    print(f"The maximum calories for puzzle 1 are {max_calories}.")

# What did I learn:
# Using the join method to combine all of the text together
# and then create a new list by breaking where there was a 
# space represented by two newline characters. I had also 
# not come across the eval method before, which parses a
# string expression into a number. Finally, I became 
# interested in adding the ability to select a file so 
# look into simple solutions and came across the 
# filedialog method from tkinter.