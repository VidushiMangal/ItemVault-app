from functools import reduce

def list_comprehension(n):
    square=[i*i for i in range(1,n )]
    print(square)

    words=["pritam","priyal","roshni","vikas"]
    word=[word.title()for word in words]
    print(word)

    word=[word for word in words if word.startswith("p")]
    print(word)

def lambda_function():
    addition=lambda n: n+10
    print(addition(5))

    s="Antra"
    startwithA=lambda s: s.startswith("A")
    print(startwithA(s))

def map_function():
    nums=[1,2,3,4,5]
    result=list(map(lambda num:num*2 ,nums))
    print(result)

    words=["pritam","priyal","roshni","vikas"]
    title_word=list(map(lambda word: word.title(),words))
    print(title_word)

    words=["pritam","priyal","roshni","vikas"]
    upper_str=list(map(lambda word:word.upper(),words))
    print(upper_str)

def filter_function():
    nums=[1,2,3,4,5,6,7,8,9,10]
    even_list=list(filter(lambda x:x%2==0,nums))
    print(even_list)

def reduce_function():
    nums=[1,2,3,4,5,6,7,8,9]
    sum=reduce(lambda x,y:x+y,nums)
    print(sum)



#list_comprehension(5)
#lambda_function()
map_function()
filter_function()
reduce_function()