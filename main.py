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
    and pop() will only remove the last index's element.
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

"""
in keyword in Python
it is use for check the presence of any data
or keyword 
logical operators 
AND and
OR  or
NOT not
"""

# names = ["Ali",'Omer','Khan','Saad']
# if "ali" or "Ali" in names:
#     print("Yes this name is available")
# else:
#     print("NO this is not available ")

# ithNames = []
# names = ["ali",'saad','khan','bilal']
# for index,value in enumerate(names):
#     if "i" in value:
#         print("Yes have")
#         ithNames.append(value)
#     else:
#         print("NOT")
# print(ithNames)

# # ithNames = []
# names = ["ali",'saad','khan','bilal','jamal','kamal','adnan']
# print("List Before Loop: ",names)
# for index,value in enumerate(names):
#     if "i" not in value:
#         # List are Changable into uppercase
#         names[index] = value.upper()
#     # else:
#         # del names[index]
# print("List After Loop: ",names)

"""
Collection of Data.
Unique elements.
No duplication is allow
NO Specific Order.


{}
Syntax:
    set1 = {1,2,3,4,,5,6}
"""

# set1 = {'a','b','c','d','e','a'}
# set1 = {250,1,2,53,4,5,6,7,8,94,94}
# print(set1)

"""
Sets are different because there is no key value pair
Dictionary
It is use for key-value pair

Syntax:
    { key:value }
"""

# studentData = {"name":"Bilal","Age":25,"Position":"Software Engineer"}
# print(studentData.items())

"""
Dictionaries Built-In methods
values()
items()
keys()
"""
# print(studentData.keys())
# print(studentData.values())
# print(studentData.items())

"""
Add New Key Value Pair 
"""

# studentData["Country"] = "Pakistan"
# print(studentData)

"""

How to Access data from Dictionary ?
As we used Index number in list to access data from list but in dictionary we cannot use index number 
we will keys to access Data.

"""
# print(studentData['Age'])

# print(studentData.get("name"))
# print(studentData)
# print(studentData.pop("Bilal"))
# print(studentData)

"""

How to change speicific value in Dictionary


"""

# studentData = {"name":"Bilal","Age":25,"Position":"Software Engineer"}
# studentData["Position"] = "Python Teacher"
# print(studentData)

# list1 = ["M","Na","i","Bil"]
# list2 = ["y","me","s","al"]
# print(["My","Name","is","Bilal"])

"""
Functions are two types 
1. Biilt-in 
2. User Define Functions

What is difference between Function and Method?
Ans:
    Actually, Python not a prue OOP based language we can use it as a functional programming.
    Function that use with OOP concepts is called a Method.
    This is function
    def add():
            sdasda

    class Calculator:
    These are methods 
    b/c functions written inside of a class
        
        Non-Parameterized Functions
        def add1():
            adasdassd
        // This is function definition
        def sub1():
            asdasdasd
            
        If we want to utilize any function then we must call that function.
        
        sub1()    
            
        Parameterized Functions 
        let say we have a sum function then we will pass 2 parameter or arguments to find solution.
        
        Q: Difference between parameters and arguments
        Ans:
            Parameters are dummy values that we pass while creating a function.
            But Arguments are the real value or data that we pass to a function or method.
            
        When we define our function and values we pass that is parameters.
        Example:
            def sum(a,b)
            c = a+b
            :return c 
            
            print(sum(10,5))
            
    
"""

# def username(firstname, lastname):
#     # print("My First Name is {} and Last Name is {}".format(firstname,lastname))
#     print(f"My First Name is {firstname} and Last Name is {lastname}")
#
#
# """
# # This is the way to call a call
# So why we call function b/c we want to execute it's functionality.
# """
# username(" Muhammad Bilal","Zafar")



"""
you use 5 parameterized function to find
FUnctions must be parameterized.

sum
sub
multiplication
div
modulus

"""

"""
Iterate over the list and find each word which contains lenght 2 or more than and starting and ending character
must be same. SO, count them total these words in list.
"""

# list1 = ["abc","abbbca","baacvb","faabbbf","ababbabab","ab","a"]
# checkwords = []
# counter = 0
# for i in list1:
#     if len(i) == 2 or len(i) > 2:
#         if i[0] == i[-1]:
#             counter +=1
#             checkwords.append(i)
# print(checkwords)
# print("Total Words are",counter)

"""

Even: 2,4,6,8,10 etc....
Odd: 1,3,5,7,9,11,13,15,17,19,21 etc....
Prime 3,5,7,11,13,17,19,23,29 etc....
Prime number is only divisible by itself. 13/13 == 0 15-- 5*3=15 15/3=5, 15/5=3
21/7=3

"""
# n = int(input("Please Enter Number to Check Prime:"))
# checker = False
# for i in range(2,n):
#     if n%i == 0:
#         checker = True
#         break
# if checker == True:
#     print(f"{n} is a Not Prime Number")
#     # pass
# else:
#     print(f"{n} is PRIME Number")
#     # pass

