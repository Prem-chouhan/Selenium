from selenium import webdriver

driver = webdriver.Firefox()

driver.get("https://www.toolsqa.com/automation-practice-table/")

rows = len(driver.find_elements_by_xpath("//*[@id='content']/table/thead/tr/th[1]"))
cols = len(driver.find_elements_by_xpath("//*[@id='content']/table/tbody/tr[1]/td[1]"))

print(rows, cols)

for r in range(2, rows+1):
    for c in range(1, cols+1):
        driver.find_element_by_xpath("//*[@id='content']/table/tbody/tr["+r+"]/th["+c+"]").text

