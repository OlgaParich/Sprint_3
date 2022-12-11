from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import TestLocators


def test_log_in_button_on_home_page(authorization):
    WebDriverWait(authorization, 3).until(
        expected_conditions.presence_of_element_located(TestLocators.WINDOW_CONSTRUCTOR))
    assert authorization.find_element(*TestLocators.BUTTON_ON_HOME_PAGE).text == 'Оформить заказ'


def test_log_in_on_personal_account(work_browser):
    work_browser.find_element(*TestLocators.BUTTON_PERSONAL_ACCOUNT_ON_HOME_PAGE).click()
    work_browser.find_element(*TestLocators.INPUT_EMAIL_ON_LOGIN_FORM).send_keys('olgaparich5123@ya.ru')
    work_browser.find_element(*TestLocators.INPUT_PASSWORD_ON_LOGIN_FORM).send_keys('1234567')
    work_browser.find_element(*TestLocators.BUTTON_LOG_IN_ON_LOGIN_FORM).click()
    WebDriverWait(work_browser, 3).until(
        expected_conditions.presence_of_element_located(TestLocators.WINDOW_CONSTRUCTOR))
    assert work_browser.find_element(*TestLocators.BUTTON_ON_HOME_PAGE).text == 'Оформить заказ'


def test_log_in_on_registration_form(work_browser):
    work_browser.find_element(*TestLocators.BUTTON_ON_HOME_PAGE).click()
    work_browser.find_element(*TestLocators.LINK_REGISTER_ON_LOGIN_FORM).click()
    work_browser.find_element(*TestLocators.LINK_LOG_IN_ON_REGISTRATION_FORM).click()
    work_browser.find_element(*TestLocators.INPUT_EMAIL_ON_LOGIN_FORM).send_keys('olgaparich5123@ya.ru')
    work_browser.find_element(*TestLocators.INPUT_PASSWORD_ON_LOGIN_FORM).send_keys('1234567')
    work_browser.find_element(*TestLocators.BUTTON_LOG_IN_ON_LOGIN_FORM).click()
    WebDriverWait(work_browser, 3).until(
        expected_conditions.presence_of_element_located(TestLocators.WINDOW_CONSTRUCTOR))
    assert work_browser.find_element(*TestLocators.BUTTON_ON_HOME_PAGE).text == 'Оформить заказ'


def test_log_in_on_password_recovery_form(work_browser):
    work_browser.find_element(*TestLocators.BUTTON_ON_HOME_PAGE).click()
    work_browser.find_element(*TestLocators.LINK_RECOVER_PASSWORD_ON_LOGIN_FORM).click()
    work_browser.find_element(*TestLocators.LINK_LOG_IN_ON_PASSWORD_RECOVERY_FORM).click()
    work_browser.find_element(*TestLocators.INPUT_EMAIL_ON_LOGIN_FORM).send_keys('olgaparich5123@ya.ru')
    work_browser.find_element(*TestLocators.INPUT_PASSWORD_ON_LOGIN_FORM).send_keys('1234567')
    work_browser.find_element(*TestLocators.BUTTON_LOG_IN_ON_LOGIN_FORM).click()
    WebDriverWait(work_browser, 3).until(
        expected_conditions.presence_of_element_located(TestLocators.WINDOW_CONSTRUCTOR))
    assert work_browser.find_element(*TestLocators.BUTTON_ON_HOME_PAGE).text == 'Оформить заказ'
