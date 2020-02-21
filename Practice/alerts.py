from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
driver = webdriver.Firefox()

driver.get("https://www.amazon.com/")

element = driver.find_element_by_xpath("//*[@id='icp-nav-flyout']/span").click()
# alt = Select(element)
# alt.select_by_visible_text("Português - PT - Tradução")
# element = driver.find_element_by_xpath("//*[@id='icp-nav-flyout']/span").click()
driver.find_element_by_name("LOP").click()
time.sleep(5)

driver.switch_to_alert().accept()
    9822