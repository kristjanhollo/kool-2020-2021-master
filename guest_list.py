with open("guest_list.txt", "a") as file_object:
    questions = True
    while questions:
        print("You can always quit with 'quit' ")
        print("Please insert your name: ")
        nimi = input()
        if nimi == "quit" :
            questions = False
            break
        else:
            print(f"{nimi.title()} has been added to questlist. Thank you!")
            file_object.write(nimi + "\n")