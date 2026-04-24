import random

list = list(range(1, 31, 1))
for num in list:
        print(num, end=', ')

my_list = [random.randint(1, 20) for _ in range(20
                                                )]
print("Original list:", my_list)

def palindrome(my_str):
        revstr =""
        # revstr = str[::-1]
        # if str == revstr:
        #         print("The string is a palindrome.")
        # else:
        #         print("The string is not a palindrome.")
        for i in range(len(my_str)):
                print(my_str[i], end=', ')

        for i in range(len(my_str) - 1, -1, -1):
                print(my_str[i], end=', ')
                revstr = revstr + my_str[i]

        print("Reverse string:", revstr)
        if my_str == revstr:
                print("The string is a palindrome.")
        else:
                print("The string is not a palindrome.")
palindrome("racecar")
palindrome("malayalam")

def unique_elements(lst):
        unique_lst = []
        for element in lst:
                if element not in unique_lst:
                        unique_lst.append(element)
        return unique_lst

list_with_duplicates = [1, 2, 3, 4, 5, 2, 3, 6]
dict_with_duplicates = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 2, 'g': 3, 'h': 6}
tuple_with_duplicates = (1, 2, 3, 4, 5, 2, 3, 6)
set_with_duplicates = {1, 2, 3, 4, 5, 2, 3, 6}
for data in [list_with_duplicates, dict_with_duplicates, tuple_with_duplicates, set_with_duplicates]:
        unique_data = unique_elements(data)
        print("Unique elements:", unique_data)
