sandwich_orders = ["Beef sandwich", "Pastrami sandwich", "Cheese sandwich", "Pastrami sandwich",
                   "Chicken sandwich", "Pork sandwich", "Tuna sandwich", "Pastrami sandwich"]
finished_sandwiches = []

print("Deli has run out from Pastrami sandwiches! Sorry")

while "Pastrami sandwich" in sandwich_orders:
    sandwich_orders.remove("Pastrami sandwich")

while sandwich_orders:
    sandwich = sandwich_orders.pop()

    print(f"This {sandwich} is ready!")
    finished_sandwiches.append(sandwich)

print("We are out of sandwiches")
print(sandwich_orders)
while polling_active:
    name = input("\nWhat is your name?")
    favorite_country = input("What is your favorite country"?)