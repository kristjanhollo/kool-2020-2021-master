rivers = {"Prita jõgi": "Tallinn", "Ema jõgi": "Tartu", "Püha jõgi": "Rakvere"}
for jõed, linnad in rivers.items():
    print(f"{jõed} asub {linnad}.")

"""for jõed in rivers.keys():
    print(f"{jõed}")"""

for linnad in rivers.values():
    print(f"{linnad}")