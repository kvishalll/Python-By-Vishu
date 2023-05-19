# 1. Write a Python program to replace last value of tuples in a list


tuples_list = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
new_value = 10

for i in range(len(tuples_list)):
    tuples_list[i] = tuples_list[i][:-1] + (new_value,)

print(tuples_list)
