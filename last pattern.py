n = input("enter your first symbol")
m = input("enter your second symbol")
height = int(input("enter height"))
x=1
for i in range(1, height + 1):
    if(i%2!=0):
        symbol=n
    else:
        symbol=m
    y=symbol*x
    print((" "*(height-i))+y)
    x=x+2




n = input("enter your first symbol")
m = input("enter your second symbol")
height = int(input("enter height"))
x=1
i=1
while(i<=height):
    if(i%2!=0):
        symbol=n
    else:
        symbol=m
    y=symbol*x
    print((" "*(height-i))+y)
    x=x+2
    i=i+1