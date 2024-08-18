import random
from art import logo, vs
from game_data import data

is_continue = True
player_score = 0


def compare_followers(compare_a, compare_b):
    """Compare followers against user's guess 
    and returns True if they got it right.
    Or False if they got it wrong."""
    if compare_a['follower_count'] > compare_b['follower_count']:
        return 'a'
    else:
        return 'b'


def format_data(account):
    """Format account into printable format: name, description and country"""
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name}, a {description}, from {country}"


def check_answer(player_answer, compare_a, compare_b):
    compared_value = compare_followers(compare_a, compare_b)
    print(f"compared value: {compared_value}")
    if player_answer == compared_value:
        global is_continue
        is_continue = True
        global player_score
        player_score += 1
        print(f"player score: {player_score}")
        print(f"is continue?: {is_continue}")
    else:
        is_continue = False
        print(f"is continue when false: {is_continue}")


def high_lower_game():
    print(logo)
    compare_a = random.choice(data)
    compare_b = random.choice(data)
    print(f"Compare A: {format_data(compare_a)}")
    print(vs)
    print(f"Compare B: {format_data(compare_b)}")
    player_answer = (input("Who has more followers? Type 'A' or 'B': ")).lower()
    print(f"player answer: {player_answer}")
    check_answer(player_answer, compare_a, compare_b)
    print(f"is_continue in high lower func:{is_continue}")
    while is_continue:
        print(logo)
        compare_a = compare_b
        compare_b = random.choice(data)
        print(f"Compare A: {format_data(compare_a)}")
        print(vs)
        print(f"Compare B: {format_data(compare_b)}")
        player_answer = (input("Who has more followers? Type 'A' or 'B': ")).lower()
        print(f"player answer: {player_answer}")
        check_answer(player_answer, compare_a, compare_b)
        print(f"is_continue in high lower func:{is_continue}")
    print(logo)
    print(f"Sorry, that's wrong. Final score: {player_score}")


high_lower_game()
