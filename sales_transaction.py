class SalesTransaction:
    def __init__(self):
        # List to store purchased items
        self.cart = []

    def add_to_cart(self, product, quantity):
        """Add a product to the shopping cart."""
        if quantity <= product.quantity:
            product.update_quantity(-quantity)
            self.cart.append((product.name, quantity, product.price))
            return True
        return False

    def calculate_total(self):
        """Calculate the total cost of the transaction."""
        total = 0
        for item in self.cart:
            total += item[1] * item[2]
        return total

    def generate_receipt(self):
        """Generate a formatted receipt."""
        receipt = "☕ Coffee Shop Receipt ☕\n"
        receipt += "=" * 30 + "\n"

        for item in self.cart:
            subtotal = item[1] * item[2]
            receipt += f"Item: {item[0]}\n"
            receipt += f"Quantity: {item[1]}\n"
            receipt += f"Price Each: ${item[2]:.2f}\n"
            receipt += f"Subtotal: ${subtotal:.2f}\n"
            receipt += "-" * 30 + "\n"

        receipt += f"TOTAL: ${self.calculate_total():.2f}\n"
        receipt += "=" * 30 + "\n"
        receipt += "Thank you for visiting!"

        return receipt