"""
User enters:

Number of students

Then loop should:

Ask marks for each student

After collecting all marks, program should print:

1️⃣ Total marks
2️⃣ Average marks
3️⃣ Highest mark
4️⃣ Lowest mark

"""

student_count = int(input("Enter the Student Count :"))
total = 0
for i in range(1,student_count+1):
    mark = int(input(f"Enter the mark{i} :"))
    total = total + mark
    average = total / i
    
print("Total mark is :",total)
print("Average Mark is :",average)


