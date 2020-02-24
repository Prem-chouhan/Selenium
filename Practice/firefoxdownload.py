from selenium import webdriver
from selenium.webdriver import ActionChains
import time

# fp = webdriver.FirefoxProfile()
#
# fp.set_preference("browser.helperApps.neverAsk.saveToDisk", "text/plain,application/pdf")
# fp.set_preference("browser.download.managershowWhenStarting", False)
# fp.set_preference("broewser.download.dir", "c:\Downloadedfiles")
# fp.set_preference("browser.download.folderList", 2)
# fp.set_preference("pdfjs.disabled", True)


fp = webdriver.FirefoxProfile()

fp.set_preference("browser.download.folderList", 2)
fp.set_preference("browser.download.manager.showWhenStarting", False)
fp.set_preference("browser.download.dir", os.getcwd())
fp.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/octet-stream")

driver = webdriver.Firefox()

driver.get("https://www.python.org/")

download = driver.find_element_by_xpath("//*[@id='downloads']/a")

actions = ActionChains(driver)

actions.move_to_element(download).perform()

driver.find_element_by_xpath("//*[@id='downloads']/ul/li[8]/div[2]/p[1]/a").click()

time.sleep(5)

driver.close()
