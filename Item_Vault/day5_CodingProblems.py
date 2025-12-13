def pallidrome(s):
    flag=0
    l=int(len(s)-1)
    for i in range(0,int(l/2)):
        if s[i]!=s[l]:
            flag=1
            break
        else:
            l-=1
    if flag ==1:
        print("String is not pallindrome")
    else:
        print("String is Pallindrome")

def most_occur(nums):
    most_number = None
    most_count = 0
    i = 0
    while i < len(nums):
        current = nums[i]
        count = 0
        j = 0
        while j < len(nums):
            if nums[j] == current:
                count += 1
            j += 1
        if count > most_count:
            most_count = count
            most_number = current
        i += 1
    print("Top occurring number:", most_number)
    print("It occurred:", most_count, "times")
     
def first_non_repeat(s):
    dict1={}
    for char in s:
        if char in dict1:
            dict1[char]+=1
        else:
            dict1[char]=1
    print(dict1)
    for k,v in dict1.items():
        if v==1:
            print(f"first non repeating character is : {k}")
            break
        

s=input("Enter a string check pallindrome:::")
pallidrome(s)

arr=[]
for i in range(0,4):
    arr.append(int(input(f"Enter {i+1} number")))
most_occur(arr)

first_non_repeat(s)