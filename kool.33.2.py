#Write a program that displays all even numbers between 0 and 100

x = 0
while x < 100:
    x = x + 1
    if x % 2 == 0:
        print(x)