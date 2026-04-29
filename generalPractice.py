for i in range(1, 11):
    print(i)


grocery=["milk", "bread", "eggs", "fruits", "vegetables"]
for i in grocery:
    print(i)
grocery.append("chocolate")
grocery.remove("bread")
for i in grocery:
    print(i)

print(len(grocery))

set1 = {1, 2, 3, 4, 5,3,2}
print(set1)
print(len(set1))
tuple1 = (1, 2, 3, 4, 5,3,2)
print(tuple1)
print(len(tuple1))

prices = [10, 20, 30, 40, 50]
total =0
for i in range(len(prices)):
    total = total + prices[i]
print("Total price:", total)
total =0
for i in prices:
    total = total + i
print("Total price:", total)



