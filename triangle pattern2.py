n=str(input("enter your symbol"))
height=int(input("enter height"))
x=1
for i in range(1,height+1):
    y=str((n*x))
    x=x+2
    print(((" ")*(height-i)+y))


n=str(input("enter your symbol"))
height=int(input("enter height"))
x=1
i=1
while(i<=height):
    y=str((n*x))
    x=x+2
    print(((" ")*(height-i)+y))
    i=i+1