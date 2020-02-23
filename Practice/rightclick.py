from selenium import webdriver
from selenium.webdriver import ActionChains
import time

driver = webdriver.Firefox()

driver.get("https://www.amazon.in")

button = driver.find_element_by_xpath("//*[@id='nav-link-accountList']/span[1]")
# signin = driver.find_element_by_link_text("Sign in")

actions = ActionChains(driver)
actions.context_click(button).perform()