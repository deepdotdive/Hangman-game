from random import choice
from string import ascii_lowercase

word = choice(['python', 'java', 'kotlin', 'javascript'])
bank = set()
lives = 8

print('H A N G M A N')
while True:
    hint = ['-' for x in word]
    bank.clear()
    option = input('Type "play" to play the game, "exit" to quit: ')
    if option not in ('play', 'exit'):
        pass
    elif option == 'exit':
        break
    if option == 'play':

        while lives != 0:
            input_ = input(f'\n{"".join(hint)}\nInput a letter: ')

            if len(input_) != 1 or input_ == ' ':
                print('You should input a single letter')
            elif input_ not in ascii_lowercase:
                print('It is not an ASCII lowercase letter')
            elif input_ in bank:
                print('You already typed this letter')
            elif input_ not in word:
                print('No such letter in the word')
                lives -= 1

            hint = [input_ if x == input_ else hint[i] for i, x in enumerate(word)]

            bank.add(input_)
            if '-' not in hint:
                print(f'You guessed the word {"".join(hint)}!\nYou survived!\n')
                break
        else:
            print('You are hanged!\n')
            break
