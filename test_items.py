import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_add_to_basket_button(browser):
    browser.get(link)
    time.sleep(30)
    # result = WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.CLASS_NAME, "smart-hints__hint")))
    # find_button = browser.find_element(By.CLASS_NAME, "btn-add-to-baskе")
    find_button = browser(EC.visibility_of_element_located(By.CLASS_NAME, "btn-add-to-baskе"))
    assert find_button, "no button"
