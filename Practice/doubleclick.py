from selenium import webdriver
from selenium.webdriver import ActionChains
import time

driver = webdriver.Firefox()

driver.get("https://www.amazon.in")

mousehover = driver.find_element_by_xpath("//*[@id='nav-link-accountList']/span[1]")
signin = driver.find_element_by_link_text("Sign in")

actions = ActionChains(driver)

actions.move_to_element(mousehover).move_to_element(signin).click().perform()
element = driver.find_element_by_xpath("//*[@id='ap_email']").click()
actions.double_click(element).perform()

time.sleep(5)
driver.close()
