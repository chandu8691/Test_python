from selenium import webdriver
import time
driver= webdriver.Chrome(executable_path='C:\\Users\\kodiak\\Downloads\\chromedriver.exe')
driver.get("https://javascript.info/alert-prompt-confirm")
driver.find_element_by_xpath("//a[text()='Run the demo']").click()
time.sleep(5)
driver.switch_to.alert.send_keys("chandana")
driver.switch_to.alert.accept()
print(driver.switch_to.alert.text)
driver.switch_to.alert.accept()
driver.close()
