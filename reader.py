with open("text.txt") as file_object:
    lines = file_object.readlines()
pi_string = ""
for line in lines:
    pi_string += line.rstrip()

birthday = input("When is your birthday? Please enter in form of dd/mm/yy: ")
if birthday in pi_string:
    print("Your birthday is in pi-string")
else:
    print("Your birthday is not in pi-string")



