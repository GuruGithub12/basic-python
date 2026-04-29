def func_reversal(my_str):
    for i in range(len(my_str) - 1, -1, -1):
        print(my_str[i], end=', ')

func_reversal("Hello, World!")

#lice method
def func_reversal1(my_str):
    revstr = my_str[::-1]
    print("Reverse string:", revstr)
func_reversal1("Hello Mate!")