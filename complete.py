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