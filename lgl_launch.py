import lgl_core

print("Welcome to to Brand New LGL Grocery App")
def launch():
    while True:
        command = input("Enter a command (add, remove, edit, list, export, quit): ")

        if command == "add":
            print("Here's where you add items to your grocery list.")
            name, store, cost, amount, priority, buy = get_inputs()
            lgl_core.add_item(name=name, store=store, cost=cost, amount=amount, priority=priority, buy=buy)

        if command == "remove":
            name = input("Enter the item's name to remove from your list: ")

            lgl_core.remove_item(name)

        if command == "edit":
            name, store, cost, amount, priority, buy = get_inputs()

            lgl_core.edit_item(name, store, cost, amount, priority, buy)

        if command == "list":
            lgl_core.list_items()

        if command == "export":
            lgl_core.export_items()

        if command == "quit":
            break

def get_inputs():
    while True:
        name = input("Enter the item's name to edit (ex. milk): ") 
        if name:
            break
        print("Invalid input. Please enter a valid item")

    while True:
        store = input("What's the name of the store: ")
        if store == "skip":
            store = None
            break
        elif store:
            store = store
            break
        print("Invalid input. Please add a valid store name")

    while True:
        try:
            cost = input("Enter the price of the item (ex. 1.95): ")
            if cost == "skip":
                cost = None
                break
            else:
                cost = float(cost)
                break
        except ValueError:
            print("Invalid input. Please enter a valid price")

    while True:
        try:
            amount = input("How many of the item are you getting: ")
            if amount == "skip":
                amount = None
                break
            elif int(amount) > 0:
                amount = int(amount)
                break
            else:
                print("Quantity must be a positive number")
        except ValueError:
            print("Invalid input. Please enter a valid quantity")

    while True:
        try:
            priority = input("What is the item's priority (i.e. 1 the highest and 5 the lowest): ")
            if priority == "skip":
                priority = None
                break
            elif 1 <= int(priority) <= 5:
                break
            else:
                print("Priority must be between 1 and 5")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 5")

    while True:
        try:
            buy = input("Confirm you intend to buy the item (true or false): ")
            if buy.lower() =="true":
                buy = True
                break
            elif buy.lower() == "false":
                buy = False
                break
            elif buy == "skip":
                buy = "skip"
                break
            else:
                print("Invalid input. Please enter true or false")
        except ValueError:
            print("Invalid input. Please enter 'true' or 'false'")

    return name, store, cost, amount, priority, buy

if __name__ == '__main__':
    launch()