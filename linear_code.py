import time

from selenium import webdriver
c_path = r"C:\Users\Adithya M M\PycharmProjects\pharmeasy\drivers\chromedriver.exe"

option = webdriver.ChromeOptions()
option.add_argument("--disable-notifications")
driver = webdriver.Chrome(executable_path=c_path, options=option)

driver.maximize_window()
driver.get("https://pharmeasy.in/")
driver.implicitly_wait(30)
# driver.find_element("xpath", '//span[text()="Hello, Log in"]').click()
# time.sleep(1)
# driver.find_element("xpath", '//input[@type="tel"]').send_keys("9742428125")
# driver.find_element("xpath", '//span[text()="Send OTP"]').click()
# time.sleep(20)
# driver.find_element("xpath", '//span[text()="Continue"]').click()
# time.sleep(1)
driver.find_element("id", "0").click()
time.sleep(1)

driver.find_element("xpath", '//span[text()="Select Pincode"]').click()
time.sleep(1)

driver.find_element("xpath", '//input[@placeholder="Enter PIN Code"]').send_keys("577301")
time.sleep(1)

driver.find_element("xpath", '//button[@type="submit"]').click()
time.sleep(5)

driver.find_element("xpath", '//input[@placeholder="Search medicines/Healthcare products "]').send_keys("dolo")
time.sleep(1)

driver.find_element("xpath", '(//div[@aria-label="Search"])[2]').click()
time.sleep(1)

driver.find_element("xpath", '''//h1[contains(text(),'Dolo 650mg')]/../../..//button[@type="submit"]''').click()
time.sleep(1)

driver.find_element("xpath", '//li[@data-value="8"]').click()
time.sleep(1)

driver.find_element("xpath", '//span[text()="View Cart"]').click()
time.sleep(1)

driver.find_element("xpath", '//span[text()="Add Delivery Address"]').click()
time.sleep(1)

driver.find_element("xpath", '//input[@placeholder="Enter your phone number"]').send_keys("9008240114")

driver.find_element("xpath", '//button[text()="Send OTP"]').click()
time.sleep(20)

driver.find_element("xpath", '//button[text()="CONTINUE"]').click()

driver.find_element("xpath", '//button[text()="Save"]').click()

driver.find_element("xpath", '//span[text()="Proceed To Buy"]').click()

# driver.find_element("xpath", '//input[@placeholder="Full Name"]').send_keys("Akshay M M")
#
# driver.find_element("xpath", '//input[@name="flat"]').send_keys("Sri Malatesha Nilaya")
#
# driver.find_element("xpath", '//input[@name="ship-address"]').send_keys("O.S.M 5th cross, old town, Bhadravathi")
#
# driver.find_element("xpath", '//input[@name="ship-zip"]').send_keys("577301")
#
# driver.find_element("xpath", '(//div[@class="_3zgC6"])[1]').click()
#
# driver.find_element("xpath", '//div[@class="_1OXmH"]').click()


