#Loop Concept


"""
loop na enna ?


same work an repeated panna use panradhutha loop

Ex:

if u have 50 student mark list 
and u wants to print those mark 

without loop we will print 

print(mark1)
print(mark2)
print(mark3)
........
.......
....
....

impossible right ?


with Loop

we can repeat the process one by one 


"""



#Type of Loop:

'''

1.For Loop
2.While Loop

'''

for i in range(5):
    print(i)


"""
for -> its is an loop

i -> Varibale name

in -> is an keyword

range() -> is an class

"""



"""
Print numbers from 1 to 20
But print only numbers divisible by 3.

Expected output:
3 6 9 12 15 18

"""

for i in range(1,20):
    if i %3 ==0:
        print(i)



number = 5

for i in range(1,11):
    print(number*i)



#while loop


"""
it will run till condition is currect 

"""



"""
1️⃣ Print Reverse Numbers

Print numbers from 10 to 1 using for loop.

"""


for i in range(10,0,-1):
    print(i)




"""
Print all even numbers from 1 to 50.
Also print how many even numbers are there.

"""


for i in range(1,50):
    if i % 2== 0:
        print(i)