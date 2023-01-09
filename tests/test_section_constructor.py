from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import TestLocators


def test_constructor_sauces(work_browser):
    WebDriverWait(work_browser, 3).until(
        expected_conditions.presence_of_element_located(TestLocators.WINDOW_CONSTRUCTOR))
    work_browser.find_element(*TestLocators.SELECTOR_SAUCES).click()
    assert work_browser.find_element(*TestLocators.CURRENT_SELECTOR_ON_CONSTRUCTOR).text == 'Соусы'


def test_constructor_fillings(work_browser):
    WebDriverWait(work_browser, 3).until(
        expected_conditions.presence_of_element_located(TestLocators.WINDOW_CONSTRUCTOR))
    work_browser.find_element(*TestLocators.SELECTOR_FILLINGS).click()
    assert work_browser.find_element(*TestLocators.CURRENT_SELECTOR_ON_CONSTRUCTOR).text == 'Начинки'


def test_constructor_buns(work_browser):
    WebDriverWait(work_browser, 3).until(
        expected_conditions.presence_of_element_located(TestLocators.WINDOW_CONSTRUCTOR))
    work_browser.find_element(*TestLocators.SELECTOR_SAUCES).click()
    work_browser.find_element(*TestLocators.SELECTOR_BUNS).click()
    assert work_browser.find_element(*TestLocators.CURRENT_SELECTOR_ON_CONSTRUCTOR).text == 'Булки'

