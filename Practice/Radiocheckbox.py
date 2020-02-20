from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class RadioButton:

    def radio(self):
        driver = webdriver.Firefox()

        driver.get("https://www.irctc.co.in/nget/profile/user-registration")

        driver.find_element_by_id("M").click()

        time.sleep(5)  # waits for 5 seconds

        driver.close()


if __name__ == '__main__':
    obj = RadioButton()
    obj.radio()