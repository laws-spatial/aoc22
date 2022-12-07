# change conditional statements to if right[0] <= left[0] <=right[-1] or vice versa
from pathlib import Path

# import file
file_str = "input.txt"
file_path = Path(file_str)


with open(file_path, "r") as f:
    # create text object and strip nrewline characters
    text = [t.strip("\n") for t in f.readlines()]

    # seperate values by chaining list comprehension
    # internal list splits values at commma while the 
    # outer then joins them again with a hyphen then
    # splits them al at the hyphens
    split_text = ["-".join(y).split("-") for y in [list(x.split(",")) for x in text]]

    # create ranges of values per each partner
    range_text_first = [range(int(x[0]), int(x[1]) + 1) for x in split_text]
    range_text_second = [range(int(x[2]), int(x[3]) + 1) for x in split_text]

    # index and count
    i = 0
    count = 0

    while i < len(range_text_first):
        
        # get range values for each partner
        left = range_text_first[i]
        right = range_text_second[i]

        # if the lengths are the same then there is overlap if the value at
        # index 0 is the same
        if (right[0] <= left[0] <= right[-1]):
                count += 1
        # if left is longer than right, check to make sure its first and 
        # final values are smaller/equal to or larger/equal too, respectively
        elif (right[0] <= left[-1] <= right[-1]):
                    count += 1
        elif (left[0] <= right[0] <= left[-1]):
                    count += 1
        # same logic as left but for right
        else :
            if (left[0] <= right[-1] <= left[-1]):
                    count += 1
        i += 1

    print(f"{count} assignment ranges overlap with their counterpart assignment.")