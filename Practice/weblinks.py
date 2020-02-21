from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()

driver.get("https://www.amazon.com/")

links = driver.find_elements(By.TAG_NAME, "a")

print(len(links))

# for link in links:
#     print(link.text)
driver.find_element(By.LINK_TEXT, "Sign in").click()

driver.close()
