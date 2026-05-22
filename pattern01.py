n=input("enter your symbol")
x=int(input("enter how many terms"))
for i in range(1,x+1):
    y=n*i
    print((y)+(" ")*(x-i))


n=input("enter your symbol")
x=int(input("enter how many terms"))
i=1
while(i<=x):
    y=n*i
    print((y)+(" ")*(x-i))
    i=i+1