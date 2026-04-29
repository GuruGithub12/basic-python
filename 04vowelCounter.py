def count_vowels(s):
    vowels = 'aeiouAEIOU'
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count
input_string = input("Enter a string: ")
vowel_count = count_vowels(input_string)
print("Number of vowels in the string:", vowel_count)


dict1 = {'NSW': 'Sydney', 'Victoria': 'Melbourne', 'Queensland': 'Brisbane', 'Western Australia': 'Perth', 'South Australia': 'Adelaide', 'Tasmania': 'Hobart', 'Australian Capital Territory': 'Canberra'}
for state, capital in dict1.items():
    print(f"The capital of {state} is {capital}.")  
    input_string = input("Enter a state name to find its capital: ")
capital = dict1.get(input_string)
if capital:
    print(f"The capital of {input_string} is {capital}.")
else:    print("State not found in the dictionary.")
    