# from replit import clear
#HINT: You can call clear() to clear the output in the console.

from art import logo

print(logo)
print("Welcome to the secret auction program.")

is_finished = False
participants = {}


while not is_finished:
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: "))
    finish = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    participants[name] = {"bid": bid}
    if finish == 'no':
        is_finished = True

    # clear()

highest_bid = 0
highest_bid_name = ""

for participant in participants:
    if participants[participant]["bid"] >= highest_bid:
        highest_bid = participants[participant]["bid"]
        highest_bid_name = participant


print(f"The winner is {highest_bid_name} with a bid of ${highest_bid}")