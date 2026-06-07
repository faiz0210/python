import random

print("Hello what's your name?")
name = input()

print(f"Well, '{name}', I am thinking of a number between 1 to 20 ")

secretNumber = random.randint(1, 20)

i = 0
while i < 7:
    print('Take a guess?')
    try:
        guess = int(input())
        i += 1
        if guess < secretNumber:
            print('Your guess is too low')
        elif guess > secretNumber:
            print('Your guess is too high')
        else:
            print(f"Good Job '{name}, you guessed the number {secretNumber} correctly in {i} attempts")
    except ValueError:
        print('Please enter a number.')


