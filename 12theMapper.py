from functools import reduce


my_List = [1,2,3,4,5,6]
result= list(map(lambda x:x*x,my_List))
print(result)


my_StringList = ["hello", "world", "python"]
result = list(filter(lambda x: len(x) > 5, my_StringList))
print(result)

my_oddNum_List =[1,3,5,6,7,9]
result = reduce(lambda x,y:x+y,my_oddNum_List)
print(result)


from functools import reduce

nums = {1, 2, 3, 4}

print(set(map(lambda x: x*x, nums)))         # {16, 1, 4, 9}
print(set(filter(lambda x: x % 2 == 0, nums)))   # {2, 4}
print(reduce(lambda a, b: a + b, nums))      # 10


from functools import reduce

nums = (1, 2, 3, 4)

print(tuple(map(lambda x: x*x, nums)))       # (1, 4, 9, 16)
print(tuple(filter(lambda x: x % 2 == 0, nums)))  # (2, 4)
print(reduce(lambda a, b: a + b, nums))      # 10


from functools import reduce

nums = [1, 2, 3, 4]

# map → transform
print(list(map(lambda x: x*x, nums)))        # [1, 4, 9, 16]

# filter → keep
print(list(filter(lambda x: x % 2 == 0, nums)))  # [2, 4]
# reduce → combine
print(reduce(lambda a, b: a + b, nums))      # 10


# map
# Applies the logic to every element  
# → transforms each item
# → output has the same number of elements

# Example idea: square every number.

# filter
# Applies the logic as a test  
# → keeps only elements where the logic returns True  
# → output has fewer or equal elements

# Example idea: keep only even numbers.

# reduce
# Applies the logic repeatedly, carrying forward the running result  
# → collapses many values into one final value  
# → output is one element only

# Example idea: sum, multiply, max, min, flatten, build, accumulate.
