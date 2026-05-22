n=str(input("enter your number or word"))
count=len(n)
m=n[count-1]+n[count-2:0:-1]+n[0]
if(m==n):
    print("it is a palindrome")
else:
    print("it i not a palindrome")