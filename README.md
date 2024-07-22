# Shopkeeper Application

## Overview

The Shopkeeper Application is a simple Python-based application designed for managing shop inventory, customers, and sales. It includes functionalities for product management, customer management, sales processing, and inventory tracking. The application uses text files to store data, making it easy to set up and run without requiring a database.

## Features

- **Product Management**:
  - Add, edit, and delete products from the inventory.
  - Store product details like name, price, quantity, and category.
  - Manage low stock alerts (optional).

- **Customer Management**:
  - Create a simple customer database (name, contact details).
  - Track customer purchases (optional).

- **Sales Management**:
  - Add items to a shopping cart.
  - Calculate total bill amount based on product prices and quantities.
  - Apply discounts or promotions (optional).
  - Generate receipts with product details and totals.

- **Inventory Management**:
  - Track product stock levels and update them after sales.
  - Display low stock warnings and allow stock replenishment (optional).

## Files

- `shopkeeper_app.py`: The main application file with the core functionality.
- `data.py`: Manages data storage and retrieval.
- `inventory.txt`: Stores product inventory data.
- `customers.txt`: Stores customer information.
- `sales.txt`: Stores sales receipts.

## Requirements

- Python 3.x

No additional libraries are required for this basic setup.

## Setup

1. **Clone the repository**:
    ```bash
    git clone https://github.com/Ochieng-001/shopkeeper_app.git
    cd shopkeeper-app
    ```

2. **Create required files**:
   Ensure that the following files are present in the project directory:
    - `inventory.txt`
    - `customers.txt`
    - `sales.txt`

   You can create these files manually or use the application to generate them.

3. **Run the application**:
    ```bash
    python shopkeeper_app.py
    ```

## Usage

Once the application is running, you will be presented with a menu to choose various options:

1. Add Product
2. Edit Product
3. Delete Product
4. Add Customer
5. Make Sale
6. View Inventory
7. Exit

Follow the prompts to manage products, customers, and sales.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Python Programming Language
- File I/O operations in Python
