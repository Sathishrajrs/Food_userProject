class User:
    def __init__(self, full_name, phone_number, email, address, password):
        self.full_name = full_name
        self.phone_number = phone_number
        self.email = email
        self.address = address
        self.password = password
        self.order_history = []

class FoodItem:
    def __init__(self, name, description, price):
        self.name = name
        self.description = description
        self.price = price

class Application:
    def __init__(self):
        self.users = []
        self.food_menu = [
            FoodItem("Tandoori Chicken", "4 pieces", 240),
            FoodItem("Vegan Burger", "1 Piece", 320),
            FoodItem("Truffle Cake", "500gm", 900)
        ]
        self.logged_in_user = None

    def register_user(self, full_name, phone_number, email, address, password):
        user = User(full_name, phone_number, email, address, password)
        self.users.append(user)

    def login_user(self, email, password):
        for user in self.users:
            if user.email == email and user.password == password:
                self.logged_in_user = user
                return True
        return False

    def display_food_menu(self):
        print("Food Menu:")
        for i, item in enumerate(self.food_menu, start=1):
            print(f"{i}. {item.name} ({item.description}) [INR {item.price}]")

    def place_order(self, order_items):
        if self.logged_in_user:
            selected_items = [self.food_menu[i - 1] for i in order_items]
            self.logged_in_user.order_history.append(selected_items)
            print("Order placed successfully!")
        else:
            print("Please log in to place an order.")

    def view_order_history(self):
        if self.logged_in_user:
            print("Order History:")
            for i, order in enumerate(self.logged_in_user.order_history, start=1):
                print(f"Order {i}:")
                for item in order:
                    print(f"{item.name} ({item.description}) [INR {item.price}]")
        else:
            print("Please log in to view order history.")

    def update_profile(self, full_name, phone_number, address):
        if self.logged_in_user:
            self.logged_in_user.full_name = full_name
            self.logged_in_user.phone_number = phone_number
            self.logged_in_user.address = address
            print("Profile updated successfully!")
        else:
            print("Please log in to update your profile.")

if __name__ == "__main__":
    app = Application()

    while True:
        print("\nOptions:")
        print("1. Register")
        print("2. Log in")
        print("3. Place New Order")
        print("4. Order History")
        print("5. Update Profile")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            full_name = input("Full Name: ")
            phone_number = input("Phone Number: ")
            email = input("Email: ")
            address = input("Address: ")
            password = input("Password: ")
            app.register_user(full_name, phone_number, email, address, password)

        elif choice == "2":
            email = input("Email: ")
            password = input("Password: ")
            if app.login_user(email, password):
                print(f"Logged in as {app.logged_in_user.full_name}")
            else:
                print("Login failed. Please check your email and password.")

        elif choice == "3":
            if app.logged_in_user:
                app.display_food_menu()
                order_items = input("Enter the numbers of items you want to order (e.g., 1 2 3): ")
                order_items = [int(i) for i in order_items.split()]
                app.place_order(order_items)
            else:
                print("Please log in to place an order.")

        elif choice == "4":
            app.view_order_history()

        elif choice == "5":
            if app.logged_in_user:
                full_name = input("Full Name: ")
                phone_number = input("Phone Number: ")
                address = input("Address: ")
                app.update_profile(full_name, phone_number, address)
            else:
                print("Please log in to update your profile.")

        elif choice == "6":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")
