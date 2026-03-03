"""
SECTION A – Basics (20 Marks)
Q1 (5 Marks)

Write a function add(a, b)
Return the sum of two numbers.


"""

def add(a,b):
    return a+b


result = add(1,3)

print("Sum of Two Number :",result)



"""
Q2 (5 Marks)

Write a function is_even(n)
Return True if even, else False.


"""
def is_even(n):
    if n %2==0:
        return True
    else:
        return False
    


n = int(input('Enter the Number :'))

result = is_even(n)

print(result)



"""
Q3 (5 Marks)

Write a function square_list(n)
Print squares from 1 to n using loop inside function.

"""

n= int(input("Enter the number :"))


def square_list(n):
    for i in range(1,n+1):
        square = i*i
        print(square)


square_list(n)


Q4 (5 Marks)

What will be output?

def test(x):
    x = x + 5
    return x

num = 10
print(test(num))
print(num)


15
10