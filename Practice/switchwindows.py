from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://www.irctc.co.in/nget/train-search")

driver.find_element_by_xpath("//*[@id='divMain']/div/app-main-page/div[1]/div/div[1]/div/div/div[1]/div/app-jp-input/div[5]/div[1]/a").click()

handles =driver.window_handles

for handle in handles:
    driver.switch_to.window(handle)
    print(driver.title)
    driver.close()

driver.quit()