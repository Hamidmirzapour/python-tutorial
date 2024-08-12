import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

class Browser:
    def __init__(self):
        print('Starting up ...')
        self.browser = webdriver.Chrome()

    def open_page(self, url: str):
        print(f'Opening {url}')
        self.browser.get(url)

    def close_page(self):
        print('Closing browser ...')
        self.browser.close()


if __name__ == '__main__':
    browser = Browser()
    browser.open_page('https://python.org')
    time.sleep(5)
    browser.close_page()
    time.sleep(5)