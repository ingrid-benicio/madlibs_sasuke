import random

#computer 
def guess(x):
    random_number = random.randint(1, x)
    guess = 0

    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {x}: "))
        print(guess)
        if guess < random_number:
            print('\nSorry, your guess is too low. Guess again.\n')
        elif guess > random_number:
            print("\nSorry, your guess is too high. Guess again.\n")

    print (f'Yey! Congrats champs, you got the righ number {random_number}!')
    

guess (10)


#user

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'C':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        feedback = input(f'\nIs the {guess} correct (C) ? too low (L)? to high (H)? ')
        if feedback == 'H':
            high = guess - 1
        elif feedback == 'L':
            low = guess + 1

    print (f'\nYay! The computer guessed the righ number {guess}') 

computer_guess(10)


    
 
