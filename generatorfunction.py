def genfunc(my_list):
    for i in range(len(my_list)):
        yield my_list[i]

my_list = [1, 2, 3, 4, 5]
generator = genfunc(my_list)
print(next(generator))
print(next(generator))
print(next(generator))

my_List = [1, 2, 3, 4, 5]
my_List.remove(3)
print(my_List)

my_List1 =  ["Hi"]
print(my_List1)
my_List1.append("Hello")
print(my_List1)

text = "Hi"
result = list(text)

print("Original string:", text)
print("After converting to list:", result)