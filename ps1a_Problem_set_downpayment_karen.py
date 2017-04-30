"""
@author: Karen
"""

yearly_salary = float (input("Please enter your annual salary: " ))
monthly_savings = float (input ("Portion of your salary you\'re willing to set aside each month in %: "))
total_cost = float (input("The rieltor said the house costs how much?! "))
number_of_months = 0
monthly_salary = yearly_salary / 12
savings = monthly_salary * monthly_savings /100
portion_down_payment = total_cost * 0.25
current_savings = 0

while current_savings <= portion_down_payment:
    current_savings = savings + current_savings + (current_savings * 0.04) /12
    number_of_months = number_of_months + 1

print("Number of months you'll have to wait:")    
print(number_of_months)