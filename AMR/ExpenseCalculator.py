name = input("Enter Your Name: ")
salary = float(input("Enter Your Salary: "))

print("\nExpense Calculator:- \n")

grocery_bill = float(input("Enter Your Grocery Bill: "))
electric_bill = float(input("Enter Your Electric Bill: "))
gas_bill = float(input("Enter Your Gas Bill: "))
internet_bill = float(input("Enter Your Internet Bill: "))
water_bill = float(input("Enter Your Water Bill: "))
sweeper_bill = float(input("Enter Your Sweeper Bill: "))
superCard = float(input("Enter Your Super Card: "))
transport = float(input("Enter Your Transport: "))
own_house = input("Do You Live In Your Own House? ")


if own_house.lower() == "no":
    rent = float(input("Enter Your Rent: "))
else:
    rent = 0




is_married = input("Are You Married? ")

if is_married.lower() == "yes":
    child = int(input("How Many Children Do You Have? "))
    if child > 0:
        child_expense = float(input("Enter Your Child Expenses: "))
    else:
        child_expense = 0


total_expenses = grocery_bill + electric_bill + gas_bill + internet_bill + water_bill + sweeper_bill + superCard + transport + rent + child_expense
total_savings = salary - total_expenses

if salary > total_expenses:
    print(f"{name} -> Your Savings Are: {total_savings} \nYou Should Take Savings Plans Kindly Visit Your Nearest Meezan Bank!")
elif salary == total_expenses:
    print(f"{name} -> Please You Should Take Major Steps To Increase Your Income So Please Contact Dholu Bholu!")
else:
    print(f"{name} -> Please look After Your Expenses!")
print(f"Your Total Expense Is: {total_expenses} \nYour Total Savings Is: {total_savings}")