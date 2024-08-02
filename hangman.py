from random import choice

def run_game():
    word: str = choice(['secret', 'apple', 'banana', 'taxi', 'horse', 'weather'])
    username: str = input('What is your name? >> ')
    print(f'Welcome to hangman, {username}!')

    guessed: str = ''
    tries: int = 3

    # Setup
    while tries > 0:
        blanks: int = 0
        print('Word: ', end='')
        for letter in word:
            if letter in guessed:
                print(letter, end='')
            else:
                print('_', end='')
                blanks += 1

        print() # Add a blank line

        if blanks == 0:
            print('You got it!')
            break
        guess: str = input('Enter a letter: ')
        if guess in guessed:
            print(f'You already used: {guess}. Please try with another letter!')
            continue
        
        if len(guess) > 1: 
            if guess == word:
                print(f'Word: {word}')
                print('You got it')
                break
            else:
                print('You should guess the word completely or you can guess only one letter!')
                continue

        guessed += guess

        if guess not in word:
            tries -= 1
            print(f'Sorry, that was wrong ... ({tries} tries remaining)')
        
        if tries == 0:
            print('No more tries remaining ... you lose.')
            break


if __name__ == '__main__':
    run_game()