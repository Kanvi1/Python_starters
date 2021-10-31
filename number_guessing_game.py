import random

guesses = 0
number = 0
gameover = 0

while not gameover:
    number = random.randint(0,20);
    guesses = 0
    
    while True:
        guesses += 1
        guess = input("What's your guess? ")

        if guess.isdigit():
            guess = int(guess)
        else:
            guess = input('Please guess a number: ')
            continue
        
        if(number == guess):
            print("Correct! You Win!")
            print("You took", guesses, "guesses.")
            gameover = input("Play again?(y/n) ").lower() != 'y'
            break
        elif guess > number:
            print('Incorrect! Guess a lower number! ')
        else:
            print("Incorrect! Guess a higher number!")
    
