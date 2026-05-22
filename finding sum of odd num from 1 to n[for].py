n=int(input("enter your number"))
sum=0
for i in range(n+1):
    if(i%2!=0):
        sum=sum+i
print(sum)


n=int(input("enter your number"))
sum=0
i=1
while(i<=n):
    if(i%2!=0):
        sum=sum+i
        i=i+2
print(sum)