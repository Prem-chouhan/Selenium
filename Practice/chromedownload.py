from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
import time
ChromeOptions = Options()

ChromeOptions.add_experimental_option("prefs", {"Default Directory": "/home/admin-1/prem"})
driver = webdriver.Chrome(chrome_options=ChromeOptions)

driver.get("https://www.python.org/")

download = driver.find_element_by_xpath("//*[@id='downloads']/a")

actions = ActionChains(driver)

actions.move_to_element(download).perform()

driver.find_element_by_xpath("//*[@id='downloads']/ul/li[8]/div[2]/p[1]/a").click()

time.sleep(5)

driver.close()
