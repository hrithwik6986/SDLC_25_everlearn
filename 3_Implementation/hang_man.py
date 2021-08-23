import random

hangman = ['''
    ======
         |
         |
         |
         |
        ===''', '''
    ======
    O    |
         |
         |
         |
        ===''', '''
    ======
    O    |
    |    | 
         |
         |
        ===''', '''
    ======
    O    |
   /|    |
         |
         |
        ===''', '''
    ======
    O    |
   /|\   |
         |
         |
        ===''', '''
    ======
    O    |
   /|\   |
   /     |
         |
        ===''', '''
    ======
    O    |
   /|\   |
   / \   | 
         |
        ===''']
countries = 'algeria argentina angola austria afghanistan bulgaria bangladesh belgium brazil bolivia bhutan bahamas cambodia china chile canada cuba denmark egypt fiji finland france germany greece georgia hungary iceland india indonesia iran iraq ireland israel italy japan jamaica kuwait korea kenya libya madagascar malaysia maldives mexico mongolia mauritius nepal norway netherlands nigeria oman pakistan portugal poland qatar russia serbia somalia singapore spain sweden switzerland taiwan thailand turkey unitedkingdom ukraine venezuela vietnam yemen zambia zimbabwe'.split()

def random_word(wordList):
    index = random.randint(0, len(wordList)-1)
    return wordList[index]

def display(missed, correct, secretWord):
    print(hangman[len(missed)])
    print()
    print('MISSED LETTERS: ', end=' ')
    for i in missed:
        print(i, end=' ')
    print()
    dash = '_' * len(secretWord)
    for i in range(len(secretWord)):
        if secretWord[i] in correct:
            dash = dash[:i] + secretWord[i] + dash[i+1:]
    # Display the secret word with spaces between the letters:
    for i in dash:
        print(i, end =' ')
    print()

def get_letter(alreadyGuessed):
    """ Returns the letter the player entered. Checks whether the player enters a single letter """
    while True:
        print('GUESS A LETTER: ')
        l = input()
        l = l.lower()
        if len(l) != 1:
            print('Enter single letter only.')
        elif l in alreadyGuessed:
            print('You have already guessed that letter. Try again')
        elif l not in 'abcdefghijklmnopqrstuvwxyz':
            print('Please enter only alphabet.')
        else:
            return l

def playAgain():
    """ Returns True if the player wants to play again, False otherwise """
    print('\nWOULD YOU LIKE TO PLAY AGAIN? Press y for yes and n for no')
    return input().lower().startswith('y')

print('=======================================')
print('		WELCOME TO HANGMAN GAME		')
print('=======================================')
print()
print(  'GUESS THE COUNTRY')
missed = ''
correct = ''
secretWord = random_word(countries)
gameOver = False

while True:
    display(missed, correct, secretWord)
    # Let the player enter a letter:
    l = get_letter(missed + correct)

    if l in secretWord:
        correct = correct + l
        # Check to see if the player has won:
        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correct:
                foundAllLetters = False
                break
        if foundAllLetters:
            print('You guessed it!')
            print('The secret word is "' + secretWord + '"! You win!')
            gameOver = True
    else:
        missed = missed + l
        # Check if the player has guessed too many times and lost.
        if len(missed) == len(hangman) -1:
            display(missed, correct, secretWord)
            print('You have run out of guesses!!!\nAfter ' + str(len(missed)) + ' missed guesses and ' + str(len(correct)) + ' correct guesses, the word was "' + secretWord + '"')
            gameOver = True
    # If the game is over, ask the player to try again.
    if gameOver:
        if playAgain():
            missed = ''
            correct = ''
            gameOver = False
            secretWord = random_word(countries)
        else:
            break
