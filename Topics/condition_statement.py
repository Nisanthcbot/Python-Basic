"""
Condition Statement na enna?

Condition statement na oru condition check pannuradhu.

👉 Oru condition true ah irundha oru block execute aagum
👉 false ah irundha vera block execute aagum

Simple ah sonna:

"Idhu nadandha idhu seiyanum, illa na adhu seiyanum"

"""

#if Syntax

if condition:
    statement


#Example

age = 18

if age >=18:
    print("Your Are eligible ")

#enna nadakudhu ingha ?

'''
age >=18 condition check pannum

greaterthan ah irudhal it till print the statement 

flase na -> nothing will happen 

'''

'''----------------------------------------------------------------------------------------------------------------------------------------------------------------------'''


#if else

if condition:
    statement

else:
    statement


#example

if age >=18:
    print("Ur Eligible")

else:
    print("Not Eligible")

#Enna Nadakdhu ingha?

'''
same as if firts condition ah check pannum age >=18 ah irudha it will excute the statement

flase -> it will excute the else statement

'''


'''----------------------------------------------------------------------------------------------------------------------------------------------------------------------'''


#if  elif else

if condition1:
    statement
elif condition2:
    statement
else:
    statement



marks = 75

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")


'''
Explanation:

First condition check pannum

True na adhu execute pannum

False na next elif check pannum

Ellam false na → else execute aagum

'''