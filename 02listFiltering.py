




my_List = [1,3,4,2,5,3,6,2,7,8,4,9,10]
even= list(filter(lambda x: x % 2 == 0, my_List))
print(even)

for element in my_List:
   if element %2 == 0:
      print("even number:" ,element)
   else:
        print("odd number:" ,element)
      
      
      