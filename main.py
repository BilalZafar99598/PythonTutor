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
# msg = "Hello\tMy\tName\tis\tBilal"
# print(msg.count("L"))
# print(msg.find("hello"))
# if find() function is return -1 then it means sunstring not found
# print(msg.index("hello"))
# but in index() function if substring not found it gives us ValueError Exception.
# print(msg.endswith("L"))
# print(msg.expandtabs())

"""
Q: Find the Even Odd Values from given Python List and Separate Even List and Odd List?
Ans:
    if-else
    3 Lists
    Arthimetic Opt.
    
Loop are use for Iterations.
Example 
    Bilal
    Bilal 
    Bilal
        

"""


# print("Bilal")
# print("Bilal")
# print("Bilal")
# print("Bilal")
# print("Bilal")
"""
Our code is reduntant 
This is actually Code retundancy. So in programming we should avoid code retundancy.

FOr Loop:
        C++ Example:
            for(i=2;i<=10;i++)
            {
                // Loop's Body
            }

        Python's Syntax:
            for variable_name in range():
                
"in" is a keyword in Python

IMPORTANT Point:
    range() function by default start from 0 value so ending value will excluded
    By Default Loop is increamented by 1 Value 
"""
# allNumbers = [1,2,3,4,5,6,7,8,9,10]
# for i in range(20):
#     print(i)
# evenList = []
# oddList = []
# allNumbers = [1,2,3,4,5,6,7,8,9,10,13,16,256,23324,21]
# # print(len(allNumbers))
# for i in range(len(allNumbers)):
#     if allNumbers[i]%2==0:
#         evenList.append(allNumbers[i])
#     else:
#         oddList.append(allNumbers[i])
#
# print(allNumbers)
# print(evenList)
# print(oddList)

"""
List's Built-In Functions in Python.

reverse()
sort()
index()
insert()

"""
# k = [1,2,3,4,5,6,7,8,9,10]
# print(numbers[::-1])
# print(reversed(list))

nums = [3,5,2,1,10,10]
# print(nums)

# nums.append(123)
# print(nums)

# print(nums.count(10))

# print(nums.index(3))

# print(nums.insert(456,1))

"""
break and countine statement.
Basically these are keywords,
Break will break our for loop 
and Continue will skip the current step
"""

# for i in range(10):
#     if i==3:
#         break
#     else:
#         print(i)

"""
Python Functions
There are two types of functions in programming 
1. Built-In functions
2. User-Define Functions
Syntax:
        Function Definition
        def functionName():
            // Function's Body
            return 
            
            
        Function Invokement
        Function Call
"""
# a = 450
#
# def add():
#     """
#
#         Actually these variables are Local Variable
#         a and b has only life in add() function
#
#     """
#     # a = 550
#     b = 110
#     sum = a+b
#     print(sum)
#     # return sum
#
# """
# If we want to use function then we must call that function
# """
# # add()
#
# add()
"""
Very Basic Calculator Functionality using Python Functions
"""

# num1 = 100
# num2 = 50
#
# def sum():
#     return num1+num2
#
# def sub():
#     return num1-num2
#
# def mul():
#     return num1*num2
#
# def divi():
#     return num1/num2
#
# def remainder():
#     return num1%num2
#
#
# print("Sum Result is: "+str(sum()))
# print("Sub Result is: "+str(sub()))
# print("Mul Result is: "+str(mul()))
# print("Divi Result is: "+str(divi()))
# print("Modulus Result is: "+str(remainder()))


"""
List's Built-In Functions
"""


"""
Q: How to reverse our Python List
"""

# digits = ["zero","one","two","three"]
# digits.reverse()
# print(digits[::-1])

"""
Q: How to sort our List in ascending order
"""

# intList = [0,40,1,32,23,13]
# intList.sort()
# print(intList)

"""
Q: How to sort our List in decending order
"""
# intList.sort(reverse=False)
# print(intList)


# digits = ["zero","one","two","three"]
"""
Q: How to add new Element in Python List
When we will add new Element using append() function so element will add at the last index of the List

"""
# digits.append("four")
# print(len(digits))

