all_records = []
class Transaction:
    def __init__(self, title, if_profit, amount):
        self.title = title
        self.if_profit = if_profit
        self.amount = amount

    def get_title(self):
        return self.title

    def get_profit(self):
        return self.if_profit

    def get_amount(self):
        return self.amount

    def __str__(self) -> str:
        return f'Title: {self.title}\nAmount: {self.amount}'

def menu():
    cont = True

    while (cont):
        choice = input("1. Add new record\n2. View all records\n3. Exit\nEnter here: ")
        match choice:
            case "1":
                add_new_record()
            case "2":
                view_all_records()
            case "3":
                print("You chose to exit, goodbye!")
                cont = False
                break
            case _:
                print("That was an invalid input. Please enter 1, 2, or 3.")

def add_new_record():
    title = input("Title of the transaction: Enter a short description\n")
    gained = input("Was this transaction a profit?: Y/N\n")
    if (gained == 'Y'):
        profit = True
    else:
        profit = False

    amount = input("Enter the amount of the transaction: Enter a decimal number\n")
    new_record = Transaction(title, profit, amount)
    all_records.append(new_record)
    print(f'Successfull added a new transaction of {amount}.\n')

def view_all_records():
    if (len(all_records) == 0):
        print("No records in the database. Create a new record by selecting '1' in the main menu.\n")
    else:
        print("All records to date:\n")
        for record in all_records:
            print(f'{record}\n')

menu()
