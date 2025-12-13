import itertools
def word_occur_count(s):
   dict1={}
   words=s.split()
   print(words)
   for word in words:
      if word in dict1:
        dict1[word]+=1
      else:
        dict1[word]=1
   print(dict1)
     
def intersection_pair (x,y):
  intersec_pair=[]
  for j in range(0,len(y)):
    for i in range(len(x)):
      if x[i]==y[j]:
        intersec_pair=x[i]
    print(intersec_pair)
      
def balance_parenthesis(s):
  stack=[]
  open_brackett='({['
  for char in s:
    if char in open_brackett:
      stack.append(char)
      print(stack)
    elif not stack:
      print("Stack is empty")
    else:
      stack.pop()
      print(stack)

  if stack:
    print("Incorrect Expression:::")
  else:
    print("Correct Expression")


s="I am lerning python and python is powerful"
word_occur_count(s)
x=[1,2,3,4,5,6,7,8]
y=[1,3,4,2,5]
intersection_pair(x,y)
brackett_expression="{[()]}"
balance_parenthesis(brackett_expression)