from collections import namedtuple

Person=namedtuple("Person",["name","age","address"]) # nametuple Person
P=Person(name="Vidushi",age="34",address="Delhi")
print(P)

Student=namedtuple("Student",["name","standard","marks"]) # nametuple student
s1=Student(name="Priya",standard="First",marks=90)
s2=Student(name="Rekha",standard="First",marks=80)
s3=Student(name="Pankaj",standard="Second",marks=94)
if s1.marks>s2.marks & s1.marks>s3.marks:
    print(f"{s1.marks} are greatest")
elif s2.marks>s2.marks & s2.marks>s3.marks:
    print(f"{s2.marks} are greatest")
else:
    print(f"{s3.marks} are greatest")