from selenium import webdriver


def invoke_browser(func):
    def inner(url):
        driver=webdriver.Chrome(executable_path='C:\\Users\\kodiak\\Downloads\\chromedriver.exe')
        driver.get(url)
        func(driver)
        driver.close()
    return inner

@invoke_browser
def test_1(driver):
    print("test case 1 executed")

@invoke_browser
def test_2(driver):
    try:
        driver.find_element_by_id("identifierId").send_keys("chandana")
        driver.find_element_by_xpath("//span[text()='Next']").click()
        print("test case 2 executed")
    except WrongMailID as e:
        print(e)

@invoke_browser
def test_3(driver):
    print("test case 3 executed")

@invoke_browser
def test_4(driver):
    print("test case 4 executed")

@invoke_browser
def test_5(driver):
    print("test case 5 executed")

test_1("https://www.facebook.com")
test_2("https://gmail.com")
test_3("https://www.youtube.com/")
test_4("https://opensource-demo.orangehrmlive.com/")
test_5("https://www.amazon.com/")
