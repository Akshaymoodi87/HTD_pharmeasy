import pytest
from POM.medicine_page import MedicinePage
from library.excel_lib import Readexcel
import datetime


class TestMedicinePage:
    read_xl = Readexcel()
    data = read_xl.read_test_data()

    @pytest.mark.parametrize("pin, search, mobno", data)
    def test_medicine(self,init_driver, pin, search, mobno):
        driver = init_driver
        try:
            me = MedicinePage(driver)
            me.click_medicine()
            me.click_pincode()
            me.click_enter_pin(pin)
            me.click_submit()
            me.click_search(search)
            me.click_s_button()
            me.enter_dolo()
            me.select_qty()
            me.click_view_cart()
            me.click_add_delivery()
            me.click_enter_num(mobno)
            me.click_send_otp()
            me.click_continue()

        except BaseException:
            td = datetime.datetime.now()
            name = f"screenshot_{td.hour}_{td.minute}_{td.second}.png"
            path = r"C:\Users\Adithya M M\PycharmProjects\pharmeasy\screenshot"
            driver.save_screenshot(path + name)
