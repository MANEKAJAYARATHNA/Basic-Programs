x=int(input("enter your number"))
i=1
fact=1
while(i<=x):
    fact=fact*i
    i=i+1
print(fact)


x=int(input("enter your number"))
i=1
fact=1
for i in range(1,x+1):
    fact=fact*i
print(fact)