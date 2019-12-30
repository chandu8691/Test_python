from selenium import webdriver
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common import alert

driver=webdriver.Chrome(executable_path='C:\\Users\\kodiak\\Downloads\\chromedriver.exe')
#driver.get("https://accounts.google.com/signin/v2/identifier?service=mail&passive=true&rm=false&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&ss=1&scc=1&ltmpl=default&ltmplcache=2&emr=1&osid=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin")
# driver.get("https://in.ebay.com/")

# driver.find_element_by_id("identifierId").send_keys("chandana.r@testyantra.com")
# driver.find_element_by_xpath("//span[text()='Next']").click()
# driver.implicitly_wait(10)
# driver.find_element_by_name("password").send_keys("Chandu8691")
# driver.implicitly_wait(10)
# driver.find_element_by_xpath("//span[text()='Next']").click()
# g=driver.find_element_by_xpath("//span[text()='226']").text
# print(g)

# m=driver.find_element_by_xpath("//span[text()='cpanel@testyantra.com']").text
# print(m)
# a=driver.find_element_by_xpath("//h2[text()='[testyantra.com] Email configuration settings for “chandana.r@testyantra.com']").text
# print(a)
# driver.close()

# driver.find_element_by_xpath("//div[text()='Compose']").click
# driver.find_element_by_name("to").send_keys("chandu8691@gmail.com")
# driver.find_element_by_name("subjectbox").send_keys("TestMail")
# driver.find_element_by_xpath("//div[@class='Am Al editable LW-avf tS-tW']").send_keys("Hi")
# driver.find_element_by_xpath("//div[@class='bBf']").click()
# time.sleep(5)
# driver.find_element_by_xpath("//div[text()='Send']").click()


#ebay

# def search():
#
#     driver.find_element_by_name("_nkw").send_keys("Apple Phones")
#     driver.find_element_by_id("gh-btn").click()
# search()
#
# def product():
#         prod=driver.find_elements_by_xpath("//h3[@class='s-item__title']")
#         for i in prod:
#             print(i.text)
#         ele=prod[10]
#         print("10th element is",ele.text)
#
# product()


#Bluestone
# driver= webdriver.Chrome(executable_path='C:\\Users\\kodiak\\Downloads\\chromedriver.exe')
driver.get("https://www.bluestone.com/")
driver.implicitly_wait(10)
driver.maximize_window()
mousehover=driver.find_element_by_xpath("//a[text()='Rings ']")
a=ActionChains(driver)
a.move_to_element(mousehover).perform()
time.sleep(3)
driver.find_element_by_link_text("Diamond").click()
driver.find_elements_by_xpath("//span[text()='Price']").click()
driver.find_elements_by_xpath("//span[text()='20% off on diamond price']")

for i in lst:
    price=i.text
    price_1=price[3:]
    price_def.append(price_1)
driver.find_elements_by_xpath()



driver.close()
