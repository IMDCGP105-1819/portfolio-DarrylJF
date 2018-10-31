import bisect

print("Enter the starting salary: ")
annual_salary = float(input())

semi_annual_return=0.07
r=0.04
total_cost=1000000
down_payment=(total_cost*0.25)
current_savings=0
months=0
months_to_save=36
monthly_salary = annual_salary/12
interest = annual_salary*r



epsilon=100
high, low = 1, 0
guess=(high+low) / 2
steps=0

# loop check to see if calculation is possible within the time period
while current_savings <= down_payment + epsilon and current_savings >= down_payment - epsilon: # uses epsilon to check leeway either side
       for i in range(1, months_to_save+1): # makes sure it makes calculations based on 36 months and doesnt go over
           current_savings += monthly_salary # adds monthly salary to current savings
           current_savings += interest/12 # add interest to current savings (I presumed because interest is based annually to divide it by 12? or add another modulus in the to add every 12(months)?)
           months +=1 # increments months by 1
           if months % 6==0: # modulus condition runs every 6
               current_savings += * semi_annual_return # adds semi annual return to current savings
               months +=1 # increments months by 1
       if current_savings < down_payment + epsilon or current_savings < down_payment - epsilon: # checks if current savings is now equal to cost of down payment including leeway either side
           print("It is not possible for you to afford the deposit within the time period") # print statement if condition is true
           break # programs stops if condition is true
       current_savings =0 # reset value for bisection search
       months =0 # reset value for bisetion search
       for i in range(1,months_to_save+1):
           current_savings += monthly_salary * guess
           current_savings += * interest/12
           months+=1
           if months % 6==0:
               current_savings += * semi_annual_return
               
             



