from data import get_inventory, save_inventory, get_customers, save_customers, get_sales, save_sales

def add_product():
    name = input("Enter product name: ")
    price = input("Enter product price: ")
    quantity = input("Enter product quantity: ")
    category = input("Enter product category (optional): ")

    inventory = get_inventory()
    inventory.append([name, price, quantity, category])
    save_inventory(inventory)
    print("Product added successfully!")

def edit_product():
    name = input("Enter the name of the product to edit: ")
    inventory = get_inventory()
    for i, product in enumerate(inventory):
        if product[0] == name:
            price = input("Enter new price: ")
            quantity = input("Enter new quantity: ")
            category = input("Enter new category (optional): ")
            inventory[i] = [name, price, quantity, category]
            save_inventory(inventory)
            print("Product updated successfully!")
            return
    print("Product not found!")

def delete_product():
    name = input("Enter the name of the product to delete: ")
    inventory = get_inventory()
    for i, product in enumerate(inventory):
        if product[0] == name:
            inventory.pop(i)
            save_inventory(inventory)
            print("Product deleted successfully!")
            return
    print("Product not found!")

def add_customer():
    name = input("Enter customer name: ")
    contact = input("Enter customer contact details: ")

    customers = get_customers()
    customers.append([name, contact])
    save_customers(customers)
    print("Customer added successfully!")

def make_sale():
    cart = []
    while True:
        product_name = input("Enter product name to add to cart (or 'done' to finish): ")
        if product_name == 'done':
            break
        quantity = int(input(f"Enter quantity for {product_name}: "))

        inventory = get_inventory()
        for product in inventory:
            if product[0] == product_name:
                price = float(product[1])
                cart.append([product_name, price, quantity])
                break

    total = sum(price * quantity for _, price, quantity in cart)
    print(f"Total bill amount: ${total:.2f}")

    receipt = []
    for product_name, price, quantity in cart:
        receipt.append(f"{product_name} | {price} | {quantity}")
    receipt.append(f"Total | | {total:.2f}")

    sales = get_sales()
    sales.append(receipt)
    save_sales(sales)
    print("Sale completed and receipt generated!")

def view_inventory():
    inventory = get_inventory()
    for product in inventory:
        print(f"Name: {product[0]}, Price: {product[1]}, Quantity: {product[2]}, Category: {product[3]}")

def main():
    while True:
        print("\n--- Shopkeeper Application ---")
        print("1. Add Product")
        print("2. Edit Product")
        print("3. Delete Product")
        print("4. Add Customer")
        print("5. Make Sale")
        print("6. View Inventory")
        print("7. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            add_product()
        elif choice == '2':
            edit_product()
        elif choice == '3':
            delete_product()
        elif choice == '4':
            add_customer()
        elif choice == '5':
            make_sale()
        elif choice == '6':
            view_inventory()
        elif choice == '7':
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == '__main__':
    main()
