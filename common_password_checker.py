def check_password(password: str):
    with open('common-passwords.txt', 'r') as file:
        common_passwords: list[str] = file.read().splitlines()
        for i, common_password in enumerate(common_passwords, start=1):
            if password == common_password:
                print(f'{password}: ❌ (#{i})')
                return
            
        print(f'{password}: ✅ (Unique)')

def main():
    while True:
        user_password: str = input('Enter a password: ')
        if len(user_password) > 0:
            check_password(user_password)
            break
        else:
            print('The length of password should be greater than 0.')

if __name__ == '__main__':
    main()