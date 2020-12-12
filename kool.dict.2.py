"""Kristjan = {"name": "Kristjan", "surname": "Hollo", "age": 30, "town": "Tallinn"}
Annika = {"name": "Annika", "surname": "Andresen", "age": 29, "town": "Pärnu"}
Oleg = {"name": "Oleg", "surname": "Prokofijev", "age": 53, "town": "Lasnamägi"}

inimesed = [Kristjan, Annika, Oleg]

for inimene in inimesed:
    print(inimene["name"], "on", inimene["age"], "aastat vana. Ta elab", inimene["town"],"linnas.")"""

favorite_places = {
    "Kristjan": {
        "linn": "Tallinn",
        "linn_2": "Pärnu",
        "linn_3": "Tartu"
    },

    "Annika": {
        "linn": "Pärnu",
        "linn_2": "Tallinn",
        "linn_3": "Kuressaare"
    },

    "Peeter": {
        "linn": "Las Vegas",
        "linn_2": "New York",
        "linn_3": "Istanbul"
    }
}

for nimi, info in favorite_places.items():
    print(f"nimi: {nimi}")
    le_linn = info["linn"]
    le_linn_2 = info["linn_2"]
    le_linn_3 = info["linn_3"]
    print("Lemmik linn on: ", le_linn)
    print("Teine lemmik linn on: ", le_linn_2)
    print("Kolmas lemmik linn on: ", le_linn_3,"\n")
    