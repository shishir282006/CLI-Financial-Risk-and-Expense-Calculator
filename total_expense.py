# Welcome to the expense calculator
 
income = int(input("Enter your monthly income"))

# write your total expense

expense ={}

while True:
    name = input("item name or (press enter to finish ) : ")
    if name == "":
        break
    price = int(input(f"price of {name} :"))
    expense[name] = price

amount = list(expense.values())

print("total expense =", "=".join(str(a) for a in amount))
print("Total expense in this month is " , sum(amount))