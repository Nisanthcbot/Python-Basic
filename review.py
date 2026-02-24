'''
Q9 (6 Marks)

Print numbers from 1 to 100.

But:

If number divisible by 3 → print "Fizz"

If divisible by 5 → print "Buzz"

If divisible by both → print "FizzBuzz"

Otherwise print the number

(⚠ Order of conditions very important)

'''

for i in range(1,101):

    if i % 3==0 and i % 5 ==0:
        print("FizzBuzz")
        
    elif i % 3 ==0:
        print("Fizz")

    elif i % 3==0:
        print("Buzz")
        
    else:
        print(i)

"""
Q11 (6 Marks)

Take a number from user.

Print multiplication table of that number up to 10.

Example:
Input: 5
Output:
5 x 1 = 5
5 x 2 = 10
...
5 x 10 = 50

"""


num =int(input('Enter the number :'))


for i in range(1 ,11):
    print(f"{num}X{i} =",num*i)



"""
Q12 (6 Marks)

Take number n from user.

Count:

How many even numbers from 1 to n

How many odd numbers from 1 to n

Print both counts.

"""


num =int(input('Enter the number :'))

odd_count =0
even_count =0
for i in range(1 ,num+1):
    if i % 2==0:
        even_count+=1

    else:
        odd_count +=1

total_count = odd_count + even_count
print(f" odd count is :{odd_count} and  Even Count is {even_count} and total count is {total_count}")





