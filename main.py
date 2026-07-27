import tkinter as tk
from tkinter import messagebox, simpledialog

from product import Product
from inventory import Inventory
from sales_transaction import SalesTransaction

# Create inventory object
inventory = Inventory()

# Add default products
inventory.add_product(Product("Latte", 5.25, 15))
inventory.add_product(Product("Iced Coffee", 5.75, 12))
inventory.add_product(Product("Mocha", 6.00, 10))
inventory.add_product(Product("Energy Tea", 3.50, 20))


# Function to add a new product
def add_product():
    name = simpledialog.askstring("Add Product", "Enter product name:")

    if not name:
        return

    try:
        price = float(simpledialog.askstring("Add Product", "Enter product price:"))
        quantity = int(simpledialog.askstring("Add Product", "Enter quantity:"))
    except (TypeError, ValueError):
        messagebox.showerror("Error", "Please enter valid values.")
        return

    # Check for valid input
    if name.strip() == "":
        messagebox.showerror("Error", "Product name cannot be empty.")
        return

    if price < 0:
        messagebox.showerror("Error", "Price cannot be negative.")
        return

    if quantity < 0:
        messagebox.showerror("Error", "Quantity cannot be negative.")
        return

    product = Product(name, price, quantity)
    inventory.add_product(product)

    messagebox.showinfo("Success", f"{name} added successfully!")


# Function to display inventory
def view_inventory():
    inventory_list = inventory.display_inventory()

    messagebox.showinfo(
        "Current Inventory",
        "\n".join(inventory_list)
    )


# Function to sell a product
def sell_product():
    name = simpledialog.askstring("Sell Product", "Enter product name:")

    if not name:
        return

    product = inventory.find_product(name)

    if product is None:
        messagebox.showerror("Error", "Product not found.")
        return

    try:
        quantity = int(simpledialog.askstring("Sell Product", "Enter quantity:"))
    except (TypeError, ValueError):
        messagebox.showerror("Error", "Invalid quantity.")
        return

    sale = SalesTransaction()

    if sale.add_to_cart(product, quantity):
        messagebox.showinfo("Receipt", sale.generate_receipt())
    else:
        messagebox.showerror("Error", "Not enough inventory available.")


# ---------------- GUI ---------------- #

root = tk.Tk()
root.title("☕ Coffee Shop Inventory System")
root.geometry("450x350")

title = tk.Label(
    root,
    text="☕ Coffee Shop Inventory System ☕",
    font=("Arial", 18, "bold")
)
title.pack(pady=20)

tk.Button(
    root,
    text="Add Product",
    width=25,
    command=add_product
).pack(pady=5)

tk.Button(
    root,
    text="View Inventory",
    width=25,
    command=view_inventory
).pack(pady=5)

tk.Button(
    root,
    text="Sell Product",
    width=25,
    command=sell_product
).pack(pady=5)

tk.Button(
    root,
    text="Exit",
    width=25,
    command=root.destroy
).pack(pady=20)

root.mainloop()