my_List = [1, 2, 3, 4, 5]
def sum_of_list(lst):
    total = 0
    for num in lst:
        total += num
    return total

print(sum_of_list(my_List))