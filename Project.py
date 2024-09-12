# Define the inventory list
inventory = []

# Function to add an item to the inventory
def add_item():
    name = input("Enter item name: ")
    price = float(input("Enter item price: "))
    quantity = int(input("Enter item quantity: "))
    category = input("Enter item category: ")

    # Create a new item as a dictionary
    item = {
        "name": name,
        "price": price,
        "quantity": quantity,
        "category": category
    }
    # Add the item to the inventory
    inventory.append(item)
    print(f'Item "{name}" added successfully!')

# Function to update an item in the inventory
def update_item():
    name = input("Enter the name of the item to update: ")
    
    # Search for the item by name
    for item in inventory:
        if item['name'].lower() == name.lower():
            print(f'Updating item "{name}"...')
            item['price'] = float(input("Enter new price: "))
            item['quantity'] = int(input("Enter new quantity: "))
            item['category'] = input("Enter new category: ")
            print(f'Item "{name}" updated successfully!')
            return
    
    print(f'Item "{name}" not found in inventory.')

# Function to view the inventory
def view_inventory():
    if not inventory:
        print("Inventory is empty.")
        return

    print("\nInventory:")
    for item in inventory:
        print(f"Name: {item['name']}, Price: {item['price']}, Quantity: {item['quantity']}, Category: {item['category']}")
    print()

# Function to remove an item from the inventory
def remove_item():
    name = input("Enter the name of the item to remove: ")
    
    # Search for the item by name and remove it
    for item in inventory:
        if item['name'].lower() == name.lower():
            inventory.remove(item)
            print(f'Item "{name}" removed successfully!')
            return
    
    print(f'Item "{name}" not found in inventory.')

# Function to search items by category
def search_by_category():
    category = input("Enter the category to search for: ")
    
    found_items = [item for item in inventory if item['category'].lower() == category.lower()]
    
    if found_items:
        print(f'\nItems in category "{category}":')
        for item in found_items:
            print(f"Name: {item['name']}, Price: {item['price']}, Quantity: {item['quantity']}")
        print()
    else:
        print(f'No items found in category "{category}".')

# Main loop to interact with the user
def main():
    while True:
        print("\nInventory Management System")
        print("1. Add Item")
        print("2. Update Item")
        print("3. View Inventory")
        print("4. Remove Item")
        print("5. Search by Category")
        print("6. Exit")
        
        choice = input("Choose an option: ")

        if choice == "1":
            add_item()
        elif choice == "2":
            update_item()
        elif choice == "3":
            view_inventory()
        elif choice == "4":
            remove_item()
        elif choice == "5":
            search_by_category()
        elif choice == "6":
            print("Exiting the system.")
            break
        else:
            print("Invalid option, please try again.")

# Start the program
main()
