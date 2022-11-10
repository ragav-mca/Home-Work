"""
Write a program to calculate the milege. Ask the user how many litres of petrol they have. 
Ask how many km they have to drive. Calcualte the milege. If the mileage is more than 30km per litre, tell 
the user they have to fill the tank again.
"""

petrol_stock = int(input("Enter the quantity of petrol you have: "))
travel_distance = int(input("Enter the total distance in km: "))
mileage = (travel_distance // petrol_stock)

print (petrol_stock )
print (travel_distance)
print (mileage)

if (mileage > 30):
    print("Fill the Petrol Tank")
else:
    print("No need to Fill the tank")