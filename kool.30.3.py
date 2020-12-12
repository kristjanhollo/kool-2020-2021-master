print("Write your number: ")
number = int(input())
if number % 7 == 0:
    print("Dividable by 7")
elif number % 5 == 0:
    print("Dividable by 5")
elif number % 3 == 0:
    print("Dividable by 3")
else :
    print("Number is not dividable by 7, 5 or 3")