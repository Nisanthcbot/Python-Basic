"""
Find Second Largest Number

numbers = [10,25,8,40,15]

Output

Second Largest : 25

Rules

No sort()
No max()

We’ll build the loop logic together.
"""

numbers = [10,25,8,40,15]

Second_list=[]

num = numbers[0]


for i in numbers:
    if i > num:
        num = i
print(num)


