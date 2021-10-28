import random

print('Hello. What is your name?')
name = input()

print('Well, ' + name + ', I am thinking of a number between 1 and 20')
print('You will have exactly 7 tries to figure out the number I am thinking of')
secretNumber = random.randint(1,20)

for guessesTaken in range(1,7):
    print('Take a guess')
    guess = int(input())

    if guess < secretNumber:
        print('Your guess is too low.')
    elif guess > secretNumber:
        print('Your guess is too high.')
    else:
        break # this condition is because the user's guess was correct

if guess == secretNumber:
    print('Good job ' + name + '! You guessed my number in ' + str(guessesTaken) + ' guesses!')
else:
    print('Nope. The number I was thinking of was ' + str(secretNumber))
