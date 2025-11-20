import copy

a=[1,[2,3]]
b=copy.copy(a)

c=copy.deepcopy(a)

b[1][0]=100
b[0]=20

c[1][1]=500

print("a:",a)
print("b:",b)
print("c:",c)