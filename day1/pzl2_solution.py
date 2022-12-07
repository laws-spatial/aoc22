# import the list of sums from the first puzzle solution
from pzl1_solution import sum_list

# sort list in descending order
sum_list.sort(reverse=True)

# slice top 3
top_three = sum_list[0:3]

# sum those top 3
top_three_tot = sum(top_three)

print(f"The maximum calories for puzzle 2 are {top_three_tot}.")