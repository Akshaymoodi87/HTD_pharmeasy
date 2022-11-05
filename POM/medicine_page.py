import time

from library.excel_lib import Readexcel
from library.config import Configuration


class MedicinePage:
    read_xl = Readexcel()
    medicine_locators = read_xl.read_locators()

    def __init__(self, driver):
        self.driver = driver

    def click_medicine(self):
        locator = self.medicine_locators["medicine"]
        self.driver.find_element(*locator).click()

    def click_pincode(self):
        locator = self.medicine_locators["pincode"]
        self.driver.find_element(*locator).click()

    def click_enter_pin(self, pin):
        if isinstance(pin, float):
            pin = (int(pin))
        assert len(str(pin)) == 6
        locator = self.medicine_locators["enter_pin"]
        self.driver.find_element(*locator).send_keys(pin)

    def click_submit(self):
        locator = self.medicine_locators["submit"]
        self.driver.find_element(*locator).click()
        time.sleep(4)

    def click_search(self, search):
        locator = self.medicine_locators["search"]
        self.driver.find_element(*locator).send_keys(search)
        time.sleep(4)

    def click_s_button(self):
        locator = self.medicine_locators["s_button"]
        self.driver.find_element(*locator).click()
        time.sleep(4)


    def enter_dolo(self):
        locator = self.medicine_locators["dolo"]
        self.driver.find_element(*locator).click()


    def select_qty(self):
        locator = self.medicine_locators["qty"]
        self.driver.find_element(*locator).click()

    def click_view_cart(self):
        locator = self.medicine_locators["view_cart"]
        self.driver.find_element(*locator).click()

    def click_add_delivery(self):
        locator = self.medicine_locators["add_delivery"]
        self.driver.find_element(*locator).click()

    def click_enter_num(self, mobno):
        if isinstance(mobno, float):
            mobno = int(mobno)
        locator = self.medicine_locators["enter_num"]
        self.driver.find_element(*locator).send_keys(mobno)

    def click_send_otp(self):
        locator = self.medicine_locators["send_otp"]
        self.driver.find_element(*locator).click()
        time.sleep(20)

    def click_continue(self):
        locator = self.medicine_locators["continue"]
        self.driver.find_element(*locator).click()
