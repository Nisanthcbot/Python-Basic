"""
E-Commerce Order Validation System

User enters:

Product price

Stock quantity

User membership (normal / premium)

Payment amount

Rules:

If stock is 0 → "Out of Stock"

If payment < product price → "Payment Failed"

If membership is premium AND payment correct → Apply 10% cashback

If payment > product price → Show refund amount

Otherwise → "Order Placed Successfully"

Only one final outcome should print.

"""


product_price = int(input("Enter the product Amount :₹"))
stock_quantity = 10 
user_membership = input("Select You are (Normal / Premium) Membership :").lower()
payment_amount=int(input("Enter the paument Amount : ₹"))

cashback = product_price *10/100

if stock_quantity >0:
    if user_membership =="premium" and payment_amount == product_price :
        print(f"{product_price} You Have get 10% off{cashback}")
    
    elif payment_amount == product_price:
        print(f"{product_price}")
    
    else:
        print("payment Faild")



