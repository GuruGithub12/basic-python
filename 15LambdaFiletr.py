
my_List =["Guru","prasad","Goddumuri","Lazy","ADHD","impatient","horrible","unbearable"]
my_List1 = []
for i in range(len(my_List)):
    if len(my_List[i])>5:
        print(len(my_List[i]))
        my_List1.append(my_List[i])
    
print("\nNew list with words longer than 5 characters:", my_List1)

my_List2 = [word for word in my_List if word not in my_List1]
print("\nNew list with words shorter than 5 characters:", my_List2)
