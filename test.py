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
stock_quantity = int(input("Enter the Stock Quantity :"))
user_membership = input("Select You are (Normal / Premium) Membership :").lower()
payment_amount=int(input("Enter the Payment Amount : ₹"))

cashback = product_price *10/100

if stock_quantity >0:
    if payment_amount < product_price:
        print("Payment Failed")
        
    elif payment_amount > product_price:
        refund_amount = payment_amount - product_price
        print("Refund Amount :₹",refund_amount)
    
    elif product_price == payment_amount and user_membership =="premium":
        print("You get 10% Cashback and the Amount is :₹",cashback)
        print("Order Has been Plased Successfully")

    elif product_price == payment_amount:
         print("Order has been Successfully Placed")

else:
       print("Out of Stock")
    












