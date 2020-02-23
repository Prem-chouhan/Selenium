from selenium import webdriver
from selenium.webdriver import ActionChains
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()

driver.get("http://testautomationpractice.blogspot.com/")

driver.switch_to_frame(0)

driver.find_element_by_xpath("//*[@id='RESULT_FileUpload-10']").send_keys("/home/admin-1/Pictures/Wallpapers/0ea973e329cab30c0f97d0798d2fab27.jpg")

time.sleep(5)

driver.close()