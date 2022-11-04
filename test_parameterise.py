import re
import datetime

import xlrd
import pytest

from selenium import webdriver


class ReadExcel:

    def read_testdata(self):
        f_path = r"C:\Users\Adithya M M\PycharmProjects\pharmeasy\test_data\pharmeasy.xlsx"
        wb = xlrd.open_workbook(f_path)
        ws = wb.sheet_by_name("login")
        rows = ws.get_rows()
        header = next(rows)
        data = []
        for row in rows:
            element = (row[0].value)
            data.append(element)
        return data

    def read_locators(self):
        f_path = r"C:\Users\Adithya M M\PycharmProjects\pharmeasy\test_data\pharmeasy.xlsx"
        wb = xlrd.open_workbook(f_path)
        ws = wb.sheet_by_name("locators")
        rows = ws.get_rows()
        header = next(rows)

        d = {}
        for row in rows:
            d[row[0].value] = (row[1].value, row[2].value)

        return d


@pytest.fixture(params=["Chrome", "edge"])
def init_driver(request):

    browser = request.param

    if browser.lower() == "chrome":
        chrome_path = r"C:\Users\Adithya M M\PycharmProjects\pharmeasy\drivers\chromedriver.exe"
        driver = webdriver.Chrome(executable_path=chrome_path)

    else:
        edge_path = r"C:\Users\Adithya M M\PycharmProjects\pharmeasy\drivers\msedgedriver.exe"
        driver = webdriver.Edge(executable_path=edge_path)

    driver.get("https://pharmeasy.in/")
    driver.maximize_window()
    yield driver
    driver.close()

class MedicinePage:

    read_xl = ReadExcel()
    reg_locators = read_xl.read_locators()

    def __init__(self, driver):
        self.driver = driver

    def click_on_medicine(self):
        locator = self.reg_locators["medicine"]
        self.driver.find_element(*locator).click()

    def enter_pincode(self):
        locator = self.reg_locators["pincode"]
        self.driver.find_element(*locator).send_keys()

    def click_check(self):
        locator = self.reg_locators["enter pin"]
        self.driver.find_element(*locator).click()

    def submit(self):
        locator = self.reg_locators["submit"]
        self.driver.find_element(*locator).click()

    def search(self):
        locator = self.reg_locators["search"]
        self.driver.find_element(*locator).click()

    def search_for_product(self):
        locator = self.reg_locators["search"]
        self.driver.find_element(*locator).send_keys()

    def select_qty(self):
        locator = self.reg_locators["qty"]
        self.driver.find_element(*locator).click()


class TestRegisterPage:

    read_xl = ReadExcel()
    data = read_xl.read_testdata()

    @pytest.mark.parametrize("mobile_num", data)
    def test_registration(self, mobile_num, init_driver):
        driver = init_driver

        try:
            lp = MedicinePage(driver)
            lp.click_on_medicine()


        except BaseException as error_msg:
            td = datetime.datetime.now()
            name = f"screenshot_{td.hour}_{td.minute}_{td.second}.png"
            path = r"C:\Users\Adithya M M\PycharmProjects\pharmeasy\screenshot"
            driver.save_screenshot(path + name)
            raise error_msg

