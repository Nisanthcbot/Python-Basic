"""
TYPE 1 – Normal Increment (Forward Loop)
Q1

Print numbers from 1 to 10.

Q2

Print numbers from 5 to 20.

Q3

Print numbers from 1 to 50 with step 3

"""
#Print numbers from 1 to 10.


for i in range(1,10):
    print(i)



#Print numbers from 5 to 20.


for i in range(5,20):
    print(i)


#Print numbers from 1 to 50 with step 3


for i in range(1,50,3):
    print(i)

"""
TYPE 2 – Reverse (Decrement Style)
Q4

Print numbers from 10 to 1.

Q5

Print numbers from 100 to 50.

Q6

Print numbers from 20 to 0 decreasing by 2.

"""


#Print numbers from 10 to 1.

for i in range(10,0,-1):
    print(i)



#Print numbers from 100 to 50.


for i in range(100,50,-1):
    print(i)

#Print numbers from 20 to 0 decreasing by 2.

for i in range(20,0,-2):
    print(i)



"""
Q7

Using while loop, print numbers from 1 to 10
Increase counter manually inside loop.

"""
i=0

while i<=10 :
    print(i)
    i+=1

"""
🔵 TYPE 4 – Manual Decrement (Simulating i--)
Q8

Using while loop, print numbers from 10 to 1
Decrease counter manually.

"""

i=10
while i>=1:
    print(i)
    i-=1

"""
TYPE 6 – Advanced Increment Logic
Q11

Print first 10 even numbers using only range step (no if condition).

"""

for i in range(0,21,2):
    print(i)




"""
Python Mini Project Questions (Week 3)
1️⃣ Student Report Card Generator

Problem Statement

Create a Python program that generates a student report card.

Requirements:

Take input from the user:

Student ID

Student Name

Marks for each subject (for example: Math, Science, English)

Store the marks in a dictionary.

Calculate:

Total marks

Average marks

Assign grade based on average:

90+  → Grade A
75–89 → Grade B
50–74 → Grade C
Below 50 → Fail

Print a formatted report card like this:

-----------------------------
Student ID : 101
Name       : Ravi

Math       : 85
Science    : 90
English    : 78

Total      : 253
Average    : 84.33
Grade      : B
-----------------------------
"""

student_id = input("Enter the Student ID :")
student_name = input("Enter the Student Name :")  
subject_count = int(input("Enter the Total Subject :"))

subject = {}
total =0
average = 0

for i in range(subject_count):
    subject_name = input("Enter the Subject Name :")
    subject_mark = int(input("Enter the Mark :"))
    subject[subject_name]=subject_mark
    total = total + subject_mark
    average = total / subject_count
    

print(total)

def grade():
    if average >=90:
        return "Grade A"
    elif average >=75:
        return "Grade B"
    elif average >=50:
        return "Grade c"
    else:
        return "Fail"


print("----------------------------------------------------------")
print("Student ID :",student_id)
print("Name :",student_name)
print()
for sub,mark in subject.items():
    print(sub,":",mark)
print()
print("Total :",total)
print("Average :",average)
print("Garde :",grade())
print("----------------------------------------------------------")


"""
1️⃣ List Logic (Easy)

You are given a list of numbers.

numbers = [10, 25, 8, 40, 15]

Tasks

Print the largest number

Print the smallest number

Print the sum of all numbers

Print numbers greater than 20

Example Output

Largest : 40
Smallest : 8
Sum : 98
Greater than 20 : 25 40
"""


numbers = [10, 25, 8, 40, 15]

largerst_num = numbers[0]
smallest_num = numbers[0]

greaterthan =[]


for i in numbers:
    if i > largerst_num:
        largerst_num = i
    
    if i < smallest_num:
        smallest_num = i
    
    if i >20:
        greaterthan.append(i)


print("Largest :",largerst_num)
print("Smallest :",smallest_num)

print("Sum :",sum(numbers))

print(greaterthan)

        
"""
String Logic

Take a string from user.

Example

Input : "python"

Tasks

Count total characters

Count vowels

Count consonants

Output Example

Characters : 6
Vowels : 1
Consonants : 5
"""

User_input = input("Enter the input :")
total_lenth = len(User_input)
vowels ="AEIOUaeiou"
vowels_count = 0


for i in User_input:
    if i in vowels:
        vowels_count  = vowels_count +1
    
    else:
        consonants = total_lenth - vowels_count


print("Characters :",total_lenth)
print("Vowels :",vowels_count)
print("Consonants :",consonants)