from unittest import result


my_List =[1,3,4,2,5,3,6,2,7,8,4,9,10]
result = list(filter(lambda x: x % 2 == 0, my_List))
print(result)

def  func_evenodd():
    my_List =[1,3,4,2,5,3,6,2,7,8,4,9,10]
    even_list = list(filter(lambda x: x % 2 == 0, my_List))
    odd_list = list(filter(lambda x: x % 2 != 0, my_List))
    print("Even numbers:", even_list)
    print("Odd numbers:", odd_list)
func_evenodd()


# my_List =[1,3,4,2,5,3,6,2,7,8,4,9,10]

# for i in my_List:
#     if i % 2 == 0:
#         print("Even numbers:", i)
#     else:
#         print("Odd numbers:", i)
    
my_List =[1,3,4,2,5,3,6,2,7,8,4,9,10]

list(map(lambda x: print("Even numbers:", x) if x % 2 == 0 
         else print("Odd numbers:", x), my_List))
