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



