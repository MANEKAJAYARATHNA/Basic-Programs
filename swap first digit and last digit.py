n=str(input("enter your number"))
count=len(n)
m=n[count-1]+n[1:count-1]+n[0]
print(m)