from product import Product

class Inventory:
    def __init__(self):
        # Dictionary to store products
        self.products = {}

    def add_product(self, product):
        """Add a product to the inventory."""
        self.products[product.name] = product

    def remove_product(self, product_name):
        """Remove a product from the inventory."""
        if product_name in self.products:
            del self.products[product_name]
            return True
        return False

    def find_product(self, product_name):
        """Find a product by name."""
        return self.products.get(product_name)

    def display_inventory(self):
        """Return a list of all product information."""
        if not self.products:
            return ["Inventory is empty."]

        inventory_list = []
        for product in self.products.values():
            inventory_list.append(product.get_product_info())
        return inventory_list