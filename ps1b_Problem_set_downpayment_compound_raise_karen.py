
"""
@author: Karen
"""

yearly_salary = float(input("Please enter your annual salary: " ))
monthly_savings = float (input ("Portion of your salary you\'re willing to set aside each month in %: "))
total_cost = float (input("The rieltor said the house costs how much?!"))
semi_annual_rise = float (input("Please enter your rise in %: "))
number_of_months = 0
monthly_salary = yearly_salary / 12
addition_to_salary = (monthly_salary/100)*semi_annual_rise
# FV = PV(1+k)**n
savings = monthly_salary * monthly_savings /100
portion_down_payment = total_cost * 0.25
current_savings = 0
count = 0
time_frame = 6


while current_savings <= portion_down_payment:
    current_savings = savings + current_savings + (current_savings * 0.04) /12
    number_of_months = number_of_months + 1
    count += 1
    if count == time_frame:
        count = 0
        monthly_salary += addition_to_salary
        addition_to_salary = (monthly_salary/100)*semi_annual_rise
        #code health checkup
        #print(monthly_salary)
        #print(current_savings)
        #print(portion_down_payment)
        
print("Number of months you'll have to wait:")         
print(number_of_months)
