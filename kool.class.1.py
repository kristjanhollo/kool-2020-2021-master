from random import choice
import random

def lotto(numbers):
    winning_ticket = []
    while len(winning_ticket) < 8:
        pulled_number = random.choice(numbers)
        if pulled_number not in winning_ticket:
            winning_ticket.append(pulled_number)

    return winning_ticket


def check_ticket(played_ticket, winning_ticket):
    for element in played_ticket:
        if element not in winning_ticket:
            return False
    return True

def make_random_ticket(numbers):
    ticket = []
    while len(ticket) < 8:
        pulled_number = random.choice(numbers)
        if pulled_number not in ticket:
            ticket.append(pulled_number)
    return ticket


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e']
plays = 0
won = False

max_tries = 1_000_000
winning_ticket = lotto(numbers)

while not won:
    new_ticket = make_random_ticket(numbers)
    won = check_ticket(new_ticket, winning_ticket)
    plays += 1
    if plays >= max_tries:
        break

if won:
    print("We have a winning ticket!")
    print(f"Your ticket: {new_ticket}")
    print(f"Winning ticket: {winning_ticket}")
    print(f"It only took {plays} tries to win!")
else:
    print(f"Tried {plays} times, without pulling a winner. :(")
    print(f"Your ticket: {new_ticket}")
    print(f"Winning ticket: {winning_ticket}")