# a = 210
# b = 150
# c = 50
"""
Find Greater Number amongs three values how ?

"""
# if a>b and a>c:
#     print("A is greater")
# elif b>a and b>c:
#     print("B is greater")
# else:
#     print("C is greater")

"""
Libraries 
built-In functionality we use libraries in programming languges.

"""
# import os
# import pandas

"""
Iterate over the list and find total Even, Odd and Prime number and separate them in each list.
"""



EvenOddPrime = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

evenList = []
oddList = []
primeList = []
evenCounter = 0
oddCounter = 0
primeCounter = 0

# checker = False
# for ind,val in enumerate(EvenOddPrime[2:]):
#     # print(val)
#     for i in range(2,val):
#         if val%i==0:
#             # print(val)
#             checker = True
#             break
#         elif checker == True:
#             pass
#         else:
#             print(val)
            # else:
        #     print(val)
        #     break
    #     # else:
    #     #     print("Not")
    # if checker == True:
    #     print("Not Prime")
    # else:
        # print("Prime")
        # primeList.append(val)
# print(evenList)
# print(oddList)
# print(primeList)


# EvenOddPrime = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# lower = EvenOddPrime[0]
# upper = EvenOddPrime[-1]

# print("Prime numbers between", lower, "and", upper, "are:")
# evenList = []
# oddList = []
# primeList = []
# for num in range(lower, upper + 1):
#    # all prime numbers are greater than 1
#     if num > 1:
#         for i in range(2, num):
#             if (num % i) == 0:
#                 break
#         else:
#             # print(num)
#             primeList.append(num)
#
#     elif num%2 == 0:
#         evenList.append(num)
#
#     else:
#         oddList.append(num)
#
# print(primeList)

# list1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# for num in range(list1[0],list1[-1]+1):
#    for i in range(2,num):
#        if num%i==0:
#            break
#    else:
#        print(num)
#

# def sum(x):
#     return x+1
# print(sum(2))

# x = lambda a:a+1
# # print(x(2))
# sum = x
# print(sum(4))

# list1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# n = []
# for num in range(list1[0], list1[-1] + 1):
#    if num > 1:
#        for i in range(2, num):
#            if (num % i) == 0:
#                break
#        else:
#            # print(num)
#            n.append(num)
# print(n)
# randomList = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# empty = []
# primeCounter = 0
# primeChecker = False
# for num in range(randomList[0],randomList[-1]+1):
#     # print(num)
#     if num > 1:
#         for i in range(3,num):
#             if num%i == 0:
#                 break
#         else:
#             # print(num)
#             # if num == 2:
#             #     continue
#             # else:
#             #     empty.append(num)
#             if num!=2:
#                 primeChecker = True
#                 primeCounter += 1
#                 empty.append(num)
# print(empty)
# print(primeCounter)

# tuples
# tuple1 = ("abc",)
# print(type(tuple1))

"""
String Variables and String Literals
"""
#
# name = "Bilal Zafar"
# print(type(name))
#
# num = 50

"""

Here name is a string variable but "Bilal Zafar" is a String Literals 
In other words our real data is called a String Literals.

"""


# def add(a,b):
#     return a+b
#
# sumFunc = add
# print("Sum is: ",sumFunc(55,15))


"""
This is a Lambda Function use for short time period.
If we want to use logic without creating Function Name then we will use Lambda Function
Anoynomous Function
for using Lambda function we must use lambda keyword.
"""
# sum = lambda a,b:a+b
# print("Sum is :",sum(45,15))

# mul = lambda x:x*x
# print(mul(5))

# def mul(x):
#     return x*x
# print(mul(5))

"""

Parameterzied Functions

"""

# def add(a,b):
#     return a+b
# print(add(5,10))

# def add(a,b):
#     return a+b
# print(add(5,10,15,6))

"""
Non Keywords Arguments
*args
"""

"""
When Number of Arguments are Unknown then we will use Non-Keyword Arguments
Is it mandatory always use *args ?
Ans:
    No, args is just like a Variable it's user define.

"""


# def addNumber(*tupleOfValues):
#     print(type(tupleOfValues))
#     sum = 0
#     for n in tupleOfValues:
#         # sum = sum+n
#         sum +=n
#     return sum
# print(addNumber(10,15,15,50,100,33,112,55,33,55))


# n = 10,15,15,50,100,33,112,55,33,55
# print(type(n))

"""
Keywords Arguments
**kwargs

kwargs is a user-define.

"""
# def userData(**stdRecord):
# def userData(**stdRecord):
#     print(type(stdRecord))
#     for keys,values in stdRecord.items():
#         print(f"{keys} is {values}")
# userData(FirstName="Bilal",Age=26,Education="BSCS")

