from selenium import webdriver

driver = webdriver.Firefox()

driver.get("https://www.irctc.co.in/nget/profile/user-registration")

# Method One
# driver.execute_script("window.scrollBy(0,1000)", "")

# Method 2
# flag = driver.find_element_by_xpath("//*[@id='divMain']/div/app-user-registration/div[2]/div/div[2]/div[4]/form/div[14]/div/div")
# driver.execute_script("arguments[0].scrollIntoView();", flag)

# Method 3
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")

driver.close()