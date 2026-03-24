def add_expense(filename, amount, description):
    try:
        with open(filename, "a") as file:
            file.write(f"{amount},{description}\n")
            print(f"Added expense: ${amount} for {description}")
    except Exception as e:
        print(f"An error Occured: {e}")



def view_expense(filename):
    try:
        with open(filename, "r") as file:
            lines = file.readlines()
            total = 0
            for line in lines:
                amount, description = line.strip().split(',')
                print(f"{amount} - {description}")
                total = total + float(amount)
                print(f"The total expense {total}")
    except Exception as e:
        print(f"An error occured {e}")


def main():

    while True:
        print("\nSimple Expense Tracker")
        print("1. Add Expense")
        print("2. View Expense")
        print("3. Exit")

        choice = input("Enter Your Choice: ")

        if choice == "1":
            try: 
                amount = float(input("Enter expense amount: $"))
                description = input("Enter the expense description: ")
                add_expense("expense.txt", amount, description)
            except ValueError:
                print("Please enter a valid number for the amount.")        
        elif choice == "2":
            view_expense("expense.txt")
        
        elif choice == "3":
            print("Good Bye")
            break
        else:
            print("Invalid choice.")



if __name__ == "__main__":
    main()
