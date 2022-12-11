from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators import TestLocators


def test_registrations(work_browser):
    work_browser.find_element(*TestLocators.BUTTON_ON_HOME_PAGE).click()
    work_browser.find_element(*TestLocators.LINK_REGISTER_ON_LOGIN_FORM).click()
    work_browser.find_element(*TestLocators.INPUT_NAME_ON_REGISTRATION_FORM).send_keys('Ololo')
    work_browser.find_element(*TestLocators.INPUT_EMAIL_ON_REGISTRATION_FORM).send_keys('ololo6@ya.ru')
    work_browser.find_element(*TestLocators.INPUT_PASSWORD_ON_REGISTRATION_FORM).send_keys('123456')
    work_browser.find_element(*TestLocators.BUTTON_REGISTER_ON_REGISTRATION_FORM).click()
    WebDriverWait(work_browser, 3).until(
        expected_conditions.presence_of_element_located(TestLocators.HEADER_ON_LOGIN_FORM))
    assert work_browser.find_element(*TestLocators.HEADER_ON_LOGIN_FORM)


def test_incorrect_password(work_browser):
    work_browser.find_element(*TestLocators.BUTTON_ON_HOME_PAGE).click()
    work_browser.find_element(*TestLocators.LINK_REGISTER_ON_LOGIN_FORM).click()
    work_browser.find_element(*TestLocators.INPUT_NAME_ON_REGISTRATION_FORM).send_keys('Ololo')
    work_browser.find_element(*TestLocators.INPUT_EMAIL_ON_REGISTRATION_FORM).send_keys('ololo@ya.ru')
    work_browser.find_element(*TestLocators.INPUT_PASSWORD_ON_REGISTRATION_FORM).send_keys('123')
    work_browser.find_element(*TestLocators.BUTTON_REGISTER_ON_REGISTRATION_FORM).click()
    assert work_browser.find_element(*TestLocators.ERROR_INCORRECT_PASSWORD).text == 'Некорректный пароль'
