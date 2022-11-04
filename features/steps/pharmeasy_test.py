import time

from behave import *
from selenium import webdriver


@given('User should be able to launch the browser')
def open_browser(context):
    context.driver = webdriver.Chrome(r"C:\Users\Adithya M M\PycharmProjects\pharmeasy\drivers\chromedriver.exe")
    context.driver.maximize_window()
    context.driver.implicitly_wait(20)


@then('User should be able to enter homepage of pharmeasy application')
def launch_application(context):
    context.driver.get("https://pharmeasy.in/")


@when('User should be able to click on medicine module')
def medicine_module(context):
    context.driver.find_element("id", "0").click()


@when('User should be able to click on pincode')
def pincode(context):
    context.driver.find_element("xpath", '//span[text()="Select Pincode"]').click()


@then('User should be able to enter "{pincode}"')
def enter_pincode(context, pincode):
    context.driver.find_element("xpath", '//input[@placeholder="Enter PIN Code"]').send_keys(pincode)


@then('User should be able to click on submit')
def submit(context):
    context.driver.find_element("xpath", '//button[@type="submit"]').click()
    time.sleep(5)


@then('User should be able to search for "{medicine}"')
def search_medicine(context, medicine):
    context.driver.find_element("xpath", '//input[@placeholder="Search medicines/Healthcare products "]').send_keys(
        medicine)


@then('User is able to click on search button')
def click_on_search(context):
    context.driver.find_element("xpath", '(//div[@aria-label="Search"])[2]').click()


@then('User should be able to select the product')
def select_product(context):
    context.driver.find_element("xpath",
                                '''//h1[contains(text(),'Dolo 650mg')]/../../..//button[@type="submit"]''').click()


@then('User should be able to select quantity')
def select_qty(context):
    context.driver.find_element("xpath", '//li[@data-value="8"]').click()


@then('User is able to click on view cart')
def view_cart(context):
    context.driver.find_element("xpath", '//span[text()="View Cart"]').click()


@then('User is able to add delivery address')
def delivery_address(context):
    context.driver.find_element("xpath", '//span[text()="Add Delivery Address"]').click()


@then('User is able to login with "{mobile_number}"')
def login(context, mobile_number):
    context.driver.find_element("xpath", '//input[@placeholder="Enter your phone number"]').send_keys(mobile_number)


@then('User is able to click on send otp')
def send_otp(context):
    context.driver.find_element("xpath", '//button[text()="Send OTP"]').click()
    time.sleep(20)


@then('User should be able to click on continue')
def click_continue(context):
    context.driver.find_element("xpath", '//button[text()="CONTINUE"]').click()
    time.sleep(20)
    context.driver.close()


