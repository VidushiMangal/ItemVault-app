from collections import Counter, defaultdict
def Sort_dict_value(fruits):
    results=sorted(fruits.items(),key=lambda x:x[1]) # sorting by values
    return results

    results=sorted(fruits.items(),key=lambda x:x[0]) # sorting by Keys
    return results
    
# Checking whether two list have same elements
def same_number_check():
    num1=[]
    num2=[]
    n1=int(input("How many numbers you want to enter in first list:"))
    for i in range(0,n1):
        x=int(input(f"Enter {i+1} number :"))
        num1.append(x)
    n2=int(input("How many numbers you want to enter in second list:"))
    for j in range(0,n2):
        x=int(input(f"Enter {j+1} number :"))
        num2.append(x)
    if Counter(num1) == Counter(num2):
        return True
    else:
        return False

def group_anagrams(words):
    groups = defaultdict(list)

    for word in words:
        key = ''.join(sorted(word))   # sort the leters and join back to form word
        groups[key].append(word)      # add to correct group
    return list(groups.values())


def longest_common_prefix(strs):
    if not strs:
        return ""
    prefix = strs[0]   # start with first word
    for s in strs[1:]:              # compare with next words
        while not s.startswith(prefix):
            prefix = prefix[:-1]    # shrink prefix
            if prefix == "":        # no prefix left
                return ""
    return prefix


def rotate_right(num_list,positions):
    #positions=positions % num_list
    num_list=num_list[ -positions : ] + num_list[: -positions]
    print(num_list)

def rotate_left(num_list,positions):
    num_list=num_list[positions : ] + num_list[ : positions]
    print(num_list)

fruits={"banana":"1","apple":"3","cherry":"2","grapes":"4"}
print(Sort_dict_value(fruits))

strs=["flower","flow","flight"]
print(longest_common_prefix(strs))

result=same_number_check()
print(result)

words=["eat","tea","tan","ate","nat","bat"]
print(group_anagrams(words))

nums=[1,2,3,4,5,6,7]
pos=int(input("Enter positon to shift right"))
rotate_right(nums, pos)
pos=int(input("Enter positon to shift left"))
rotate_left(nums, pos) 