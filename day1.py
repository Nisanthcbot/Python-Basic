# Variable And DataType 

"""
Docstring for day1

1. Variable
2. Datatype
3. Variable Scope
4. Type Casting & Checking

"""
# Variable 

'''
  is an container to store the value 
'''


#DataType

'''
  1.int() number eg no = 12
  2.float() floating number Eg number = 12.22
  3.string() String eg Name = "nisanth'
  4. boolean() true or Flase
  5. None() nil value x

'''

name = "nisanth"
age = 22
city = "Annur"

print("My name Is :",name)
print("My Age Is :",age)
print("My Palce Is :",city)



Student_Name = "Nisanth"
english = 75
tamil = 56
math = 87


def total():
    total = english+tamil+math
    return total


def average():
    average  = total()/3
    return average

def grade(avg):
    
    if avg >=95:
        grade ="A"
    
    elif avg <=85:
        grade ="B"
    
    elif avg <=75:
        grade ="c"
    
    elif avg <=65:
        grade ="D"
    
    elif avg <=50:
        grade ="E"
    
    else :
        grade="Try Next Time"

print("Total Mark is :",total())
print("Average Mark is :",average())

grade()

