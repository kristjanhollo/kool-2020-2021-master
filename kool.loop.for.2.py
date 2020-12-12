numbrid = list(range(-20,21))
for number in numbrid[:6]:
    print("First six numbers: ", number)
for number in numbrid[-6:]:
    print("Last six numbers: ", number)
for number in numbrid:
    if number % 2 == 0:
        print("Even numbers: ", number)
for number in numbrid:
    if number == 5:
        continue
    print("Skip number 5: ", number)
for number in numbrid:
    if number == 8:
        break
    print("Up to number 7: ", number)
for number in numbrid:
    if number % 3 == 0:
        print("Dividable by 3: ", number)
print("Sum of all numbers is: ", sum(numbrid))
        ###for number in numbrid:
        ###if number >= 4:
        ###summa = number + 1
        ### print(summa)
for number in numbrid:
    print("Power of numbers: ", number * number)
for number in numbrid:
    print("Modulo of 10: ", number % 10)