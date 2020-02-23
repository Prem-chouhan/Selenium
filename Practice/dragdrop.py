from selenium import webdriver
from selenium.webdriver import ActionChains
import time

driver = webdriver.Firefox()

driver.get("http://testautomationpractice.blogspot.com/")

source = driver.find_element_by_xpath("//*[@id='draggable']")
destination = driver.find_element_by_xpath("//*[@id='droppable']")

actions = ActionChains(driver)

actions.drag_and_drop(source, destination)
time.sleep(5)
driver.close()