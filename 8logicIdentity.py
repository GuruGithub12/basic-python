

# == checks value equality

# is checks memory identity

a= 4
b= 5
c="guru"
d="lucky"
a=b
if  a==b:
    print("A value:", a)
else :
    print("B value:", b)
c=d
if c is d:
    print("guru is lucky", c)