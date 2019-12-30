from selenium import webdriver

driver=webdriver.Chrome(executable_path='C:\\Users\\kodiak\\Downloads\\chromedriver.exe')
driver.get("https://www.google.com/")

driver.execute_script('window.open("https://www.amazon.com/","tab1")')
driver.switch_to.window('tab1')
driver.execute_script("window.scrollTo(500,document.body.scrollHeight)")



