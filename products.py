class Product:
    def __init__(self, name: str, price: float, quantity: int):
        if not name or price < 0 or quantity < 0:
            raise ValueError("Invalid product details: Name cannot be empty, price and quantity must be non-negative.")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

    def get_quantity(self) -> int:
        return self.quantity

    def set_quantity(self, quantity: int):
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        self.quantity = quantity
        if self.quantity == 0:
            self.deactivate()

    def is_active(self) -> bool:
        return self.active

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def show(self) -> str:
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"

    def buy(self, quantity: int) -> float:
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero.")
        if quantity > self.quantity:
            raise ValueError("Not enough stock available.")

        total_price = quantity * self.price
        self.set_quantity(self.quantity - quantity)
        return total_price


# Test Code
if __name__ == "__main__":
    bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    mac = Product("MacBook Air M2", price=1450, quantity=100)

    print(bose.buy(50))  # Expected output: 12500
    print(mac.buy(100))  # Expected output: 145000
    print(mac.is_active())  # Expected output: False (since quantity reaches 0)

    print(bose.show())
    print(mac.show())

    bose.set_quantity(1000)
    print(bose.show())
