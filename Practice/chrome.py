from selenium import webdriver
import time


class ChromeBrowser:

    def chrome(self):
        driver = webdriver.Chrome()
        driver.get('https://python.org')
        time.sleep(5)
        driver.close()


if __name__ == '__main__':
    obj = ChromeBrowser()
    obj.chrome()
