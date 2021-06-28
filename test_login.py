import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome(ChromeDriverManager().install())
    request.addfinalizer(wd.quit)
    return wd


def test_example(driver):
    driver.get("https://localhost/litecart/admin/")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("login").click()
    wait = WebDriverWait(driver, 10)
    wait.until(lambda dr: dr.current_url != "https://localhost/litecart/admin/login.php")