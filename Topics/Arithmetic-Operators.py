# arithmetic operators
"""
+ - addition
- - subtraction
* - multiplication      
/ - division
% - modulus (remainder)
// - floor division (quotient without the remainder)
** - exponentiation (power)     

Cleaned Professional Version (Concept Only)
What you learned here:
+ - * / → Arithmetic operators
% → Remainder
// → Floor division
** → Power
Always check division by zero
Print correct variables
"""

#task 1
"""
Take two numbers from the user and:
Add
Subtract
Multiply
Divide
"""

num1 = int(input("Enter the First number: "))
num2 = int(input("Enter 2nd number : "))

add  = num1 + num2
sub = num1 - num2
mul = num1 * num2
div = num1 / num2

print("Addition of num1 and num2 :",add)
print("Subtraction of num1 and num2 :",sub)
print("multiplication of num1 and num2 :",mul)
print("division of num1 and num2 :",div)



#Task 2

"""
Given a number:

Find square

Find cube

Find remainder when divided by 5

"""


sq = int(input("Enter the number :"))
power = sq**2
cub = sq**3
rem = sq%5

print(f"Square Root of {sq} is {power}")
print(f"Cube Root of {sq} is {cub}")
print(f"Remainder when divided by 5 {rem}")



#task 3

"""

Ask the user for total marks and number of subjects.
Calculate:

Average

Floor average (//)

"""
total_mark = int(input("Enter the total mark :"))

total_sub = int(input("Enter the total Subject :"))

average = float(total_mark / total_sub)
floor_average = int(average)


print("Average:",average)
print("Floor Average:",floor_average)



#task 4

