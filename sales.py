#4.Write an app for a phone sales man. The Salesman earns Rs10000 every month. He earns Rs1000 commission for every phone he sells. 
# If he sells more than 5 phones a month, he extra Rs100 per phone (1000+100). If he sells 10 phones or more, he gets extra Rs 200 for each phone over 5. 
# He can only earn max 25000 per month. Calculate his monthly salary and avg salary per month in one year. 

monthly_base_salary = 10000
commission_per_phone = 1000
phone_sales = 0
month = 0

for phone_sales in range(1,13):
    month += 1
    phone_sales = float(input("Enter the phone sales per month: "))
    print("Month: ", month, phone_sales)

monthly_salary = monthly_base_salary + (commission_per_phone * phone_sales)
avg_salary = (monthly_base_salary + (commission_per_phone * phone_sales) * 12)

if phone_sales > 5:
    print(monthly_base_salary + commission_per_phone + (phone_sales * 100))
elif phone_sales > 10:
    print(monthly_base_salary + commission_per_phone + (phone_sales * 200))
else:
    print("Salary not Credited")

print("Monthly Salary: ", monthly_salary)
print("Average Salary Per Month in One year: ", avg_salary)