"""
(10 Marks) – Prime Number Check

Take a number from user.

Check whether it is a Prime number or Not.

Rules:

Prime number is divisible only by 1 and itself.

If number <= 1 → Not Prime

Example:
7 → Prime
8 → Not Prime

"""

names = ["karthi", "nava", "akash", "partha"]
amounts = [3000, 2100, 4000, 6000]



average = sum(amounts)/len(amounts)


print("Average Expencess :",average)


for i in range(len(amounts)):
    if amounts[i] == average:
        print(names[i],"no need to give Money")
    
    elif amounts[i]>average:
        print(names[i],":U Spend Extra Amount:",amounts[i]-average)
    

    else:
         print(names[i]," :U Need to Pay:",average-amounts[i])

