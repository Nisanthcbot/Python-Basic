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