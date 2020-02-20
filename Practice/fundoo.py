from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class FunDoo:

    def fundoo(self):
        driver = webdriver.Firefox()
        driver.get("http://127.0.0.1:8888/register")
        driver.implicitly_wait(5)

        element = driver.find_element_by_name("email").clear()
        element = driver.find_element_by_name("email")
        print(element.is_displayed())
        print(element.is_enabled())
        element.send_keys("premchouhan1995@gmail.com")
        element1 = driver.find_element_by_name("password").clear()
        element1 = driver.find_element_by_name("password")
        element1.send_keys("premsingh")
        continue_link = driver.find_element_by_link_text('Sign in').click()
        # driver.back()
        # driver.find_element_by_id("Register").click()
        element2 = driver.find_element_by_name("email")
        element2.send_keys("premchouhan007@gmail.com")
        element3 = driver.find_element_by_name("password")
        element3.send_keys("premsingh")
        driver.find_element_by_id("Login").click()
        # driver.back()
        time.sleep(5)
        # driver.switch_to.window("windows")
        # driver.switch_to.window("windows")
        # element.clear()
        # element1.clear()
        driver.close()


if __name__ == '__main__':
    obj = FunDoo()
    obj.fundoo()
