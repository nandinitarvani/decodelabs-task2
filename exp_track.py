total = 0
count = 0
expenses = []
while True:
    try:
        expense = float(input("Enter the amount :  "))    
        if expense == 0:
                break
        expenses.append(expense)
        print("Expense added !!!")
        total += expense
        count += 1

    except ValueError:
        print("Invalid input. Please enter a valid number:")

if count > 0:
    average = total / count
    print("\n================================")
    print(f"\n--> Total expenses : {total}")
    print(f"\n--> Number of expenses: {count}")
    print(f"\n--> Average expense: {average}")
    print(f"\n--> Highest expense: {max(expenses)}")
    print(f"\n--> Lowest expense: {min(expenses)}")
else:
    print("No expenses entered.")
print("\n-->Expenses entered:")
for i, expense in enumerate(expenses, start=1):
    print(f"   {i}. {expense}")


    