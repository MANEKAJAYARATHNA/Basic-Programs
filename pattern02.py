n=input("enter your symbol")
x=int(input("enter how many terms"))
for i in range(x+1,0,-1):
    y=n*i
    print((y)+(" ")*(i-x))


n=input("enter your symbol")
x=int(input("enter how many terms"))
i=x
while(i>=1):
    y=n*i
    print((y)+(" ")*(i-x))
    i=i-1