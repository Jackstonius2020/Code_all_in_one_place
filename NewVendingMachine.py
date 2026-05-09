products = {
    "1": ("Water", 2.00),
    "2": ("Sparkling Water", 3.00),
    "3": ("Orange Juice", 4.50),
    "4": ("Apple Juice", 4.50),
    "5": ("Mango Juice", 5.00),
    "6": ("Cola", 4.00),
    "7": ("Diet Cola", 4.00),
    "8": ("Energy Drink", 6.00),
    "9": ("Iced Tea", 4.50),
    "10": ("Milk", 3.50),

    "11": ("Potato Chips", 3.50),
    "12": ("Cheese Chips", 3.50),
    "13": ("Nachos", 4.00),
    "14": ("Popcorn", 3.00),
    "15": ("Pretzels", 3.00),
    "16": ("Salted Peanuts", 4.00),
    "17": ("Cashew Nuts", 6.00),
    "18": ("Trail Mix", 5.50),
    "19": ("Crackers", 3.00),
    "20": ("Granola Bar", 4.00),

    "21": ("Milk Chocolate", 5.00),
    "22": ("Dark Chocolate", 5.50),
    "23": ("White Chocolate", 5.00),
    "24": ("Chocolate Wafer", 4.00),
    "25": ("Chocolate Cookies", 4.50),
    "26": ("Vanilla Cookies", 4.00),
    "27": ("Oat Cookies", 4.50),
    "28": ("Brownie", 5.50),
    "29": ("Muffin", 5.00),
    "30": ("Cupcake", 4.50),

    "31": ("Gummy Bears", 4.00),
    "32": ("Sour Gummies", 4.00),
    "33": ("Fruit Candy", 3.50),
    "34": ("Mint Candy", 3.00),
    "35": ("Lollipop", 2.50),
    "36": ("Chewing Gum", 2.00),
    "37": ("Chocolate Bar", 5.00),
    "38": ("Caramel Candy", 3.50),
    "39": ("Toffee", 3.00),
    "40": ("Marshmallows", 4.00),

    "41": ("Chicken Sandwich", 8.00),
    "42": ("Cheese Sandwich", 7.50),
    "43": ("Tuna Sandwich", 8.50),
    "44": ("Veggie Wrap", 7.00),
    "45": ("Chicken Wrap", 8.50),
    "46": ("Hot Dog", 7.00),
    "47": ("Burger", 9.00),
    "48": ("Pizza Slice", 6.50),
    "49": ("Pasta Cup", 7.50),
    "50": ("Noodles Cup", 6.00),
}

def display_products():
    print("\n========== VENDING MACHINE ==========")
    for key in sorted(products, key=lambda x: int(x)):
        name, price = products[key]
        print(f"{key}. {name} - {price:.2f} AED")
    print("0. Exit")

def vending_machine():
    while True:
        display_products()
        choice = input("\nSelect a product number: ")

        if choice == "0":
            print("Thank you for using the vending machine.")
            break

        if choice not in products:
            print("Invalid selection. Please try again.")
            continue

        name, price = products[choice]
        print(f"\nSelected product: {name}")
        print(f"Price: {price:.2f} AED")

        try:
            money = float(input("Insert money (AED): "))
        except ValueError:
            print("Invalid amount. Please enter numbers only.")
            continue

        if money < price:
            print("Insufficient funds.")
            print(f"Inserted: {money:.2f} AED")
            print(f"Required: {price:.2f} AED")
            print("Money refunded.")
        else:
            change = money - price
            print(f"Purchase successful. Enjoy your {name}.")
            if change > 0:
                print(f"Change returned: {change:.2f} AED")

        input("\nPress Enter to continue...")

# Start the vending machine
vending_machine()