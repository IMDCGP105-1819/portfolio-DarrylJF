portion_deposit = 0.2
current_savings = 0
r = 0.04
months = 0

annual_salary = float(input("Enter your annual salary: "))
semi_annual_raise = float(input("What is the semi-annual raise you expect to recieve (As a decimal): "))
portion_saved = float(input("Enter the percentage of your salary to save (As a decimal): "))
total_cost = float(input("Enter the cost of your dream home: "))


monthly_salary = (annual_salary/12)
interest = (current_savings*r/12)
deposit = (total_cost/portion_deposit)
semi_annual_raise = (semi_annual_raise*2)


while current_savings < deposit:
    current_savings+=(monthly_salary+interest)
    current_savings+=(monthly_salary+interest+semi_annual_raise)
    months=months+1
print("Number of months: " , months)