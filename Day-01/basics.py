
#--------------------PRINT STATEMENTS--------------------
print("Hello World")
print("Hello Python")
print("My Name is Ankit")
print("I am learning AI Engineer")


#python can do calculations also 
print(10+20) #calculation of addition
print("10+20")  # it will print the text only 


#Q1) Write a program that displays this:-
#My AI Engineering Journey
#Name: Ankit
#Goal: AI Engineer
#Day: 1
#Language: Python
#I am starting my 300-day journey today!

print("My AI Engineering Journey")
print("Name: Ankit")    
print("Goal: AI Engineer")
print("Day: 1")
print("Language: Python")
print("I am starting my 300-day journey today!")


#--------------------VARIABLES--------------------

name = "Ankit"
age = 21
goal = "AI Engineer"

print(name)
print(age)
print(goal)

print("My name is ",name)
print("I am ",age," years old")
print("My goal is to become an ", goal)


#Checking the data type with type()--------------------

name = "Ankit"
age = 21
height = 5.8
is_student = True

print(type(name))
print(type(age))
print(type(height))
print(type(is_student))

#diffrence between age = 21 and age = "21"
age = 21 # it is a integer and python can perform various calculations with it
print(age+1) # it will print 22

age = "21" # it is a string and python can not perform calculations with it
print(age+"1") # it will print 211 because it is a string and python will concatenate the two strings because we are joining a string with another string "21" + "1" = "211"



#--------------------ARTHEMETIC OPERATORS-------------------------
a = 20 
b = 6

print(a+b) #addition
print(a-b) #subtraction
print(a*b) #multiplication
print(a/b) #division
print(a//b) #floor division
print(a%b) #modulus or remainder left over after division
print(a**b) #exponentiation


#One more important concept: Operator Precedence-------------------------
print((10 + 5) * 2) #here the addition will be done first because of the brackets and then multiplication will be done\
print(10 + 5 * 2) # here multiplication will be done first and then addition will be done because of operator precedence
print(20%6)

#----------------Comparision Operations----------------------- 
age = 21
#CHECKING COMPARISION OPERATORS
#1.Is age greater than 18?
print(age>18) # it will print True because age is 21 which is greater than 18

#2.Is age less than 18?
print(age<18) # it will print False because age is 21 which is not less than 18

#3.Is age equal to 21?
print(age==21) # it will print True because age is 21 which is equal to 21

#4.Is age not equal to 25?
print(age!=25) # it will print True because age is 21 which is not equal to 25

#5.Is age greater than or equal to 21?
print(age>=21) # it will print True because age is 21 which is equal to 21

#6.Is age less than or equal to 18?
print(age<=18) # it will print False because age is 21 which is not less than or equal to 18


#-------------LOGICAL OPERATORS-----------

#-- AND operator(BOTH conditions must be True)
age = 20
print(age > 18 and age < 25) # it will print True because both conditions are True

age = 30
print(age > 18 and age < 25) #it will print False because one condition is True and the other is False

marks = 75
print(marks >= 40 and marks <= 100) # it will print True because both conditions are True

marks = 35
print(marks >= 40 and marks <= 100) # it will print False because one condition is True and the other is False


#--OR operator(AT LEAST ONE condition must be True)

age = 17
print(age < 18 or age > 60) # it will print True because one condition is True and the other is False


age = 30
print(age < 18 or age > 60) # it will print False because both conditions are False

day = "Sunday"
print(day == "Sunday" or day == "Saturday") # it will print True because one condition is True and the other is False

day = "Monday"
print(day == "Sunday" or day == "Saturday") # it will print False because both conditions are False


#--NOT operator(IT will reverse the condition (reverses True/False))

is_student = True

print(not is_student) # it will print False because is_student is True and not operator will reverse it to False

#mixed questions of logical operators (and,or,not)
     
is_logged_in = True
is_admin = False

print(is_logged_in and not is_admin) # it will print True because is_logged_in is True and not is_admin is True because is_admin is False and not operator will reverse it to True
