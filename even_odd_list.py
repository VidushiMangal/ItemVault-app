evenno=[]
oddno=[]
sum=0
for i in range(10):
    x=int(input("Enter a whole number"))
    sum = sum + x
    if x%2==0:
        evenno.append(x)
    else:
        oddno.append(x)
print(f"Even no are :  {evenno}")
print(f"Odd no are :  {oddno}")
print(f"sum = {sum}")