# Default grocery list item
grocery_list = [
    {"name": "milk", "store": "Walmart", "cost": 6.47, "amount": 2, "priority": 1, "buy": True}
]

# Global variable
TAX = 1.053

# Function to add items to your grocery list
def add_item(name, store, cost, amount, priority, buy):
    # Defined dictionary item to add to list
    item = {"name": name, "store": store, "cost": cost, "amount": amount, "priority": priority, "buy": buy}
    # Add item to grocery list
    grocery_list.append(item)

# Remove item from grocery list
def remove_item(name):
    # Use name key to identify item to remove
    index = get_index_from_name(name)
    # Remove item from the list
    grocery_list.pop()

# Get index of the grocery item
def get_index_from_name(name):
    index = 0

    # Use loop to check if item name on list
    for item in grocery_list:
        if item["name"] == name:
            return index
        else:
            index += 1

# Edit list item parameters
def edit_item(name, store=None, cost=None, amount=None, priority=None, buy="skip"):
    index = get_index_from_name(name)

    old_item = grocery_list[index]

    if not store:
        store = old_item["store"]
    if not cost:
        cost = old_item["cost"]
    if not amount:
        amount = old_item["amount"]
    if not priority:
        priority = old_item["priority"]
    if buy == "skip":
        buy = old_item["buy"]
    
    item = {"name": name, "store": store, "cost": cost, "amount": amount, "priority": priority, "buy": buy}

    grocery_list[index] = item

# Display current grocery list
def list_items():
    for item in grocery_list:
        print(item)

# Display item in a more readible format and display total
def export_items():
    buy_list = []

    for item in grocery_list:
        if item["buy"]:
            buy_list.append(item)
        if buy_list:
            for item in buy_list:
                print(f"name: {item["name"]} - store: {item["store"]} - cost: ${item["cost"]} - amount: {item["amount"]} - priority: {item["priority"]}")

                total_cost = calculate_total_cost(buy_list, round_cost=True)
                
                print(f"The total cost is ${total_cost}")

# Calculate the total of your grocery list including sales tax in Virginia
def calculate_total_cost(grocery_list, round_cost=False):
    total_cost = 0
    # Calculate cost and add to total cost
    for item in grocery_list:
        cost = item['amount'] * item['cost'] 
        total_cost += cost 
    
    # Calculate total cost and tax, the round to nearest 100th of a cent
    if round_cost:
        total_cost = round(total_cost * TAX,2)
    # total cost returned once all items in the grocery list are calculated for use in other defintions
    return total_cost

                        

