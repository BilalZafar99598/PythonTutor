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
a = 100
b = 50
print("Sum is :"+str(a+b))
print("SUB is :"+str(a-b))
print("MUL is :"+str(a*b))
print("DIVISION is: "+str(int(a/b)))
print("Remainder OR Modulus is: "+str(100%51))

