import random

def play():
    user = input("Pick your choice: 'r' for rock, 'p' for paper and 's' for scissors': \n")
    computer = random.choice(['r','p','s'])
    if user == computer:
        return 'That was a tie!'
    
    if is_win(user, computer):
        return "You won!"
    return 'You lost!'


def is_win (player, opponent):
    if (player == 'r' and opponent =='s') or (player == 's' and opponent =='p') \
    or (player == 'p' and opponent == 'r'):
        return True
    
print(play())