portion_deposit = 0.2
current_savings = 0
r = 0.04
months = 0

annual_salary = float(input("Enter your annual salary: "))
semi_annual_raise = float(input("What is the semi-annual raise you expect to recieve (As a decimal): "))
portion_saved = float(input("Enter the percentage of your salary to save (As a decimal): "))
total_cost = float(input("Enter the cost of your dream home: "))


monthly_salary = (annual_salary/12)
interest = (monthly_salary*r)
deposit = (total_cost/portion_deposit)


while current_savings < deposit:
    if months != 0 and months % 6 == 0:
        current_savings += (monthly_salary) + (interest)
        current_savings += (monthly_salary) + (monthly_salary*semi_annual_raise)
        months += 1
    else:
         current_savings+=(monthly_salary) + (interest)
         months=months+1
print("Number of months: " , months)
