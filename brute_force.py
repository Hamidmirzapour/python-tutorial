import itertools
import string
import time

def common_guess(word: str) -> str | None:
    with open('common_words.txt', 'r') as words:
        words_list: list[str] = words.read().splitlines()
        
        for i, match in enumerate(words_list, start=1):
            if word == match:
                return f'Common match: {word} (#{i})'


def brute_force(word: str, length: int, digits: bool = False, symbols: bool = False) -> str | None:
    chars: str = string.ascii_lowercase + string.ascii_uppercase
    if digits:
        chars += string.digits
    if symbols:
        chars += string.punctuation

    attempts: int = 0
    for i in range(3, 14):
        for guess in itertools.product(chars, repeat=i):
            attempts += 1
            guess: str = ''.join(guess)
            
            if guess == word:
                return f'"{word}" was cracked in {attempts:,} guesses.'

        print(f'There was no match for {i} chars searching ...')

def main():
    print('Searching ...')
    password: str = input('Enter a password to show you how much time needed to crack it 😊: ')

    start_time: float = time.perf_counter()
    if common_match := common_guess(password):
        print(common_match)
    else:
        if cracked := brute_force(password, 14, True, True):
            print(cracked)
        else:
            print('There was no match')

    end_time: float = time.perf_counter()
    print(round(end_time - start_time, 2), 's needed to crack your password.')
    

if __name__ == '__main__':
    main()