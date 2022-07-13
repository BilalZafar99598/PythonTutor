"""
# Variable
Q: What is variable ?
Programming Fundamentals are same almost
variables, datatypes, loops, if-else statements, switch statments,

Ans:
   Variable is a container or holder that contains some data or hold some data, A Data is in the form of
    some values, character or word.

Q: How to use Variable in Python?
Ans:
    Before using variable we must understand variable's Syntax.
    There some rules for creating a variable in programming lan.
    Always start from Alphabets not a Numeric Value.
    We can use underscore at the beginning of the variable.
    and Variable's name should be user friendly.

    Exp: 1abc This is wrong way to create variable
        _A This is valid.
        A,a,ABC,XYZ

        Variable is a User Define.

        Syntax of Variable:
                Assignment Operator: =
                int a = 10;  Here semicolon is Statment terminator  C++ Syntax
                Python's Syntax
                a = 10

Q: Is Python Case-Sensitive Language ?
Ans:
    Yes, Python is a Case-Sensitive Language. Why ?
    Because here is example:

    Let say we have 2 variables with same name.

    name = "Ali"
    name = "Omer"

    Name and name are equal?
    No, they both are different so we created 2 different variables this is
    because of Python is a Case-Sensitive Lan...

    Variable Declaration and Variable Initialization.
    Variable Declaration:
                        In simple words, we can say that we just create a variable this is
                        called Declaration.

    Variable Initialization:
                        When we intialize any data to a Variable is called a Variable Initialization.

    name = "Ali"

Q: How to display data in Python?
Ans:
    For Display Data on console we use Python's Built-In Function print()

"""

# name = "Ali"
# name = "Omer"
#
#
# print(id(name))
# print(id(name))
# print("My name is ",name)

"""
Concatenation in Python
Example 
Plus (+) Operator is use for Concatenation

"""

# Static Code and Hard Code
# firstName = "Bilal"
# lastName = "Zafar"
# fullName = firstName+" -- "+lastName
# print(firstName+" - "+lastName)
# print("My Full Name is: "+fullName)

#Text Formatting
# print(f"My Full Name is {fullName}")



# Dynamic Code OR Generic Code
# firstName = input("Please Enter Your First Name!!")
# lastName = input("Please Enter Your Last Name!!")
# print(f"My First Name is {firstName} and my Last Name is {lastName}")


# String Data Type.
# name = 'Bilal Zafar'
# print(name)



# Single Quotes create issue when we want to use with Apostoph
# print("This is Bilal's Laptop")

"""

Everything is an Object in Python 
Object and Class 
class Animal:
    name = 'Cat'
    age = 2
    price = 5000

We will access Class's attributes by creating an Object of that Class
# Q: How to check datatype of variable in Python
Ans:
    We can check datatype of variable by using Built-In Function name type(variable_name)
    
    Data Type of Bilal Zafar is str
    
"""



# name = "Bilal Zafar"
# age = 25
# #Concatenation
# print(type(name))

# Type Casting
"""
Q: What is Type Casting?
Ans:
    In simple words Type casting is to convert one datatype to another datatype.
    So, In Python we can use built-in functions for Type Casting.
"""



# This is Comment But Shortcut for single Comment is ctrl+/ Shift+RIght Arrow for selection
# print(f"Data Type of {name} is"+str(type(name)))






"""
Q: What is list in Python?
Ans:
    In Simple words, actually Array is a List in Python and if you are not familiar with Array
    so Array basically a Combination of more than single value OR Data.

Name of Brackets
1. () This is Parenthese 
2. []  This is Square Bracket
3. {}   This is Curly Bracket
4. <> This is Angular Brackets
"""





# This is not a Multiple Data actually it's only single value because written within Double Quotes.
# name = "Omer, Ali, Khan"
age = 25
weight = 78.56
# name = "Ali"
# names = ['Ali','Omer','Khan']

# floatToStr = str(weight)
# print(type(floatToStr))

# print(type(age), type(weight), type(name), type(names))

"""
List Index:
            Actually, In simple words indexing is just a like a Position or Location of any list item or element.
        IMPORTANT:
                    List Index is always start from Zero (0).
                    
        List Indexing Syntax:
                    List_Name[Index_Number]                
    Q: How to access data from List?
    Ans:
        By Using List
        
    Slicing:
            "BILAL"
    Slicing Syntax:
                StringName OR ListName[start-index:stop-index]
        IMPORTANT POINT IN SLICING:
        ENDING-INDEX is excluded
         
"""
# names = ['Ali','Omer','Khan']
# print(names[1])
# name = "Omer, Ali, Khan"
# print(name[5])
# print(name[0:4])

