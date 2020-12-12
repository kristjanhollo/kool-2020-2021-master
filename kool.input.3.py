tervitus = "Tere! Kui vana Te olete?:"

while True:
    vanus = int(input(tervitus))
    if vanus < 3:
        print("Pilet on tasuta")
    elif vanus > 3 or vanus < 12:
        print("Teie pilet maksab €10")
    elif vanus > 15:
        print("Teie pilet on €15")
    else:
        vanus == "quit"
        break