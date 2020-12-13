people = {}

polling_active = True

while polling_active:
    name = input("\nWhat is your name? ")
    favorite_country = input(" What is your favorite country?" )
    people[name] = favorite_country

    repeat = input(" Would you like to let another person respond? (yes/no)" )
    if repeat == "no":
        polling_active = False

print("---Poll results---")

for name, favorite_country in people.items():
    print(f"{name} favorite country is {favorite_country}")

print(people)