# names = ['Ali','Omer','Khan']
# print(names[0:2])

"""
Arithmetic Operators in Python 
+
-
Division /
Multiplication *
Modulus % 
What is Modulus ?
Ans:
    In simple words, Modulus is Remainder in division
    Exp:
        5/2
        In this case our Remainder is 1 so actually this One is Our Modulus.
    

"""


# Implementation of Arithmetic Operators
# a = 100
# b = 50
# print("Sum is :"+str(a+b))
# print("SUB is :"+str(a-b))
# print("MUL is :"+str(a*b))
# print("DIVISION is: "+str(int(a/b)))
# print("Remainder OR Modulus is: "+str(100%51))

"""
Assign single value to multiple variables
"""
# a = 10
# b = 10
# c = 10
# a = b = c = 20
# print(f"Value of A is: {a}")

# animals = ["Cat","Dog","Lion"]

# One D Array, 1 Dimension
# print(animals[0][0:2])
# print(animals[1])
# print(animals[2])


"""
List Unpacking
"""
# animals = ["Cat","Dog","Lion"]
# cat,dog,lion = animals
# print(cat[0:2])
# print(dog)
# print(lion)

# Q: How to print list in Reverse Order

# print(animals[::-1])

# val = "0123456789"
# print(val[::3])
# numbers = [0,1,2,3,4,5,6,7,8,9,10]

# Built-In Function
# Q: How to print minimum value from Python List
# print(min(numbers))

# Q: How to print maximum value from Python List
# print(max(numbers))
# print(numbers[::3])


# Q: What is Append Function in Python ?
# Append Function is always insert data in list at Last Index
# empt_list = []
# empt_list.append("Ali")
# empt_list.append("Omer")
# empt_list.append("Haris")
# empt_list.append("Haris")
# print(empt_list)

# Print only unique data ignore duplicate data


# DataType Set
# list_to_set = set(empt_list)
# print(type(list_to_set))

# print(set(empt_list))

# Q: Find Even and Odd Number ?
# Keywords OR Reserve Words
# We cannnot use keywords as a Variable Name
# if for else in

# # Variable Cases
# # Camel Case
# fullNameOfStudent = "Ali"
#
# # Pascal Case
# FullNameOfStudent = "Bilal"
#
# # Snake Case
# full_name_of_student = "Saad"
# print(fullNameOfStudent,FullNameOfStudent,full_name_of_student)

"""
Q: Why we use IF-ELSE statement?
Ans:
    When we want to execute our program based on any specific condition then we use it or make decision.
    
    Syntax:
    if and else are keywords.
    In Python there is a concept that is called Indentation.
    Like in C++ how to use IF-ELSE statment block
    if(specific_Condition)
    {
        Body of IF    
    }
    else
    {
        Body of Else
    }
    
    Python's Syntax:
    if specific_Condition:
        Write your code 
        
    else:
        Else Part    
    
Q: Find Even and Odd Value?
Ans:
    Hint:
        1. IF-ELSE Statement
        2. Arthimetic Operator
 
"""
# digit = 50
# if digit%2 == 0:
#     print("Your {Number} is Even")
# else:
#     print("Your Number is Odd")


"""
Q: Take value from user and find Even/Odd Value?
Ans:
    Hint:
        use input method
        
        By Default Input function gives us String value
"""
# digit = int(input("Please Enter your Number:"))
# if digit%2 == 0:
#     print(f"Your Number {digit} is Even")
# else:
#     print(f"Your Number {digit} is Odd")


"""
String's Built-In Functions
lower()
"""
name = "bilal"

# print(name.lower())
# print(name.capitalize())
# print(name.upper())
# print(name.isdigit())

# a = "10A"
# print(a.isdigit())

# print(len(name))
# Python is a Case-Sensitive Langugae
# a and A are not Equal
msg = "Hello\tMy\tName\tis\tBilal"
# print(msg.count("L"))
# print(msg.find("hello"))
# if find() function is return -1 then it means sunstring not found
# print(msg.index("hello"))
# but in index() function if substring not found it gives us ValueError Exception.
# print(msg.endswith("L"))
print(msg.expandtabs())







