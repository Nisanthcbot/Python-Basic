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





"""
🎉 1️⃣ Movie Night Snacks Split

Friends bought snacks separately.

Names = ["A", "B", "C", "D"]
Amounts = [500, 700, 300, 500]

Tasks:

Find average

Who paid extra?

Who needs to pay?

Print total amount to be settled

"""

Names = ["A", "B", "C", "D"]
Amounts = [500, 700, 300, 500]


average =sum(Amounts)/len(Amounts)

print(average)


for i in range(len(Amounts)):
    if Amounts[i] > average:
        print(Names[i],"You Paid Extra")
    
    elif Amounts[i]<average:
        print(Names[i],"You paid Less Amount")
    
    else:
        print(Names[i],"You no need to pay any Amount")