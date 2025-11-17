def reverse_str():
    reverse_word=[]
    word=input("enter a string to reverse  : ")
    for char in range(len(word)-1,-1,-1):
         reverse_word.append(word[char])
    print(f"reverse string is :: {reverse_word}")

"""    print(word[::-1]) # Using Slicer"""

def frequency_char():
    freq_dict={}
    word=input("Enter a string:::")
    for char in word:
        if char in freq_dict:
            freq_dict[char]=freq_dict[char] + 1
        else:
            freq_dict[char]=1
    print(freq_dict)

def remove_duplicate():
    no_list=[1,2,3,2,1,2,3,4]
    unique=[]
    for i in no_list:
        if i not in unique:
            unique.append(i)
    print(unique)

"""     USING INBULT METHOD
no_list=[1,2,3,4,3,2,1,2,3,34,1]
    no_list=list(set(no_list))
    print(no_list)
"""
def merge_dict():
    dict1={"apple":"red","Banana":"yellow"}
    dict2={"peas":"green","potato":"brown"}
    dict2.update(dict1)
    print(dict2)

def even_odd_count():
    even_list=[]
    odd_list=[]
    count1=0
    count2=0
    for i in range(10):
        no=int(input("Enter a whole number to check(Even/Odd):::"))
        if no % 2==0:
            even_list.append(no)
            count1+=1
        else:
            odd_list.append(no)
            count2+=1
    print(f"Even numbers are :: {even_list} total :: {count1}")
    print(f"Odd numbers are :: {odd_list} total :: {count2}")

def second_largest():
    no_list=[1,3,2,6,5,4,3,78,98,65,43,45,32,34,78]
    largest=no_list[0]
    i=1
    for i in no_list:
        if largest<i:
            largest=i
    i=1
    sec_largest=no_list[0]
    for i in no_list:
        if sec_largest<i<largest:
            sec_largest=i
    print(f"largest is :: {largest}\n second largest is :: {sec_largest}")

    
#reverse_str()
#frequency_char()
#remove_duplicate()
# merge_dict()
# even_odd_count()
second_largest()