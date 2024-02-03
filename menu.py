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
        choice = input("***************\n1. Add new record\n2. Delete a record\n3. View all records\n4. Exit\nEnter here: ")
        match choice:
            case "1":
                add_new_record()
            case "2":
                delete_record()
            case "3":
                view_all_records()
            case "4":
                print("You chose to exit, goodbye!")
                cont = False
                break
            case _:
                print("That was an invalid input. Please enter 1, 2, 3, or 4.")

def add_new_record():
    title = input("\nTitle of the transaction: Enter a short description\n")
    gained = input("Was this transaction a profit?: Y/N\n")
    if (gained == 'Y'):
        profit = True
    else:
        profit = False

    amount = input("Enter the amount of the transaction: Enter a decimal number\n")
    new_record = Transaction(title, profit, amount)
    all_records.append(new_record)
    print(f'Successfull added a new transaction of {amount}.\n')

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

menu()