# std = {}
# std["Name"] = "Ali"
# std["Age"] = 30
# print(std)

"""
Find Maximum value from list
"""
# l = [3,5,77,44,6,4,33]
# print(max(l))

# def checkMax(list1):
#     print(type(list1))
#     m = 0
#     for i in list1:
#         if i > m:
#             m = i
#     return m
#
# print(checkMax([33,44,22,155,2,56,100]))


# def checkMin(list1):
#     print(type(list1))
#     m = list1[0]
#     for i in list1:
#         if i < m:
#             m = i
#     return m
# print(checkMin([33,44,22,155,2,56,100,1,-10000]))

"""
"""

list1 = ['P','Y','T','H','O','N']
"""
Output:
        PYTHON
"""
# for i in list1:
#     print(i)
"""
Built-in Functions
"""
# str1 = ''.join(list1)
# print(str1)

"""
Find the Differences between 2 lists 
[3,4,3,5,5,6]
[33,55,22,77,55,66]
By using List Comprehension way
"""

# list1 = [i for i in range(15)]
# list2 = [j for j in range(0,20,3)]
#
# diff1 = list(set(list1)-set(list2))
# diff2 = list(set(list2)-set(list1))
#
# res = diff1+diff2
# print(list1)
# print(list2)
# print(res)

# StudentRecord = {"Name":[],"Age":[],"Education":[],"Gender":[]}
# StudentRecord["Name"] = ["Ali","Omer","Khan"]
# StudentRecord["Age"] = [20,14,15]
# StudentRecord["Name"] = ["Ali","Omer","Khan"]
#
# print(StudentRecord)


# names = []
# age = []
#
# StudentRecord = {"Name":names,"Age":age,"Education":[],"Gender":[]}
# userName = input("Please Enter Your Name")
# names.append(userName)
# print(StudentRecord)

"""
Variable's Scope
                1. Global Variable's Scope 
                2. Local ... Scope
                
"""
# Here Number is a Global Variable
# number = 5
# def func():
#     # Here number is Local Variable
#     global number
#     number = 10
#     return number
# # print("Number Outside of Function is: ",number)
# print("Inside Func is: ",func())
# print("Outside of Func Number",number)


# # a = 10
# def check():
#     global a
#     a = 20
#     print("Inside is: ",a)
# check()
# print("Ouside A is: ",a)



"""
Data Analysis 
Web Development with Python
HTML,CSS,BOOTSTRAP,JAVASCRIPT,PYTHON
"""

"""
map() and filter()
Built-In functions
these are use to achieve Functional Programming 

user-define and iterable object
list, tuple

def display():
lambda function
Nameless function
map(function,list)

High Order Functions
builtin 
userdefine
parameterized
without para
lambda
What is High Order Function?
Ans:
	In High Orde Functions we pass a Funcion as a Parameter to another Function.

here a and b are variables.
def sum(a,b):
	return a+b



map() filter()

"""


# def f(n):
# 	if n>3:
# 		return n
# 	# else:
# 	# 	return "Not Greater than 3"
# y = filter(f,(1,2,3,4,5,67,0))
#
# print(y)
# print(list(y))


"""
Python Functions are also High Order Function.
How we can use Parameterized Functions.
when we will pass a Function as a Parameter to any other function is called a High Order Function.

Programming Paradigm 
Functial Programming 
Procedurals Programming
OOP Programming


# By Default Python is not a OOP based Programming we can make them OOP based by using Class and Object
# Concept
By Default Python is not a Functional Programming
How we can make a Python Functional Programming. We can use map() and filter() builtin functions 

map and filter function's Syntax:
		
		1. What is function.
		2. Parameterized Function.
		3. Iterable Object. List, Tuple, Dictionary,Set in other words collect of data is called iterable objects
		4. High Order Functions.
		5. How to pass Function as a Parameter	
			
		map(function_name,iterable_Object)

"""

# def message(text):
# 	return text
#
# print(message("Hello Everyone"))






# def f(n):
# 	if n>3:
# 		return n
# 	# else:
# 	# 	return "Not Greater than 3"
# y = filter(f,(1,2,3,4,5,67,0))
#
# print(y)
# print(list(y))


# Functional Programming
# def function(number):
#     if number > 3:
#         return number
#     else:
#         return "Less than 3"
# # map(function_name,iterable_Object)
# y = map(function,(1,2,3,4,5,6,0,3,35))
# # print(y)
# print(list(y))

# Assignment
# What are Programming Paradigm In Python ?


"""

Python Functiona are also called a 
First Class Citizen Object.
In other words we can assign Function to a Variable or Return Funtion as well is called a 
"""

# Data Analysis
#
# def sum(a,b):
#     add = a+b
#     return add
#
# adder = sum
# print(adder(10,4))

























