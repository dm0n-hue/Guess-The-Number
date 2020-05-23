import random

def getNumber(answerNumber, compGuess):
    if answerNumber == compGuess:
        return 'That is correct!'
    elif answerNumber < 0:
        return 'That answer is too low. It is not in the range of numbers to guess from.'
    elif answerNumber > 9:
        return 'That answer is too high. It is not in the range of numbers to guess from.'
    else:
        return 'The computers number was ' + str(compGuess) + '. Try again.'

secret = random.randint(1,9)
try:
    # for answerNumber in range(1,7):
        print('Guess the number the computer is thinking from 1 through 9')
        print(getNumber(int(input()), secret))
except ValueError:
    print('You did not enter an integer')

# try and add multiple attempts into the code where it reads back to you
# how many guesses there are left
