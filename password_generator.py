import string
import secrets

def contains_upper(password: str) -> bool:
    for char in password:
        if char.isupper():
            return True
    return False


def contains_symbol(password: str) -> bool:
    for char in password:
        if char in string.punctuation:
            return True
    return False

def generate_password(length: int, upper: bool, symbols: bool) -> str:
    combination: str = string.ascii_lowercase + string.digits
    new_password = ''

    if upper:
        combination += string.ascii_uppercase
        uppercases = string.ascii_uppercase
        new_password += uppercases[secrets.randbelow(len(uppercases))]
    
    if symbols:
        combination += string.punctuation
        symbols = string.punctuation
        new_password += symbols[secrets.randbelow(len(symbols))]

    combination_length = len(combination)


    for _ in range(length - 2):

        new_password += combination[secrets.randbelow(combination_length)]

    return new_password

if __name__ == '__main__':
    print('Welcome to password generator!')
    try:
        password_count: int = int(input('How many passwords you want? '))
        while True:
            password_length: int = int(input('Enter the length of password(s): '))
            if password_length > 2:
                break
            else:
                print('Password length should be greater than 3 !')
        password_has_upper: bool = bool(input('Should password(s) contains uppercase characters? (True or False) ').capitalize())
        password_has_symbols: bool = bool(input('Should password(s) contains symbols? (True or False) ').capitalize())
    except ValueError:
        print('Invalid input(s) ...')
    for i in range(1, password_count):
        password = generate_password(password_length, password_has_upper, password_has_symbols)
        specs = f'U: {contains_upper(password)}, S: {contains_symbol(password)}'
        print(f'{i} -> {password} ({specs})')
