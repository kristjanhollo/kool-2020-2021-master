guest_list = ["Toomas" , "Peeter" , "Meelis" , "Gustav"]
print(f"{guest_list[2]} ei saa peole tulla.")

del guest_list[2]
guest_list.insert(2, "Rasmus")
message = (
    f"Oled oodatud mu peole {guest_list[0]}!\n"
    f"Oled oodatud mu peole {guest_list[1]}!\n"
    f"Oled oodatud mu peole {guest_list[2]}!\n"
    f"Oled oodatud mu peole {guest_list[3]}!\n"
    ) 
print(message)

print("Ma leidsin meile suurema koha!\n")

guest_list.insert(0, "Oskar")
guest_list.insert(3, "Annika")
guest_list.append("Raigo")

print(message +
    f"Oled oodatud mu peole {guest_list[4]}!\n"
    f"Oled oodatud mu peole {guest_list[5]}!\n"
    f"Oled oodatud mu peole {guest_list[6]}!\n"
)

print("Vabandust, ruumi on ainult kahele inimesele.")

maha_list = guest_list.pop()
print(maha_list + " anna andeks, Sa pole peole enam kutsutud!")
maha_list = guest_list.pop()
print(maha_list + " anna andeks, Sa pole peole enam kutsutud!")
maha_list = guest_list.pop()
print(maha_list + " anna andeks, Sa pole peole enam kutsutud!")
maha_list = guest_list.pop()
print(maha_list + " anna andeks, Sa pole peole enam kutsutud!")
maha_list = guest_list.pop()
print(maha_list + " anna andeks, Sa pole peole enam kutsutud!")
print("Te olete oodatud mu peole "
    f"{guest_list[0]} , "
    f"{guest_list[1]}"
    )
del guest_list[0]
del guest_list[0]
