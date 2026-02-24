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
Print first 10 odd numbers using only range.

"""

