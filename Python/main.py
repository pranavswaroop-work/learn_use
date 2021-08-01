from selenium import webdriver

driver = webdriver.Chrome(executable_path='Python/driver/chromedriver.exe')

# Navigate to page
driver.get('https://google.com')
print(driver.title)

driver.quit()