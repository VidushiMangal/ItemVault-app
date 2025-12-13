def move_zero_to_end():
    nums=[1,2,0,0,9,0,2,0,4,0,1]
    j=0
    for i in range(0,len(nums)):
        if nums[i]!=0:
            nums[j]=nums[i]
            j+=1
    print(nums)
    while j<len(nums):
        nums[j]=0
        j+=1
    print(nums)

def vowel_count(s):
    count=0
    for char in s:
        if char in 'aeiou':
            count+=1
    print(f"Total vowels in string ---{s}--- are {count}")

def merge_list(list1,list2):
    length=len(list1)-1
    for i in list2:
        list1.append(i)
    print(list1)

move_zero_to_end()
vowel_count("this is a computer lab")
list1=[1,2,3,4,5]
list2=[6,7,8,9,10]
merge_list(list1,list2)