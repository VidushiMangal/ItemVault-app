def target_sum():
    pair_dict={}
    target=int(input("Enter number for target :::"))
    no_list=[1,4,3,2,5,6,7,8,6,5,4,3,2,8,6,5,0]
    for i in range(0,len(no_list)):
        for j in range(i+1,len(no_list)):
            if no_list[i] + no_list[j] ==target:
                pair_dict[no_list[i]]=no_list[j]
    print(pair_dict)

def is_pallindrome():
    word=input("Enter a word to check for pallindrome:::")
    flag=1
    half_len=len(word)
    for i in range(half_len):
        if word[i]!=word[0-(i+1)]:
            flag=0
            break
    if flag==1:
        print(f"Word {word} is pallindrome")
    else:
        print(f"Word {word} is not pallindrome")

def is_anargam():
    s=input("Enter a first strings :::")   
    s1=input("Enter a second strings to check for anargam:::")   
    dict1={}
    dict2={}
    for char in s:
        if char in dict1:
            dict1[char]+=1
        else:
            dict1[char]=1
    for char in s1:
        if char in dict2:
            dict2[char]+=1
        else:
            dict2[char]=1
    if dict1==dict2:
        print("Anargam")
    else:
        print("Not Anargam")

target_sum()
is_pallindrome()
is_anargam()
