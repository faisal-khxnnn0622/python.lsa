#first program
print("hello world")
print("im faisal khan")
print("im learning python from scratch")

#The things written after hashtag will not come in the output
#for example
#print("hello world")

#Varibles 
name = "faisal" #string or str
age = 17 #integer or int
marks = 12.4 #float
is_student = "true" #boolean
print(name)
print(age)
print(marks)
print(is_student)

#data types
print(type(name))
print(type(age))
print(type(marks))
print(type(is_student))

#Printing sum valus

a = 15
b = 25
c = (a+b)
print(c)

#one more example;

a = 12
b = 12
c = 12
d = 12
sum = (a+b+c+d)
print(sum)


#ARITHMETIC OPERATORS

#Arithmatic operators
# + addition
# - subtraction
# * multiplication
# / divisionn
# // floor division#
# % reminder
# ** power

a = 12
b = 12

print(a+b)
print(a-b)
print(a*b)
print(a/b) #Will be always float value
print(a//b)
print(a%b)
print(a**b)


# COMPARATIVE OPERATORS (answer in boolean values)

# == Equal to 
# != not equal to
# > greater then
# < smaller then
# >= greater or equal
# <= lower or equal to


x = 45
y = 60

print(x==y)
print(x!=y)
print(x>y)
print(x<y)
print(x>=y)
print(x<=y)

#Assignment operators

# "="
# "+="
# "-="
# "*="
# "/="
# "%="
# "**="

numm = 15
numm = numm + 10
print(numm)
numm = numm - 5
print(numm)
numm = numm * 2
print(numm)
numm = numm / 10
print(numm)
numm = numm % 2
print(numm)
numm = numm + 10
print(numm)
numm = numm ** 2
print(numm)


#Type conversion

a1 = 15 #int
b1 = "22" #str
c1 = 19 #int
d1 = "10" #str

print(a1+int(b1))
print(c1+int(d1))

# Input and Output

#nAme = input("Enter your Name: ")
#print("Welcome" , nAme)
#aGe = input("Whats your age?")
#print("Nice you turned" , aGe)

#mArks = input("How many marks did you got in your maths exam?")
#print("Wow thats great you scored", str(mArks) , "marks in exam")

#val1 = input("First number?")
#val2 = input("Second number")
#print("Sum of val1 and val2 is;",int(val1) + int(val2))

#Assesment
# Q. write a program to input side of a square and print its area

#side = input("What is the value of side?")
#print("Area is equal to side x side")
#every_sides = (int(side)*int(side))
#print("the area  of square is",every_sides)


#It annoys you alot when you have to write more code thats why adding hashtag on above code


# String functioning

intro = "Im faisal khan.\n Im 17 year old."
print(intro)
#Back slash is used when you have to write in next line

duction = "Im doing be. In aiml. \n i will work hard for better placement"

print(duction)


# Adding of strings
str1 = "Faisal"
str2 = "khan"
print(str1+str2)
print(str1 + " " + str2)

#Finding length of string (len())
print(len(str1))
print(len(str2))


#Indexing
naam = "Faisal_khan"
print(naam[1])
print(naam[6])

print(naam[-1])
print(naam[-6])

print(naam[1:3])
print(naam[:6])
print(naam[-3:-1])

# 1. .endswith("")
naam = "Faisal_khan"
print(naam.endswith("khan"))
print(naam.endswith("faisal"))

# 2. .capitalize()
naam1 = "im faislest khan"
naam1 = (naam1.capitalize())
print(naam1)

# 3. .replace(

name2 = "Im faisal khan and im learning python"
print(name2.replace("faisal","ameen"))
print(name2.replace("python","javascript"))

name3 = "Im faisal khan im gonna master Pythonn"
print(name3.find("f"))
print(name3.find("master"))

# 5. .count()

name4 = "This is faisal speaking im gonna master pythonn in 2 months"
print(name4.count("a"))
print(name4.count("k"))
print(name4.count("z"))

# 6. .append

lst = ["car" , "bus" , "auto" , "bike"]
lst.append("cycle")
print(lst)


# 7. .insert

lst.insert(0 , "carrr")
print(lst)

# 8. .extend

lst.extend([1 , 2 , 3])
print(lst)

lst.pop()
print(lst)

del lst[2]
print(lst)

lst.remove("bike")
print(lst)

lst.clear()
print(lst)

lst1 = [10 , 25 , 30 , 22 , 70 , 95]
lst1.sort()
print(lst1)
lst1.sort(reverse=True)
print(lst1)

marks = 90 # Can also use int thn input
if (marks>=95):
    print("A GRADE")
elif(marks>=70):
    print("B GRADE")
elif(marks>=55): 
    print("C GRADE")
else:
    print("FAIL")



# Functions :
# It is reusable block of code


def greet(): #FUnction
    print("Welcome to python!") #function body
greet()

def greet(name):
    print("Hello" , name)
greet("FAISAL")

# Multiple parameters
def add(a,b):
    print(a+b)
add(10,20)

# Return statement

def ad(a,b):
    return a+b
result = ad(15,25)
print(result)

# Dictionaries

info = {
        "nameeee" : "Faisal",
        "subjects" : ["python" , "c++" , "Java"],
        "topics" : ("dictionaries" , "Sets"),
        "age22" : 18,
        "is_student" : True,
        "marks" : 95.7,
}
print(info)
print(type(info))
print(info["nameeee"])
print(info["subjects"])
print(info["age22"])
# We can make changes in dictionary
info["nameeee"] = "Faisal"" ""khan"
info["Nickname"] = "Sher" " " "khan"
print(info)


# Nested dictionaries

student = {
            "name11" : "FAISALEST KHAN",
            "subjects" : {
                    "maths" : 97,
                    "chem" : 99,
                    "phy" : 94,
                
            }   
}

print(student)
[print(student["subjects"])]
[print(student["subjects"]["maths"])]

## Dict functions
# .key()

print((student.keys()))
print(list(info.keys())) #Can also make dict keys to list

# .values
print(student.values())
print(list(info.values()))

# .items
print(student.items())
print(list(info.items()))

# To create a list of only one item
pair = list(student.items())
print(pair[0])
print(pair[1])

pairs = list(info.items())
print(pairs[4])

# .get("key")

print(student.get("name11"))
print(student.get("age11")) #There is no key present like that so none value
# print(student["age11"]) #This will show error thats why we use get.("key") as we write long long programs


# .update
new_dict = {"Grade" : 9}
student.update(new_dict)
print(student)
# Or                               # Both will work

student.update({"grade" : 9})
print(student)


# Sets 
# -> Set is the collection of unordered value 
# -> Each value in the set must be unique and immutable

collection = {1 , 2 , 3 , 4 , "Hello world" , 2.2 ,}
print(collection)
print(type(collection))

collection1 = {1 , 2 , 2 , 2 , 3 , 3 , 3 , "hello" , "hello"}
print(collection1)

collection3 = set()
print(type(collection3))

# Functions of sets

# set.add()

collection = set()
collection.add(1)
collection.add(2)
collection.add(3)
collection.add(4)
collection.add("helololo")
print(collection)

# set.remove()
collection.remove(1)
collection.remove(2)
print(collection)

# set.pop()

print(collection.pop()) # Prints any random value
print(collection.pop())

# set.clear()
print(collection.clear())
print(len(collection))

# set.union
set1 = {1 , 2 , 3, 4}
set2 = {3 , 4 , 5 , 6}
print(set1.union(set2))

# set.intersection
print(set1.intersection(set2))


# While loops
x =1
while x<=10:
    print(x)
    x +=1
a = 3  
i = 1
while i<=10:
    print(f"{a} x {i} = {a*i}"  )
    i += 1
    
count = 1
while count<=3:
    print(count , "Hello")
    count +=1
    
l = 1
while l<=100:
    print(l)
    l+=1
    
nums = [1 , 4 , 9 , 16 , 25 , 36 , 49 , 64 , 81 , 100]
idx = 0
while idx<len(nums):
    print(nums[idx])
    idx += 1
    
r = 1 
while r <= 6:
    print(r)
    r += 1
    if r==5:
        break
    
print("Loop ended")

i = 0
while i <=7:
    if i == 1:
        i +=1
    print(i)
    i += 1


# For loop   
numss = [1 , 4 , 9 , 16 , 25 , 36 , 49 , 64 , 81 , 100]
x = int(49)
for num1 in numss:
    if num1==x:
        print("Found" , x )
        break
   
    print(num1)
    
scores = [88 , 79 , 83 , 91 , 92 , 77 , 56]

total = 0
highest = 0
lowest = 0
average = 0
toppers = 0
for score in scores:
    total+=score
    if score>highest:
        highest = score
    if score<lowest:
        lowest = score
    if score>=90:
        toppers+=1
    
average = total / len(scores)


print("TOTAL - " , total)
print("HIGHEST MARKS - " , highest)
print("LOWEST MARKS - " , lowest)
print("AVERAGE MARKS - " ,average)
print("TOPPERS - " , toppers)

#Enumerate() attaching the index values

studentss = ["Arav" , "sneha" , "Rohan" , "abhi"]
for i , name in enumerate(studentss, start=1):
    print(f"{i} . {name}")
    
#zip

names = ["Arav" , "sneha" , "Rohan" , "abhi"]
marks_maths = [88 , 98 , 45 , 87]

for name,score in zip(names, marks_maths):
    grade = "A" if score >=90 else "B" if score>=75 else "C"
    print(f"{name}-> {score} Grade : {grade}")
    
# While loop + break + continue
data = [10 , 5 , 0 , 22 , 3 , 15 , 99]
index = 0

while index < len(data):
    value = data[index]
    index +=1
    if value < 0:
        continue
    if value >35:
        break
    print(f"Processing : {value}")
    
# Restaurant bill using zip and for loop
items = ["Burger" , "Pizza" , "Sandwich" ,"donuts"]
prices = [240 , 200 , 150 , 100]
for item,price in zip(items , prices):
    total += price
    gst = total *18/100
print(f"ITEMS - {items}")
print(f"Sub-TOTAL -> {total} \n GST - {gst}")
final = total + gst
print(f"YOUR TOTAL BILL IS {final}")


# Range
a = 9
i = 1
while i in range (0,11):
    print(f"{a} x {i} = {a*i} ")
    i += 1
    
# Functions
