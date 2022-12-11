import random
import string


def generator_pass():
    chars = string.ascii_letters + string.digits
    password = ''.join(random.choice(chars) for _ in range(6))
    return password


def generator_email():
    domain = ['ya.ru', 'mail.ru', 'gmail.com', 'icloud.com']
    chars_login = string.ascii_letters + string.digits
    email = ''.join(random.choice(chars_login) for _ in range(3, 10)) + '@' + random.choice(domain)
    return email
