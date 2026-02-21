"""
Condition Statement na enna?

Condition statement na oru condition check pannuradhu.

👉 Oru condition true ah irundha oru block execute aagum
👉 false ah irundha vera block execute aagum

Simple ah sonna:

"Idhu nadandha idhu seiyanum, illa na adhu seiyanum"

"""

#if Syntax

if condition:
    statement


#Example

age = 18

if age >=18:
    print("Your Are eligible ")

#enna nadakudhu ingha ?

'''
age >=18 condition check pannum

greaterthan ah irudhal it till print the statement 

flase na -> nothing will happen 

'''

'''----------------------------------------------------------------------------------------------------------------------------------------------------------------------'''


#if else

if condition:
    statement

else:
    statement


#example

if age >=18:
    print("Ur Eligible")

else:
    print("Not Eligible")

#Enna Nadakdhu ingha?

'''
same as if firts condition ah check pannum age >=18 ah irudha it will excute the statement

flase -> it will excute the else statement

'''


'''----------------------------------------------------------------------------------------------------------------------------------------------------------------------'''


#if  elif else

if condition1:
    statement
elif condition2:
    statement
else:
    statement



marks = 75

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")


'''
Explanation:

First condition check pannum

True na adhu execute pannum

False na next elif check pannum

Ellam false na → else execute aagum

'''



"""
User enters:

Monthly revenue

Active users

Subscription plan (basic / pro / enterprise)

Rules:

If plan enterprise:

If revenue > 10 lakh AND users > 1000 → Enterprise Elite

Else → Enterprise Standard

If plan pro:

If revenue > 5 lakh → Pro Premium

Else → Pro Standard

If basic:

If revenue > 1 lakh → Upgrade Suggested

Else → Starter Tier

"""


monthly_revenue = int(input("Enter the monthly recvenue :"))
active_user = int(input("Enter the Active User :"))
plan =input("Selct the plan (baisc/pro/enterprise):").lower()

if plan=="enterprise":
    if monthly_revenue >1000000 and active_user >1000:
        print("Enterprice Elite")
    else:
        print("Enterprice Standard")

elif plan =="pro":
    if monthly_revenue >500000 :
        print('pro Premium')
    else:
        print("Pro Standard")

elif plan =="baisc":
    if monthly_revenue >100000 :
        print("Upgrade Suggested")
    else:
        print("Started tier")
else:
    print("Enter Currect Plan")



'''
SCENARIO 7 – Company Bonus System (Very Hard)
Problem

An employee works in a company.

Inputs:

Monthly salary

Years of experience

Rules:

If experience ≥ 5 years → Bonus = 20% salary

Else if experience ≥ 3 years → Bonus = 10% salary

Else → No bonus

Tasks:

Calculate bonus

Calculate final salary

Check if final salary ≥ ₹50,000 → Senior Employee

'''



monthly_Salary = int(input("Enter the Monthly Salary : ₹"))
Yr_Ex = int(input("Enter the Year of Experience :"))

if Yr_Ex >= 5:
    bonus = monthly_Salary *20/100

elif Yr_Ex >=3:
    bonus = monthly_Salary*10/100
    
else:
    print("No Bonus")

final_Salary = bonus + monthly_Salary
print("Bonus Amount For this Year ",bonus)
print("Final Salry : ₹",final_Salary)

if final_Salary >=50000:
       print("Senior EmployeeS")