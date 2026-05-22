n=str(input("enter your symbol"))
height=int(input("enter height"))
width=int(input("enter width"))
for i in range(1,height+1):
    y=str(n*width)
    print(((" ")*(height-i)+y))


n=str(input("enter your symbol"))
height=int(input("enter height"))
width=int(input("enter width"))
i=1
while(i<=height):
    y=str(n*width)
    print(((" ")*(height-i)+y))
    i=i+1