"""
Q: How to add new Element in Python List at Specific Position
"""
# digits.insert(1,"1")
# print(digits)

"""
Q: How to clear Python List ?
"""
# digits.clear()
# print(digits)

# digitsCopy = digits.copy()
# print(digitsCopy)

"""
Q: How to Access data from Python List?
Ans:
    Based on index number
"""

# digits = ["zero","one","two","three",1,2,3,4,5,3.14,5.2]
# print(digits)
# print(digits[0:3])
"""
Difference between Mutable and Immutable in Python?
Python Lists are Changeable (Mutable)
So List are Mutable in Python.
Python's List are Ordered List
Python List are allows us duplicate values and multiple datatypes of an element
"""

digits = ["zero","one","two","three",4]
# del digits[3]
# print(digits)
# print(digits)
# digits.pop()
# print(digits)
"""
Differenece Between del and pop()
Ans:
    del is keyword and pop() is a function
    by using del keyword we can remove specific list item
    and pop() will only remove the last index's element
"""
"""
Nested List
Means List within a List
"""
# l1 = [0,1,2]
# l2 = ['zero','one','two']
# l1.append(l2)
# print(l1[3][::-1])

"""

Packing vs Unpacking
Packing
"""

# This is Packing
list1 = ["zero","one","two","three",'0,1,2,3,4,5',"After-List"]

# Unpacking
# zero,one,two,three, *intList, afterlist = list1
# print(type(list1))
# print(one)
# print(two)
# print(three)
# print(type(intList))
# print(type(afterlist))

"""
Integer 
Float
String
Boolean
List

"""

"""
In Boolean there are only two conditions either True or False

False and True are keywords in Python
 
 
"""

# a = False
# b = True
# print(type(a),type(b))

"""
List Comprehension
What is List Comprehension?
Ans:
    It is a ShortHand way to create a Python List.
"""

# listComprehension = [i for i in range(10)]
# print(listComprehension)

# emptyList = []
# for i in range(15):
#     emptyList.append(i)
# print(emptyList)

"""
DataTypes
String, Integer these are all for only single element 
But for collection of elements we have a 4 datatypes

list = [1,2,3,4,5,6]

1. List
2. Tulpe.
3. Set.
4. Dictionary.

As we already discussed about List now we are discussing about Tuples

Tuples are Immutuble it means we cannot change tuple data elements
So tuples are ordered in nature and we can access elements by using index technique


Tuple's Syntax:
    Ans:
        tuple1 = (1,2,3,4,5)


"""
# tuple1 = (1,2,3,4,5)
"""
How to create Tuple only contain single element
"""
# isTuple = ('"Bilal","Ali"',)
# print(type(isTuple))
# tuple1[0] = "one"

# print(tuple1)
# print(tuple1[0])

"""
Tuples are Immutable means we cannot change
if we want to change an element then 1st we will convert tuple into list and then changes and after changes we will
back to tuple.
B/c List allows us to change element
"""

# tuple1 = (0,1,2,3,4)
# tuple2List = list(tuple1)
# # print(type(tuple2List))
# tuple2List[2] = "TWO"
# # print(tuple2List)
# # print(tuple(tuple2List))
# backtoTuple = tuple(tuple2List)
# print(backtoTuple)

# del tuple1[4]
# print(tuple1)

# tuple0 = (0,1,2,3,4)
# tuple1 = list(tuple0)
# del tuple1[4]
# print(tuple1)

# l = list()
# pass keyword

# a = 50
# if a>10:
#     pass
# b = 100
# c = 150
# print(a,b)

"""
Comparison Operators
less than
greater than 
equal to
not equal to
greater than equal to
less than equal to

"""
# a = 100
# b = 150
# if a>b:
#     print("A is Greater Number")
# else:
#     print("B is Greater Number")

"""
enumerate() use to iterate over list and return list elements as well as index value.
"""
# animals = ["Cat",'Dog','Lion','Cheeta']
# for index,value in enumerate(animals):
#     print(f"At Index Number: {index} Element is: {value}")
















