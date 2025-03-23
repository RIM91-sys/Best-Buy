import products
import store

def start(store_instance: store.Store):
    while True:
        print("\n   Store Menu")
        print("   ----------")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")

        choice = input("Please choose a number: ")

        if choice == "1":
            print("\n------")
            for idx, product in enumerate(store_instance.get_all_products(), 1):
                print(f"{idx}. {product.show().replace('Price:', 'Price: $')}")
            print("------")

        elif choice == "2":
            print(f"\nTotal of {store_instance.get_total_quantity()} items in store")

        elif choice == "3":
            shopping_list = []
            products = store_instance.get_all_products()

            print("\n------")
            for idx, product in enumerate(products, 1):
                print(f"{idx}. {product.show().replace('Price:', 'Price: $')}")
            print("------")
            print("When you want to finish order, enter empty text.")

            while True:
                try:
                    selection = input("Which product # do you want? ")
                    if selection == "":
                        break
                    selection = int(selection)
                    if 1 <= selection <= len(products):
                        quantity = int(input("What amount do you want? "))
                        shopping_list.append((products[selection - 1], quantity))
                        print("Product added to list!")
                    else:
                        print("Error adding product!")
                except ValueError:
                    print("Please enter a valid number.")

            try:
                total_cost = store_instance.order(shopping_list)
                print(f"\nOrder placed successfully! Total cost: ${total_cost}")
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    product_list = [
        products.Product("MacBook Air M2", price=1450, quantity=100),
        products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        products.Product("Google Pixel 7", price=500, quantity=250),
    ]
    best_buy = store.Store(product_list)
    start(best_buy)
