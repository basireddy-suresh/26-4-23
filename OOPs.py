class Book:
    Numberofpages=120
    name="suresh"
    prize=210
    def __init__(self,zone,dob):  # instance attributes
        self.zone=zone
        self.dob=dob
    def __del__(self):
        print("destructor called")
my_book=Book("history","26-12-2001")  # Constructor
print(my_book.name)
print(my_book.zone)
print(my_book.dob)
del my_book

#inheritance
class school:
    name="suri"
    age=21
    def __init__(self,age):
         self.age=age
    def getAge(self):
        return self.age
class Subschool(school):
    #def __init__(self,name):
     #   print("ada")
    def getParentName(self):
        return "sai"
    def getName(self):
        return "tarak"
my_school=Subschool(13)
print(my_school.getAge())
print(my_school.getParentName())
print(my_school.getName())

# 13 sai tarak


class Parent1:
    def getName(self):
        return "parent1"
class Parent2:
    def defName(self):
        return "parent2"
class Parent3:
    def getName(self):
        return "parent3"
class child(Parent1,Parent2,Parent3):
    def getAllParent(self):
        return "AllParent"
multi_level=child()
print(multi_level.getAllParent())
print(multi_level.getName())
print(multi_level.defName())
print(multi_level.getName())

"""AllParent
parent1
parent2
parent1"""

#multilevel inheritance
class Parent1:
    def getName(self):
        return "parent1"
class Parent2:
    def defName(self):
        return "parent2"
class Parent3:
    def getName(self):
        return "parent3"
class child(Parent1,Parent2,Parent3):
    def __init__(self):
        self.getAllParent()
    def getAllParent(self):
        return "AllParent"
my=child()
print(my.getAllParent())
print(my.getName())
print(my.defName())
print(my.getName())
print(my.__class__)
parent_list=[]
for base in child.__bases__:
    parent_list.append(base)
    print(base,end="")
"""AllParent
parent1
parent2
parent1
<class '__main__.child'>
<class '__main__.Parent1'><class '__main__.Parent2'><class '__main__.Parent3'>"""

#polymorphism
#polymorphism
def addnum(a,b,c=2):
    print(a+b+c)
addnum(10,20)
def addnum2(*args):
    sum=0
    for i in args:
        sum+=i
    print(sum)
addnum2(10,20)
addnum2(10,20,30)
def addnum3(ar1,ar2,*ar3):
    print(ar1,ar2,ar3)
addnum3(1,2)
addnum3(1,2,3)
addnum3(1,2,3,4)

"""32
30
60
1 2 ()
1 2 (3,)
1 2 (3, 4)"""

def job(a1,a2,a3):
    return "suresh"

def job(a1):
    return "sai"
print(job(1))
print(job("sk"))

#output
"""sai
sai"""

def job(a1):
    return "saidsefd"
def job(a1,a2,a3):
    return "sadkasfj"
job(10,2,3)
job(1)

#output
"""def job(a1):
    return "saidsefd"
def job(a1,a2,a3):
    return "sadkasfj"
job(10,2,3)
job(1)"""

#Encapsulation
class lib:
    def getbooks(self):
        pass
    def getauthorname(self):
        pass
    def getbooknames(self):
        pass
class Mylib(lib):
    def getfavoutire(self):
        pass
    def getfavbooks(self):
        pass
ok=Mylib()
print(ok.getbooknames())

#output
"""None"""
