import autoit
from selenium import webdriver
import time
driver=webdriver.Chrome(executable_path='C:\\Users\\kodiak\\Downloads\\chromedriver.exe')
driver.get("https://accounts.google.com/ServiceLogin/identifier?service=mail&passive=true&rm=false&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F%3Fogbl&scc=1&ltmpl=default&ltmplcache=2&emr=1&osid=1&flowName=GlifWebSignIn&flowEntry=AddSession")
driver.find_element_by_id("identifierId").send_keys("chandana.r@testyantra.com")
driver.find_element_by_xpath("//span[text()='Next']").click()
driver.implicitly_wait(10)
driver.find_element_by_name("password").send_keys("Chandu8691")
driver.implicitly_wait(10)
driver.find_element_by_xpath("//span[text()='Next']").click()
#g=driver.find_element_by_xpath("//span[text()='226']").text
driver.find_element_by_xpath("//div[text()='Compose']").click()
driver.find_element_by_xpath("//div[@class='a1 aaA aMZ']").click()
time.sleep(5)
autoit.win_wait("Open",3)
autoit.control_send("[CLASS:#32770]","Edit1","November.xlsx")
autoit.control_click("[CLASS:#32770]","Button1")



