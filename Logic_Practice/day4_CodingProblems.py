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
     

s="I am lerning python and python is powerful"
word_occur_count(s)