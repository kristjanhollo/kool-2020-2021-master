# Making a function
def foo(book: object) -> object:
    print(f"My favorite book is {book.title()}")


foo("Lord of the rings")

"""def shirt(size, message):
    print(f"Your t-shirt is {size.upper()} size and {message}.")

shirt("L", "I hate school")
shirt(size="XXL", message="Will this work?")

def linnad(city, country="Eesti"):
    print(f"{city.title()} asub {country}s")

linnad("Tallinn")
linnad("Tartu")
linnad("Moskva", country="Venemaa")

def city_country(city, country):
    print(f"{city.title()}, {country.title()}")

city_country("Tallinn", "Estonia")
city_country("Moskva", "Venemaa")

def muusik(name, album_name):
    album = {"name": name, "album": album_name}
    return album

laulja=muusik("Jimi Hendrix", "Voodoo child")
print(laulja)
laulja=muusik("Test", "Test1")
print(laulja)"""

"""def album(name, album_name, tracks=0):
    album = {"name": name.title(),
             "album": album_name.title(),
             }
    if tracks:
        album["tracks"] = tracks
    return album

# Questions
name_prompt = "\nName artist"
album_prompt = "Name album"

print("Enter 'quit' at any time to quit.")

while True:
    name = input(name_prompt)
    if name == 'quit':
        break

    album_name = input(album_prompt)
    if album_name == 'quit':
        break

    valmis = album(name, album_name)
    print(valmis)
print("Thank you for answering")"""

""" def greet_users(names):
    for name in names:
        print(f"Hello, {name.title()}!")

nimed = ["Peeter", "Kristjan", "toomas"]
greet_users(nimed) """

""" def show_messages(nimikiri, empty_nimekiri):
    while nimikiri:
        current_nimikiri = nimikiri.pop()
        print(f"Copying sentence to new list: {current_nimikiri}")
        empty_nimekiri.append(current_nimikiri)

def show_copy_messages(empty_nimikiri):
    print("\nThese sentences were copied:")
    for copied_message in empty_nimikiri:
        print(empty_nimikiri)

nimekiri = [
        "The mysterious diary records the voice.",
        "She was too short to see over the fence.",
        "Never underestimate the willingness of the greedy to throw you under the bus.",
        "Don't put peanut butter on the dog's nose.",
        "Malls are great places to shop; I can find everything I need under one roof.",
        "When motorists sped in and out of traffic, all she could think of was those in need of a transplant.",
        "The wake behind the boat told of the past while the open sea for told life in the unknown future.",
            ]

empty_nimekiri = []

show_messages(nimekiri[:], empty_nimekiri)
show_copy_messages(empty_nimekiri) """


def make_car(car, manuf, **information):
    autod = {
        "car": car.title(),
        "manuf": manuf.title(),
    }
    for option, value in information.items():
        autod[option] = value

        return autod


my_outback = make_car("subaru", "outback", color="red", tow_package=True)
print(my_outback)
my_honda = make_car("Accord", "Honda", color="black", year=2008, bigrims=True, ugly=True)
print(my_honda)
