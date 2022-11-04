import xlrd
from library.config import Configuration


class Readexcel:
    def read_locators(self):
        # path = Configuration.LOCATORS_PATH
        wb = xlrd.open_workbook(Configuration.Test_data)
        ws = wb.sheet_by_name("locators")
        rows = ws.get_rows()
        header = next(rows)
        data = {}
        for row in rows:
            data[row[0].value] = (row[1].value, row[2].value)
        return data

    def read_test_data(self):
        path = Configuration.Test_data
        wb = xlrd.open_workbook(path)
        ws = wb.sheet_by_name("login")
        rows = ws.get_rows()
        header = next(rows)
        l_ = []
        for row in rows:
            l_.append((row[0].value, row[1].value, row[2].value))

        return l_


r = Readexcel()
data = r.read_test_data()
print(data)
