class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = float(price)
        self.quantity = int(quantity)

    def update_quantity(self, amount):
        """Increase or decrease the quantity."""
        self.quantity += amount

    def get_product_info(self):
        """Return a formatted string with product details."""
        return f"{self.name} - ${self.price:.2f} (Quantity: {self.quantity})"