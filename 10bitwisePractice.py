a=True
b=True
if a and b: 
    print("Both a and b are true")
a=False
b=True
if a and b:     
    print("Both a and b are true")
else:
    print("Either a or b is false")
a=True
b=True
if a or b: 
    print("testing or : Either a or b is true") 
elif a and b:
    print("Both a and b are true")
else:
    print("Both a and b are false")