import pytest
from selenium import webdriver
from locators import TestLocators


@pytest.fixture
def authorization():
    driver = webdriver.Chrome()
    driver.get('https://stellarburgers.nomoreparties.site/')
    driver.find_element(*TestLocators.BUTTON_LOG_IN_ON_HOME_PAGE).click()
    driver.find_element(*TestLocators.INPUT_EMAIL_ON_LOGIN_FORM).send_keys('olgaparich5123@ya.ru')
    driver.find_element(*TestLocators.INPUT_PASSWORD_ON_LOGIN_FORM).send_keys('1234567')
    driver.find_element(*TestLocators.BUTTON_LOG_IN_ON_LOGIN_FORM).click()
    yield driver
    driver.quit()


@pytest.fixture
def work_browser():
    driver = webdriver.Chrome()
    driver.get('https://stellarburgers.nomoreparties.site/')
    yield driver
    driver.quit()
