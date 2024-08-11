# pip install requests
from typing import Final
import requests

API_KEY: Final[str] = 'Your API KEY'
BASE_URL: Final = 'https://cutt.ly/api/api.php'


def shorten_link(full_link: str):
    payload: dict = {'key': API_KEY, 'short': full_link}
    try:
        request = requests.get(BASE_URL, params=payload)
        data: dict = request.json()

        if url_data := data.get('url'):
            if url_data['status'] == 7:
                short_link: str = url_data['shortLink']
                print(f'Link: {short_link}')
            else:
                print(f'Error Status Code: {url_data['status']}')
    except Exception as e:
        print(f'Something went wrong: {e}')


def main():
    input_link: str = input('Enter a link: ')
    shorten_link(input_link)

if __name__ == '__main__':
    main()
