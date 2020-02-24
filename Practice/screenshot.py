from selenium import webdriver

driver =webdriver.Firefox()

driver.get("https://www.amazon.com/")

# driver.save_screenshot("/home/admin-1/prem/pic.png")
driver.get_screenshot_as_file("/home/admin-1/prem/pic2.jpg")

driver.close()