# expense tracker
Total_income = int(input("Enter your monthly income : "))
print("Your Total Income is : ", Total_income)

saving = Total_income * 0.20
print("For saving : ", saving)

rest_amount = Total_income - saving
print("after saving your left_amont is ", rest_amount)

weekly_expense_target = rest_amount / 4 
print("for weekly expense (spend money in limit) ", weekly_expense_target)
