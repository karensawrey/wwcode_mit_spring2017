
"""
@author: Karen
"""

yearly_salary = float(input("Enter your starting (annual) salary: " ))
total_cost = 1000000
portion_down_payment = total_cost * 0.25
semi_annual_rise = 7 #7%
monthly_salary = yearly_salary / 12
addition_to_salary = (monthly_salary/100)*semi_annual_rise
time_frame = 36 #months
optimal_savings_portion = portion_down_payment/time_frame
optimal_savings_portion = int(optimal_savings_portion * 100) / 100
print(("Optimal $ amount of monthly savings for this house would be $"), optimal_savings_portion)
remainder_after_saving = monthly_salary - optimal_savings_portion
if remainder_after_saving < 6945:
    print("Sorry, forget about this house - it's too expensive and you can't afford it.")
if remainder_after_saving >= 6946 and remainder_after_saving <= 10000:
    print("You could try to save, but you'll starve. Look for a cheaper house.")
if remainder_after_saving >= 10001:
    print("Well, looks like you can afford an accomodation!")
    print("Start saving and in 36 months you'll be able to make that down payment.")