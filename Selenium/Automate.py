from selenium import webdriver
driver=webdriver.Chrome(executable_path='C:\\Users\\kodiak\\Downloads\\chromedriver.exe')
driver.get("")
# driver.maximize_window()
# driver.refresh()
# driver.minimize_window()
# driver.back()
# driver.forward()
# print("TITLE",driver.title())
# print("URL",driver.current_url())
# #driver.set_window_rect(x,y,w,h) #set x-axis,y-axis,height,width
# #driver.set_window_size() #
# driver.quit()
# cookie1={'name':'apple','value':'abc'}
# driver.add_cookie(cookie1)
# print(driver.get_cookie("apple"))


#automate Gmail
driver.find_element_by_id("identifierId").send_keys("chandu8691")
driver.find_element_by_xpath("//span[text()='Next']").click()
driver.implicitly_wait(10)
driver.find_element_by_name("password").send_keys("Chandu8691")
driver.implicitly_wait(10)
driver.find_element_by_xpath("//span[text()='Next']").click()


#automate orangeHRM page
# driver.find_element_by_id("txtUsername").send_keys("Admin")
# driver.find_element_by_id("txtPassword").send_keys("admin123")
# driver.find_element_by_id("btnLogin").click()
# driver.find_element_by_id("welcome").click()
# driver.find_element_by_link_text("Logout").click()



# driver.find_element_by_class_name("close-reveal-modal hide-mobile").click()
# # # driver.find_element_by_xpath("//div[@id='topnav_wrapper']/ul/li/span[contains(text(),'Sale')]").click()
# # # driver.find_element_by_xpath("//div[@id='topnav_wrapper']/ul/li/span[contains(text(),'Living')]").click()
# # # driver.find_element_by_xpath("//div[@id='topnav_wrapper']/ul/li/span[contains(text(),'Bedroom')]").click()
# # # driver.find_element_by_xpath("//div[@id='topnav_wrapper']/ul/li/span[contains(text(),'Dining')]").click()
# # # driver.find_element_by_xpath("//div[@id='topnav_wrapper']/ul/li/span[contains(text(),'Storage')]").click()
# # # driver.find_element_by_xpath("//div[@id='topnav_wrapper']/ul/li/span[contains(text(),'Study')]").click()
# driver.implicitly_wait(10)
# list=driver.find_elements_by_xpath("//div[@id='topnav_wrapper']/ul/li/span[@classname='topnav_itemname']")
# for i in list:
#      print(i.text)

