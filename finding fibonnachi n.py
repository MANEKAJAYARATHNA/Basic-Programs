x=int(input("enter your number"))
pre=0
next=1
i=3
while(i<=x):
    fib=pre+next
    pre=next
    next=fib
    i=i+1
print(fib)


x=int(input("enter your number"))
pre=0
next=1
for i in range(1,x-1):
    fib=pre+next
    pre=next
    next=fib
print(fib)
