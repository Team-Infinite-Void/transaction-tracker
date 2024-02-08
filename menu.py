from datetime import datetime
all_records = []

class Transaction:
    def __init__(self, title, if_profit, amount):
        self.title = title
        self.if_profit = if_profit
        self.amount = amount
        self.time = datetime.now()  # Automatically set the time to the current datetime

    def get_title(self):
        return self.title

    def get_profit(self):
        return self.if_profit

    def get_amount(self):
        return self.amount

    def get_time(self):
        return self.time.strftime('%Y-%m-%d %H:%M:%S')  # Return the time as a string in a readable format

    def __str__(self) -> str:
        return f'Title: {self.title}, Amount: {self.amount}, Time: {self.get_time()}'


def menu():
    cont = True

    while cont:
        choice = input("***************\n1. Add new record\n2. Delete a record\n3. View all records\n4. View Analytics\n5. Exit\nEnter here: ")
        match choice:
            case "1":
                add_new_record()
            case "2":
                delete_record()
            case "3":
                view_all_records()
            case "4":
                view_analytics()
            case "5":
                print("You chose to exit, goodbye!")
                cont = False
                break
            case _:
                print("That was an invalid input. Please enter 1, 2, 3, 4, or 5.")


def add_new_record():
    title = input("\nTitle of the transaction: Enter a short description\n")
    gained = input("Was this transaction a profit? (Y/N)\n")
    profit = gained.upper() == 'Y'

    # Attempt to convert the amount input to a float with error handling
    while True:
        amount_input = input("Enter the amount of the transaction: Enter a decimal number\n")
        try:
            amount = float(amount_input)
            break  # Exit the loop if the conversion is successful
        except ValueError:
            print("Invalid amount. Please enter a valid decimal number.")

    new_record = Transaction(title, profit, amount)
    all_records.append(new_record)
    print(f'Successfully added a new transaction of {amount}.\n')

def delete_record():
    if (len(all_records) == 0):
        print("No records in the database. Create a new record by selecting '1' in the main menu.\n")
        return
    print("***************\nAll records to date:\n")
    for record in all_records:
            print(f'{all_records.index(record) + 1}. {record}\n')
    num_to_delete = input("Which record would you like to delete? Please enter one number: ")
    to_delete = all_records[int(num_to_delete) - 1]
    all_records.remove(to_delete)
    print(f'Successfull deleted the transaction of {to_delete.get_title()}.\n')


def view_all_records():
    if (len(all_records) == 0):
        print("No records in the database. Create a new record by selecting '1' in the main menu.\n")
    else:
        print("***************\nAll records to date:\n")
        for record in all_records:
            print(f'{all_records.index(record) + 1}. {record}\n')

def view_analytics():
    total_profit = sum(record.amount for record in all_records if record.if_profit)
    total_loss = sum(record.amount for record in all_records if not record.if_profit)
    net_balance = total_profit - total_loss

    print(f"***************\nAnalytics Summary:\n")
    print(f"Total Transactions: {len(all_records)}")
    print(f"Total Profit: {total_profit}")
    print(f"Total Loss: {total_loss}")
    print(f"Net Balance: {net_balance}\n")


menu()
