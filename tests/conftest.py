import pytest
from selenium import webdriver
from library.config import Configuration

@pytest.fixture(params=["chrome", "edge"])
def init_driver(request):
    browser = request.param

    if browser.lower() == "chrome":
        driver = webdriver.Chrome(executable_path=Configuration.CHROME_PATH)

    else:
        driver = webdriver.Edge(executable_path=Configuration.EDGE_PATH)

    driver.get(Configuration.URL)
    driver.maximize_window()
    driver.implicitly_wait(30)
    yield driver
    driver.close()
