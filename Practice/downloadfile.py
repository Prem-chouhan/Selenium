from selenium import webdriver
from selenium.webdriver import ActionChains
import time

driver = webdriver.FirefoxProfile()

driver.set_preference("browser.helperApps.neverAsk.saveToDisk", "text/plain,application/pdf")
driver.set_preference("browser.download.managershowWhenStarting",False)
driver.set_preference("broewser.download.dir","c:\Downloadedfiles")
driver.set_preference("browser.download.folderList",2)
driver.set_preference("pdfjs.disabled",True)
driver1 = webdriver.Firefox(firefox_profile=driver)
driver1.get("https://www.python.org/")

download = driver1.find_element_by_xpath("//*[@id='downloads']/a")

actions = ActionChains(driver1)

actions.move_to_element(download).perform()

driver1.find_element_by_xpath("//*[@id='downloads']/ul/li[8]/div[2]/p[1]/a").click()

time.sleep(5)

driver1.close()
