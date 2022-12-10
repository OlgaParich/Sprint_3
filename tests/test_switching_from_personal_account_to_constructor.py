from locators import TestLocators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def test_switching_from_account_by_constructor(authorization):
    authorization.find_element(*TestLocators.BUTTON_PERSONAL_ACCOUNT_ON_HOME_PAGE).click()
    WebDriverWait(authorization, 3).until(
        expected_conditions.presence_of_element_located(TestLocators.WINDOW_PERSONAL_ACCOUNT))
    authorization.find_element(*TestLocators.BUTTON_CONSTRUCTOR_ON_HEADER).click()
    assert authorization.find_element(*TestLocators.WINDOW_CONSTRUCTOR)



def test_switching_from_account_by_logo(authorization):
    authorization.find_element(*TestLocators.BUTTON_PERSONAL_ACCOUNT_ON_HOME_PAGE).click()
    WebDriverWait(authorization, 3).until(
        expected_conditions.presence_of_element_located(TestLocators.WINDOW_PERSONAL_ACCOUNT))
    authorization.find_element(*TestLocators.LOGO_ON_HEADER).click()
    assert authorization.find_element(*TestLocators.WINDOW_CONSTRUCTOR)
