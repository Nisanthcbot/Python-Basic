age=int(input("Enter The Age :"))
studentORno =input("Are You an Student yes or No :")
student = studentORno.upper()
amount = 150


if age >65 or student == 'YES' :
    discount = amount * 10/100
    amount -= discount
    print(amount)