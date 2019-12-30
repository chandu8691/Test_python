from selenium import webdriver
driver=webdriver.Chrome(executable_path='C:\\Users\\kodiak\\Downloads\\chromedriver.exe')
driver.get("https://www.netmeds.com/")
driver.find_element_by_id("search").send_keys("crosin 650mg Tablet 15's")
driver.find_element_by_class_name("iconSearch").click()
driver.find_element_by_xpath("//span[text()='ADD TO CART']").click()
driver.close()

