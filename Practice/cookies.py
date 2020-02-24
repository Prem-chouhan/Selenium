from selenium import webdriver
import time
driver = webdriver.Firefox()

driver.get("https://www.amazon.com/")

cookies = driver.get_cookies()
print(len(cookies))
print(cookies)

cookies = {'name': 'Mycookies', 'value': '1234567890'}
driver.add_cookie(cookies)

cookies = driver.get_cookies()
print(len(cookies))

driver.delete_cookie('Mycookies')
time.sleep(5)
cookies = driver.get_cookies()
print(len(cookies))

driver.delete_all_cookies()
cookies = driver.get_cookies()
print(len(cookies))
driver.close()
