from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time, smtplib, ssl

# Taking Input Data
#JiraUsername = input("Enter Jira Username : ") # Not Using for now
JiraPassword = input("Enter Jira Password : ")
EmailPassword = input("Enter Email Password: ")

#-> Creation of web driver in headless mode
options = Options()
options.headless = True
driver = webdriver.Chrome(executable_path='./Python/driver/chromedriver.exe',options = options)
"""
#-> Creation of web driver 
driver = webdriver.Chrome(executable_path='./Python/driver/chromedriver.exe')
"""
# Navigate to page
driver.get('https://spycloud.atlassian.net/jira/software/c/projects/SKP/boards/3')
print(driver.title)

# Login to the page
driver.find_element_by_id("username").send_keys("messagetopranav@gmail.com")
driver.find_element_by_id("login-submit").click()
time.sleep(10)
driver.find_element_by_id("password").click()
driver.find_element_by_id("password").send_keys(JiraPassword)
driver.find_element_by_id("login-submit").click()
time.sleep(10)
# Getting the number of the cards witht he class name
board = driver.find_elements_by_class_name("ghx-summary")
print("/n Total Number of cards in board -->>>>>>> /n ",len(board))

# Logout of the account
time.sleep(10)
driver.get('https://spycloud.atlassian.net/logout')
driver.find_element_by_id("logout-submit").click()
time.sleep(10)
driver.quit()

# Email Code
#Variables Required to send mail
port = 465
smtp_server_domain_name = "smtp.gmail.com"
sender_mail = "g.pranavswaroop@gmail.com"

# Code to send mail
ssl_context = ssl.create_default_context()
service = smtplib.SMTP_SSL(smtp_server_domain_name, port, context=ssl_context)
service.login(sender_mail, EmailPassword)
result = service.sendmail(sender_mail, "messagetopranav@gmail.com", "Subject : Total Number of cards in board -->>>>>>> " + str(len(board)))
service.quit()

