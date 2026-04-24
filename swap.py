a=3
b=4
print("Before swapping: a =", a, "b =", b)
a,b =b,a
print("After swapping: a =", a, "b =", b)



my_list = list(range(1, 21))
print("Original list:", my_list)
my_NewList = [my_list[i+1] for i in range(0, len(my_list), 2)]
print("\nNew list with odd numbers:", my_NewList)
