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
high, low = 10000, 0
guess=round((high+low)/2,2)
steps=0


while abs(current_savings <= down_payment + epsilon) and abs(current_savings >= down_payment - epsilon): 
       for i in range(1, months_to_save+1): 
           current_savings += monthly_salary 
           current_savings += interest/12
           months +=1 
           if months % 6==0:
               current_savings += * semi_annual_return 
               months +=1 
       if current_savings < down_payment + epsilon or current_savings < down_payment - epsilon: 
           print("It is not possible for you to afford the deposit within the time period") 
           break 
       current_savings =0 
       months =0 
       for i in range(1,months_to_save+1):
           current_savings += monthly_salary * guess
           current_savings += * interest/12
           months+=1
           if months % 6==0:
               current_savings += * semi_annual_return
       if   current_savings < down_payment:
           low = guess
       else:
           high = guess
           guess = guess/10000
           steps +=1
           print("Best savings rate: ", round(guess,2))
           print("Steps in bisection: ", steps) 