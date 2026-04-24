list =range(1, 30, 1)  
for num in list:
        if num % 3 == 0 :
            print("FizzBuzz", end=', ')
        else:
            print(num, end=', ')
