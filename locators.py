from selenium.webdriver.common.by import By


class TestLocators:
    BUTTON_LOG_IN_ON_HOME_PAGE = By.XPATH, './/button[text() = "Войти в аккаунт"]'  # "Войти в аккаунт" на главной
    BUTTON_PERSONAL_ACCOUNT_ON_HOME_PAGE = By.XPATH, './/a[@href = "/account"]'  # "Личный кабинет" на главной

    INPUT_EMAIL_ON_LOGIN_FORM = By.XPATH, './/input[@type="text"]'  # "Email" на форме входа
    INPUT_PASSWORD_ON_LOGIN_FORM = By.XPATH, './/input[@type="password"]'  # "Пароль" на форме входа
    BUTTON_LOG_IN_ON_LOGIN_FORM = By.XPATH, './/button[@class="button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa"]'  # "Войти" на форме входа
    LINK_REGISTER_ON_LOGIN_FORM = By.XPATH, './/a[@href="/register"]'  # "Зарегистироваться" на форме входа
    LINK_RECOVER_PASSWORD_ON_LOGIN_FORM = By.XPATH, './/a[@href="/forgot-password"]'  # "Восстановить пароль" на форме входа
    HEADER_ON_LOGIN_FORM = By.XPATH, './/h2[text()="Вход"]' # Заголовок на форме авторизации
    WINDOW_LOGIN_FORM = By.XPATH, './/div[@class = "Auth_login__3hAey"]' # Окно формы авторизации

    LINK_LOG_IN_ON_PASSWORD_RECOVERY_FORM = By.XPATH, './/a[@href = "/login"]'  # "Войти" на форме восстановления пароля
    LINK_LOG_IN_ON_REGISTRATION_FORM = By.XPATH, './/a[@href = "/login"]'  # "Войти" на форме регистрации

    INPUT_NAME_ON_REGISTRATION_FORM = By.XPATH, './/fieldset[@class = "Auth_fieldset__1QzWN mb-6"][1]//input'  # "Имя" на форме регистрации
    INPUT_EMAIL_ON_REGISTRATION_FORM = By.XPATH, "//label[text() = 'Email']/../input"  # "Email" на форме регистрации
    INPUT_PASSWORD_ON_REGISTRATION_FORM = By.XPATH, './/input[@type = "password"]'  # "Пароль" на форме регистрации
    BUTTON_REGISTER_ON_REGISTRATION_FORM = By.XPATH, './/button[@class = "button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa"]'  # "Зарегистрироваться" на форме регистрации
    ERROR_INCORRECT_PASSWORD = By.XPATH, './/fieldset//p[@class = "input__error text_type_main-default"]'  # Ошибка "Некорректный пароль"

    ELEMENTS_PERSONAL_ACCOUNT = By.XPATH, './/ul[@class = "Account_list__3KQQf mb-20"]'  # Меню в Личном кабинете
    WINDOW_PERSONAL_ACCOUNT = By.CLASS_NAME, 'Account_account__vgk_w'  # Окно Личного кабинета
    BUTTON_LOG_OUT_ON_PERSONAL_ACCOUNT = By.XPATH, './/button[text()="Выход"]'  # Кнопка выход в личном кабинете
