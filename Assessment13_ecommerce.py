class Product:
    def __init__(self, pid, name, price, stock):
        self.pid = pid
        self.name = name
        self.price = price
        self.stock = stock

class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add_item(self, product, qty):
        if qty > product.stock:
            print(f"  Only {product.stock} units available.")
            return
        self.items[product] = self.items.get(product, 0) + qty
        print(f" Added {qty}x {product.name}")

    def remove_item(self, product):
        if product in self.items:
            del self.items[product]
            print(f"  Removed {product.name}")

    def view_cart(self):
        if not self.items:
            print(" Cart is empty!")
            return 0
        total = 0
        print(f"\n{'Product':<25} {'Qty':>4} {'Price':>8} {'Total':>10}")
        print("-" * 50)
        for product, qty in self.items.items():
            subtotal = product.price * qty
            total += subtotal
            print(f"{product.name:<25} {qty:>4} ₹{product.price:>7.2f} ₹{subtotal:>9.2f}")
        print("-" * 50)
        print(f"{'TOTAL':>40} ₹{total:>9.2f}")
        return total

    def checkout(self):
        total = self.view_cart()
        if total == 0:
            return
        print("\n1. Cash on Delivery\n2. UPI\n3. Card")
        choice = input("Payment method: ")
        methods = {"1": "Cash on Delivery", "2": "UPI", "3": "Card"}
        print(f" Order placed! Total: ₹{total:.2f} via {methods.get(choice, 'Unknown')}")
        self.items.clear()

def main():
    products = [
        Product(1, "Python Book",      499.00, 10),
        Product(2, "Mechanical Keyboard", 2499.00, 5),
        Product(3, "USB-C Hub",         899.00,  8),
        Product(4, "Laptop Stand",      749.00, 12),
        Product(5, "Wireless Mouse",    649.00, 15),
    ]
    cart = ShoppingCart()

    print("=" * 45)
    print(" E-Commerce Cart System")
    print("=" * 45)

    while True:
        print("\n1. View Products\n2. Add to Cart\n3. View Cart\n4. Remove Item\n5. Checkout\n6. Exit")
        choice = input("Choice: ")

        if choice == "1":
            print(f"\n{'ID':<4} {'Name':<25} {'Price':>10} {'Stock':>6}")
            print("-" * 48)
            for p in products:
                print(f"{p.pid:<4} {p.name:<25} ₹{p.price:>8.2f} {p.stock:>6}")
        elif choice == "2":
            pid = int(input("Enter Product ID: "))
            product = next((p for p in products if p.pid == pid), None)
            if product:
                qty = int(input("Enter quantity: "))
                cart.add_item(product, qty)
            else:
                print(" Product not found.")
        elif choice == "3":
            cart.view_cart()
        elif choice == "4":
            pid = int(input("Enter Product ID to remove: "))
            product = next((p for p in products if p.pid == pid), None)
            if product:
                cart.remove_item(product)
        elif choice == "5":
            cart.checkout()
        elif choice == "6":
            print(" Goodbye!")
            break

if __name__ == "__main__":
    main()