x=int(input("enter your value one"))
y=int(input("enter your value two"))
z=int(input("enter your value three"))
if(x>y):
    if(x>z):
        if(y>z):
            max=x
            min=z
        else:
            max=x
            min=y
    else:
        max=z
        min=y
elif(y>z):
    if(x>z):
        max=y
        min=z
    else:
        max=y
        min=x
else:
    max=z
    min=x
print(max)
print(min)