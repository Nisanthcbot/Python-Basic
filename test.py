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












