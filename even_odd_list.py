even_list=[]
odd_list=[]
for i in range(10):
    no=int(input("Enter a whole number to check(Even/Odd):::"))
    if no % 2==0:
        even_list.append(no)
    else:
        odd_list.append(no)
print(f"Even numbers are :: {even_list}")
print(f"Odd numbers are :: {odd_list}")
