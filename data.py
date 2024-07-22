import os

INVENTORY_FILE = 'inventory.txt'
CUSTOMERS_FILE = 'customers.txt'
SALES_FILE = 'sales.txt'

def read_file(filename):
    if not os.path.exists(filename):
        return []
    with open(filename, 'r') as file:
        return [line.strip().split('|') for line in file]

def write_file(filename, data):
    with open(filename, 'w') as file:
        for line in data:
            file.write('|'.join(line) + '\n')

def get_inventory():
    return read_file(INVENTORY_FILE)

def save_inventory(inventory):
    write_file(INVENTORY_FILE, inventory)

def get_customers():
    return read_file(CUSTOMERS_FILE)

def save_customers(customers):
    write_file(CUSTOMERS_FILE, customers)

def get_sales():
    return read_file(SALES_FILE)

def save_sales(sales):
    write_file(SALES_FILE, sales)
