portion_deposit = 0.2
current_savings = 0
r = 0.04
months = 0

annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percentage of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))

monthly_salary = (annual_salary/12)
interest = (current_savings*r/12)
deposit = (total_cost/portion_deposit)


while current_savings < deposit:
    current_savings+=(monthly_salary+interest)
    months=months+1
print("Number of months: " , months)