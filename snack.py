#Write an app to calculate the total bill at the Snack bar. The price of coffee is Rs 100, Vadai (1) is Rs100,
#Sandwich is Rs 200, Coke Rs 60. If the customer buys more than one sandwich or more than two vadai, the price of coffee is Rs 50. 
#If the customer buys one of each item, then there is discount of 20% of the total. No further discounts after the 20% discount.
#If the total price of the bill is more than Rs1000, then also there is a 20% discount.  

#Inputs of the given program
coffee_price = 100
vadai_price = 100
sandwich_price = 200
coke_price = 60
offer_coffee_price = 50
total = 0
discount = 0
other_discount_applied = 0
coffee = int(input("Enter the no of Coffee: "))
vadai = int(input("Enter the no of  Vadai: "))
sandwich = int(input("Enter the no of Sandwich: "))
coke = int(input("Enter the no of Coke: "))

#condition for sandwich greater than one or vadai greater than two
if (sandwich > 1 or vadai > 2):
    total+=(offer_coffee_price*coffee + vadai_price*vadai + sandwich_price*sandwich + coke_price*coke)
#condition for if customer buys one of each item
elif (coffee==1 + vadai==1 + sandwich==1 + coke==1):
    total+=(coffee_price*coffee + vadai_price*vadai + sandwich_price*sandwich + coke_price*coke)
    other_discount_applied += True
total=(total-(total/10)*2)
print("total",total)
#condition if total price of the bill is more than Rs1000
if(total>1000 and (not other_discount_applied)):
    total=(total-(total/10)*2)
    print("total",total)
else:
    print("total",discount) 
