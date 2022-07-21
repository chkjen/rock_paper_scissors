import random

def play():
    user = input("What is your choice? 'r' for rock, 'p' for paper, 's' for scissors:\n ").lower()
    computer = random.choice(['r','p','s'])
    print (f"Computer selection = {computer} ")

    if user == computer:
        return "It's a tie"

    # r > s, s > p, p > r
    if is_win(user,computer):
        return "You won!"

    return "You lost!"



def is_win(player, opponent):
    #returns as true if the player wins.
    # r > s, s > p, p > r

    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True


print(play())