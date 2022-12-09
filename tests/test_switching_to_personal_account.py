from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import TestLocators


def test_open_lk(authorization):
    authorization.find_element(*TestLocators.BUTTON_PERSONAL_ACCOUNT_ON_HOME_PAGE).click()
    WebDriverWait(authorization, 3).until(expected_conditions.presence_of_element_located((TestLocators.WINDOW_PERSONAL_ACCOUNT)))
    assert authorization.find_element(*TestLocators.ELEMENTS_PERSONAL_ACCOUNT)
