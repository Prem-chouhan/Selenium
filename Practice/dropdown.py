from selenium import webdriver

from selenium.webdriver.support.ui import Select


class Dropdown:
    def dropdown(self):
        driver = webdriver.Chrome()

        driver.get("https://www.irctc.co.in/nget/profile/user-registration")
        element = driver.find_elements_by_tag_name("label")
        drp = Select(element)

        drp.select_by_index('English')


if __name__ == '__main__':
    d = Dropdown()
    d.dropdown()