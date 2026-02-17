'''
Q1. User Subscription Access System

A SaaS platform offers plans:

Plan	Price	Access
Free	₹0	Limited
Basic	₹999	Standard
Pro	₹1999	Full

Rules:

If user selects Pro and payment ≥ ₹1999 → Full access

If payment < plan price → Access denied

Tasks:

Validate payment

Assign access level

Print subscription status

'''

Plan = input("Select the paln (Free / Basic / Pro)").lower()
payment = int(input("Enter the Amount To paid :₹"))

if Plan == "pro" and payment >=1999:
    print("Successfull Now u will get all access")

else:
    print("Access denied")
    

