from selenium import webdriver
import time
driver= webdriver.Chrome(executable_path='C:\\Users\\kodiak\\Downloads\\chromedriver.exe')
driver.get("https://www.bluestone.com/")
driver.implicitly_wait(5)
driver.switch_to.frame("chat-widget")
time.sleep(5)
driver.find_element_by_xpath("//p[text()='CHAT with our experts !']").click()
time.sleep(5)

driver.switch_to.default_content()
