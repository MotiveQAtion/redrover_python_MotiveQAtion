# import time
# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
#
#
# with webdriver.Chrome(ChromeDriverManager().install()) as driver:
#     driver.get("https://stepik.org/course/104774")
#     time.sleep(5)

# Или
# import time
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
#
# Устанавливаем драйвер через Service
# service = Service(ChromeDriverManager().install())
#
# with webdriver.Chrome(service=service) as driver:
#     driver.get("https://stepik.org/course/104774")
#     time.sleep(5)

#Или

# import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.os_manager import ChromeType
from selenium.webdriver.chrome.service import Service as ChromiumService

# with webdriver.Chrome(service=ChromiumService(ChromeDriverManager().install())) as driver:
#     driver.get("https://stepik.org/course/104774")
#     time.sleep(5)


from selenium import webdriver
from selenium.webdriver.common.by import By

# url = 'http://parsinger.ru/selenium/3/3.html'
# with webdriver.Chrome() as browser:
#     browser.get(url)
#     link = browser.find_element(By.CLASS_NAME, 'text')
#     # print(type(link))
#     print(link)


# URL веб-страницы для парсинга
# url = 'http://parsinger.ru/selenium/3/3.html'
#
# # Инициализируем драйвер Chrome
# with webdriver.Chrome() as browser:
#     # Открываем веб-страницу по заданному URL
#     browser.get(url)
#
#     # Используем метод .find_elements() для поиска всех элементов, соответствующих нашему XPath
#     p_elements = browser.find_elements(By.XPATH, "//div[@class='text']/p[2]")
#
#     # Проходимся по списку найденных элементов и выводим их текст
#     for i, p_element in enumerate(p_elements):
#         print(f"Текст второго p тега в {i + 1}-м div с классом 'text': {p_element.text}")

#1 Мастер заполнения форм

# with webdriver.Chrome() as browser:
#     browser.get('https://parsinger.ru/selenium/1/1.html')
#     input_form = browser.find_elements(By.CLASS_NAME, 'form')
#     for i in input_form:
#         i.send_keys('Text')
#     button = browser.find_element(By.CLASS_NAME, 'btn').click()
#     print(button)
#     time.sleep(5)

#2 Охотник за Сокровищами

# with webdriver.Chrome() as browser:
#     browser.get('https://parsinger.ru/selenium/2/2.html')
#     link = browser.find_element(By.PARTIAL_LINK_TEXT, '16243162441624')
#     link.click()
#     time.sleep(5)
#
#     result = browser.find_element(By.ID, 'result').text
#     print(result)

#3 Кодекс Охотников за Цифрами

# with webdriver.Chrome() as browser:
#     browser.get('https://parsinger.ru/selenium/3/3.html')
#     find_text = browser.find_elements(By.TAG_NAME, 'p')
#     counter = 0
#     # for i in find_text:
#     #     counter += int(i.text)
#     # print(counter)
#
#     l = []
#     for i in find_text:
#         l.append(int(i.text))
#     print(l)

#4 Поход за сокровищами в Цифровом Лабиринте

# with webdriver.Chrome() as browser:
#     browser.get('https://parsinger.ru/selenium/3/3.html')
#     find_item = browser.find_elements(By.XPATH, "//div[@class='text']/p[2]")
#     counter = 0
#     for i in find_item:
#         counter += int(i.text)
#     print(counter)


#5 Операция кодовый замок

# with webdriver.Chrome() as browser:
#     browser.get('https://parsinger.ru/selenium/4/4.html')
#     find_checkboxes = browser.find_elements(By.CLASS_NAME, 'check')
#     for i in find_checkboxes:
#         i.click()
#
#     find_button = browser.find_element(By.CLASS_NAME, 'btn').click()
#     result = browser.find_element(By.ID, 'result').text
#
#     print(result)


#6 Кодовая Одиссея
# with webdriver.Chrome() as browser:
#     browser.get('https://parsinger.ru/selenium/5/5.html')
#
#     numbers = [1, 2, 3, 4, 8, 9, 11, 12, 13, 14, 15, 16, 17, 22, 23, 28, 29, 33, 34, 38,
#                39, 43, 44, 48, 49, 51, 52, 53, 54, 55, 56, 57, 58, 61, 62, 63, 64, 68, 69, 73,
#                74, 78, 79, 83, 84, 88, 89, 91, 92, 97, 98, 101, 104, 108, 109, 113, 114, 118,
#                119, 123, 124, 128, 129, 131, 132, 137, 138, 140, 141, 144, 145, 148, 149, 153,
#                154, 158, 159, 163, 164, 165, 168, 169, 171, 172, 177, 178, 180, 181, 184, 185,
#                187, 188, 189, 190, 192, 193, 194, 195, 197, 198, 199, 200, 204, 205, 206, 207,
#                208, 209, 211, 212, 217, 218, 220, 221, 224, 225, 227, 228, 229, 230, 232, 233,
#                234, 235, 237, 238, 239, 240, 245, 246, 247, 248, 249, 251, 252, 253, 254, 255,
#                256, 257, 258, 260, 261, 264, 265, 268, 269, 273, 274, 278, 279, 288, 289, 291,
#                292, 293, 294, 295, 296, 297, 300, 301, 302, 303, 304, 305, 308, 309, 313, 314,
#                318, 319, 328, 329, 331, 332, 339, 340, 341, 342, 343, 344, 345, 346, 348, 349,
#                353, 354, 358, 359, 368, 369, 371, 372, 379, 380, 385, 386, 408, 409, 411, 412,
#                419, 420, 425, 426, 428, 429, 433, 434, 438, 439, 444, 445, 446, 447, 448, 451,
#                452, 459, 460, 465, 466, 467, 468, 469, 470, 472, 473, 474, 475, 477, 478, 479,
#                480, 485, 486, 487, 488, 491, 492, 499, 500, 505, 506, 508, 509, 513, 514, 518, 519]
#
#     checkboxes = browser.find_elements(By.CLASS_NAME, 'check')
#     for i in checkboxes:
#         if int(i.get_attribute('value')) in numbers:
#                 i.click()
#     browser.find_element(By.CLASS_NAME, 'btn').click()
#     result = browser.find_element(By.ID, 'result').text
#
# print(result)


#7 Операция "Выпадающие списки"


# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# with webdriver.Chrome() as browser:
#     browser.get('https://parsinger.ru/selenium/7/7.html')
#     g = browser.find_elements(By.TAG_NAME, 'option')
#
#     counter = 0
#     for i in g:
#         counter += int(i.text)
#     print(counter)
#
#     browser.find_element(By.ID, 'input_result').send_keys(str(counter))
#     browser.find_element(By.ID, 'sendbutton').click()
#     result = browser.find_element(By.ID, 'result').text
#
#     print(result)

#8 Миссия "Загадочный След"

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import Select
#
# # Создание объекта ChromeOptions для дополнительных настроек браузера
# options_chrome = webdriver.ChromeOptions()
#
# # Добавление аргумента '--headless' для запуска браузера в фоновом режиме
# # options_chrome.add_argument('--headless')
# options_chrome.add_argument('user-data-dir=C:\\Users\\aev32\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 4')
#
# with webdriver.Chrome(options=options_chrome) as browser:
#     browser.get('https://parsinger.ru/selenium/6/6.html')
#     text = browser.find_element(By.ID, 'text_box').text
#     text1 = eval(text)
#     print(text1)
#
#     options = browser.find_elements(By.TAG_NAME, 'option')
#     for i in options:
#         if i.text == str(text1):
#             x = i.get_attribute('value')
#
#     select = Select(browser.find_element(By.ID, 'selectId'))
#
#     select.select_by_value(x)
#
#     browser.find_element(By.ID, 'sendbutton').click()
#     result = browser.find_element(By.ID, 'result').text
#     time.sleep(10)
#     print(result)


"""Перенос профиля с основного браузера Chrome в браузер под управлением Selenium"""

# import time
# from selenium import webdriver
#
# # Задаем опции для Chrome
# options_chrome = webdriver.ChromeOptions()
# # Указываем путь к профилю пользователя
# options_chrome.add_argument('user-data-dir=C:\\Users\\aev32\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 4')
#
# # Инициализируем драйвер с указанными опциями
# with webdriver.Chrome(options=options_chrome) as browser:
#     url = 'https://yandex.ru/'
#     browser.get(url)  # Открываем страницу
#     time.sleep(10)  # Даем время на загрузку страницы


"""Cookies"""

# from pprint import pprint
# from selenium import webdriver
#
# with webdriver.Chrome() as webdriver:
#     webdriver.get('https://ya.ru/')
#     cookies = webdriver.get_cookies()
#     pprint(cookies)


"""Добавление cookie"""

# import time
# from pprint import pprint
# from selenium import webdriver
#
# cookie_dict = {
#     'name': 'any_name_cookie',    # Любое имя для cookie
#     'value': 'any_value_cookie',  # Любое значение для cookie
#     'expiry': 2_000_000_000,      # Время жизни cookie в секундах
#     'path': '/',                  # Директория на сервере дял которой будут доступны cookie
#     'domain': 'parsinger.ru',     # Информация о домене и поддомене для которых доступны cookie
#     'secure': True,  # or False   # Сигнал браузера о том что передать cookie только по защищённому HTTPS
#     'httpOnly': True,  # or False # Ограничивает достук к cookie по средствам API
#     'sameSite': 'Strict',  # or lax or none # Ограничение на передачу cookie между сайтами
# }
#
# with webdriver.Chrome() as webdriver:
#     webdriver.get('https://parsinger.ru/methods/4/index.html')
#     webdriver.add_cookie(cookie_dict)
#     pprint(webdriver.get_cookies())
#     time.sleep(100)


"""Задачи по материалу 5.6"""



#Задача 5.6.1
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# with webdriver.Chrome() as browser:
#     browser.get('https://parsinger.ru/methods/1/index.html')
#
#     result = browser.find_element(By.ID, 'result').text
#
#     while result == "refresh page":
#         browser.refresh()
#         result = browser.find_element(By.ID, 'result').text
#
#         if result != "refresh page":
#         # if result == int:
#             print(result)


#Задача 5.6.2

# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# with webdriver.Chrome() as browser:
#     browser.get('https://parsinger.ru/selenium/5.5/1/1.html')
#
#     empty_fields = browser.find_elements(By.CLASS_NAME, 'text-field')
#
#     for i in empty_fields:
#         i.clear()
#
#     button = browser.find_element(By.ID, 'checkButton').click()
#     alert = browser.switch_to.alert.text
#     print(alert)
#     time.sleep(3)

#Здача 5.6.3

# from selenium import webdriver
#
# with webdriver.Chrome() as browser:
#     browser.get('https://parsinger.ru/methods/3/index.html')
#
#     time.sleep(2)
#
#     cookies = browser.get_cookies()
#     sum_cookies = 0
#     for cookie in cookies:
#         # Проверяем, является ли число, стоящее в конце имени cookie, четным
#         # Разделяем имя cookie по символу '_', берем последний элемент и проверяем остаток от деления на 2
#         if int(cookie['name'].rsplit('_', 1)[-1]) % 2 == 0:
#             # Если условие выполняется, добавляем значение cookie к сумме
#             sum_cookies += int(cookie['value'])
#     print(sum_cookies)


#Задача 5.6.4

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
#
# with webdriver.Chrome() as browser:
#     browser.get('https://parsinger.ru/selenium/5.5/2/1.html')
#     all_fields = browser.find_elements(By.CLASS_NAME, 'text-field')
#     for field in all_fields:
#         if not field.get_attribute('disabled'):
#             field.clear()
#     button = browser.find_element(By.ID, 'checkButton').click()
#     alert = browser.switch_to.alert.text
#     time.sleep(3)
#     print(alert)


#Задача 5.6.5

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
#
# with webdriver.Chrome() as browser:
#     browser.get('https://parsinger.ru/methods/5/index.html')
#     # l_href = [item.get_attribute('href') for item in browser.find_elements(By.TAG_NAME, 'a')]
#     l_href = []
#     elements = browser.find_elements(By.TAG_NAME, 'a')  # Получаем все элементы <a>
#
#     for item in elements:
#         href = item.get_attribute('href')  # Извлекаем атрибут 'href' из элемента
#         l_href.append(href)  # Добавляем значение в список
#     # Инициализируем переменные для хранения максимального значения expiry и соответствующего результата
#     expiry = 0
#     result = 0
#
# # Проходим по каждой ссылке в списке
#     for link in l_href:
#         # Переходим на страницу по текущей ссылке
#         browser.get(link)
#         # Получаем все cookies, установленные на текущей странице
#         cookies = browser.get_cookies()
#         # Проверяем каждый cookie
#         for key in cookies:
#             # Сравниваем значение 'expiry' текущего cookie с сохраненным максимальным значением
#             if key['expiry'] > expiry:
#                 # Если 'expiry' больше, обновляем переменную result, взяв текст элемента с ID 'result'
#                 result = browser.find_element(By.ID, 'result').text
#                 # Обновляем максимальное значение 'expiry'
#                 expiry = key['expiry']
#
#     # Выводим результат
#     print(result)
#     print(expiry)


#Задача 5.6.6 - Эта задача без кода


#Задача 5.6.7

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
#
# with webdriver.Chrome() as browser:
#     browser.get('https://parsinger.ru/scroll/4/index.html')
#     buttons = browser.find_elements(By.CLASS_NAME, 'btn')
#
#     # Инициализируем переменную для хранения суммы результатов
#     result_sum = 0
#
#     for btn in buttons:
#         browser.execute_script("return arguments[0].scrollIntoView(true);", btn)
#
#         btn.click()
#         # Получаем значение элемента с ID 'result' и добавляем его к сумме
#         result_sum += int(browser.find_element(By.ID, 'result').text)
#
#         # Выводим итоговую сумму
#     print(result_sum)


#Задача 5.6.8

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
#
# with webdriver.Chrome() as browser:
#     browser.get('https://parsinger.ru/selenium/5.5/3/1.html')
#     # Находим все элементы с классом 'parent' на странице
#     elements = browser.find_elements(By.CLASS_NAME, 'parent')
#     result_sum = 0
#     # Проходим по каждому элементу (блоку) в списке
#     for box in elements:
#         # Проверяем, выбран ли чекбокс в данном блоке
#         if box.find_element(By.CLASS_NAME, 'checkbox').is_selected():
#             # Если чекбокс выбран, извлекаем текст из элемента <textarea> и добавляем его к сумме
#             result_sum += int(box.find_element(By.TAG_NAME, 'textarea').text)
#
#     # Выводим итоговую сумму
#     print(result_sum)


#Задача 5.6.9

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
#
# with webdriver.Chrome() as browser:
#     browser.get('https://parsinger.ru/selenium/5.5/4/1.html')
#     elements = browser.find_elements(By.CLASS_NAME, 'parent')

""" Проходим по каждому элементу (блоку) в списке XPATH"""
    # for box in elements:
    #     # Извлекаем текст из <textarea> с атрибутом color="gray"
    #     num = box.find_element(By.XPATH, './/textarea[@color="gray"]').text
    #     # Очищаем содержимое <textarea> с атрибутом color="gray"
    #     box.find_element(By.XPATH, './/textarea[@color="gray"]').clear()
    #     # Вставляем извлеченный текст в <textarea> с атрибутом color="blue"
    #     box.find_element(By.XPATH, './/textarea[@color="blue"]').send_keys(num)
    #     # Нажимаем на кнопку внутри текущего блока
    #     box.find_element(By.TAG_NAME, 'button').click()
    #
    # # Нажимаем на кнопку с ID 'checkAll' после обработки всех блоков
    # browser.find_element(By.ID, 'checkAll').click()
    #
    # # Выводим текст элемента с ID 'congrats'
    # print(browser.find_element(By.ID, 'congrats').text)


""" Проходим по каждому элементу (блоку) в списке CSS_SELECTOR"""
    # for box in elements:
    #     # Извлекаем текст из <textarea> с атрибутом color="gray"
    #     num = box.find_element(By.CSS_SELECTOR, 'textarea[color="gray"]').text
    #     # Очищаем содержимое <textarea> с атрибутом color="gray"
    #     box.find_element(By.CSS_SELECTOR, 'textarea[color="gray"]').clear()
    #     # Вставляем извлеченный текст в <textarea> с атрибутом color="blue"
    #     box.find_element(By.CSS_SELECTOR, 'textarea[color="blue"]').send_keys(num)
    #     # Нажимаем на кнопку внутри текущего блока
    #     box.find_element(By.TAG_NAME, 'button').click()
    #
    # # Нажимаем на кнопку с ID 'checkAll' после обработки всех блоков
    # browser.find_element(By.ID, 'checkAll').click()
    #
    # # Выводим текст элемента с ID 'congrats'
    # print(browser.find_element(By.ID, 'congrats').text)


#Задача 5.6.10

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import Select
# import time
#
# # Создаем объект настроек для Chrome
# options_chrome = webdriver.ChromeOptions()
# # Добавляем аргумент для запуска браузера в фоновом режиме (без графического интерфейса)
# options_chrome.add_argument('--headless=new')
#
# with webdriver.Chrome(options=options_chrome) as browser:
#     # Загрузка тестовой страницы
#     browser.get('https://parsinger.ru/selenium/5.5/5/1.html')
#     # browser.get('https://parsinger.ru/selenium/5.5/5/test/test.html')
#     # Находим элементы-контейнеры
#     elements = browser.find_elements(By.XPATH, '//div[contains(@style, "width: 100%")]')
#
#     for d in elements:
#         # Извлекаем цвет из <span>
#         color = d.find_element(By.TAG_NAME, 'span').text
#         # Находим выпадающий список и выбираем значение
#         dropdown = d.find_element(By.TAG_NAME, 'select')
#         select = Select(dropdown)
#         select.select_by_value(color)
#         # Нажимаем на кнопку с соответствующим data-hex
#         find_button = d.find_element(By.XPATH, f'.//button[@data-hex="{color}"]')
#         find_button.click()
#         # Ставим галочку в чекбоксе
#         checkbox = d.find_element(By.XPATH, './/input[@type="checkbox"]').click()
#         # Вводим цвет в текстовое поле
#         input_field = d.find_element(By.XPATH, './/input[@type="text"]').send_keys(color)
#         # Нажимаем кнопку "Проверить"
#         d.find_element(By.XPATH, "//button[text()='Проверить']").click()
#
#     # Нажимаем на кнопку "Проверить все элементы" после обработки всех контейнеров
#     browser.find_element(By.XPATH, "//button[text()='Проверить все элементы']").click()
#
#     # Ожидаем появления алерта
#     time.sleep(2)  # Небольшая задержка для гарантии, что алерт появился
#
#     # Получаем текст из алерта и распечатываем
#     alert = browser.switch_to.alert
#     alert_text = alert.text
#     print("Текст из алерта:", alert_text)
#
#     # Закрываем алерт
#     alert.accept()


#Задача 5.6.11

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
#
# # Создаем объект настроек для Chrome
# options_chrome = webdriver.ChromeOptions()
# # Добавляем аргумент для запуска браузера в фоновом режиме (без графического интерфейса)
# options_chrome.add_argument('--headless=new')
# #
# with webdriver.Chrome(options=options_chrome) as browser:
#     browser.get('https://parsinger.ru/methods/3/index.html')
#
#     cookies = browser.get_cookies()
#     sum_cookies = 0
#     for cookie in cookies:
#         sum_cookies += int(cookie['value'])
#     print(sum_cookies)


##Задача 5.6.12

# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# # Настройки для браузера Chrome
# options_chrome = webdriver.ChromeOptions()
# # options_chrome.add_argument('--headless=new')  # Запускаем браузер в фоновом режиме (без GUI)
#
# # Список куки для добавления в браузер
# cookies_list = [{'name': 'KXIYO4xMrWh', 'value': 'ibyAZPfXAsPqptPaNyL'},
#                 {'name': '0OIJ4G4ZLzK', 'value': 'kJcPzQu5Jr8ELK'},
#                 {'name': 'O1C4sd3RK5udnZ6P', 'value': '4mYYxbfgnIvuip2ry58EQ'},
#                 {'name': 'AUZgaLJ4Y', 'value': 'FLSZvYrkf1E57YMUkdD'},
#                 {'name': '9PWJc0VXVtnXNcS5Tf', 'value': 'YQ2G4RayBoXSEqEgA3oXRN3FAvAMT'},
#                 {'name': 'pN2x6MDb', 'value': 'htbtD59XD3vCemHRCe9iUxV1smvXAIk5XOwuHnnmMB0'},
#                 {'name': 'AsqpQd', 'value': 'uNFFRiqeRrj25MwJajG4AxeKvCxKbHUSbbvzb3C'},
#                 {'name': '73PVEdwTk0txDp4L', 'value': 'DTniz3Fwj110H24dfZfd5JqqfEtN'},
#                 {'name': 'jZ1MwGy5z0L8ZW00U', 'value': 'sspfahNvfeo3zHWAIW0jdp2A9LyDbIm0'},
#                 {'name': 'aLRosjpBhYrZ0J69a', 'value': 'zcoXWv5L9Pz5kwGeyP5jlAQ'},
#                 {'name': '9LPCTyKTNmvBcnZ', 'value': 'GWBjw1Gosk4IKxuh5J2eu0ikgowOaZwP8FOm1ekKeQIxJDIXBy'},
#                 {'name': 'psH0h', 'value': 'wNAUmVlQwG6VK5TvDfryipzWeLXX46WDbXUd8yGrhrA3Hnc'},
#                 {'name': 'BULl3P', 'value': 'wefA0ljyA82kYpV1OoOixtAIp6xjmiQlS9SLeN'},
#                 {'name': '3bIJVJCylqgshRC9r1dH', 'value': '6Y6EZE5dttgx7rKzP881nAhRPE'},
#                 {'name': 'dBDhCzi6VO0', 'value': 'LKMcpZ6bEJy5IY352OMViznSP5OMqS9IgZB0YMv'},
#                 {'name': '6SGnnuoZ7v', 'value': '6asdYiIPBsMEdO0mQ9Jlq0mSMbJjfg'},
#                 {'name': '4dfAVZ1qZwijwYMUj', 'value': '3TOxOPelSdN6cK273'},
#                 {'name': 'RMOPZQILwFr3o637M', 'value': 'RZoaTFTdytqxB6sZhO4ebrhWlxjhMoQn8ZiObpdcGgH'},
#                 {'name': '08cQ7E3qHOOMk4uy1fLz', 'value': 'YfYkz9boRjDHLTahMuZcAJPzbjwTlRt1iNZzGl'},
#                 {'name': 'YT1NKf55egy', 'value': '3MSmfnklFY5TzvM8np4guMsJYtmdHmbyHiz3Vp6Rtk7r4GWhC'},
#                 {'name': 'cTKnm0a3H2euL46Ibi', 'value': 'HCZ0KYkidXfFowGinPuWG19cT79gEJC'},
#                 {'name': 'mvAz0P7Igjs2JY', 'value': '8O67zvSDHJx'},
#                 {'name': 'TzWXbWMvDBcKTo', 'value': 'dzwNYZCg4jpxKtpCeumwq0DO2KtGWLIHpQLOrzmGbXMC8G'},
#                 {'name': '1BMgyMHkzUemIEr', 'value': '08Sd1v8kQi6eB1FTs9qfjDkJ9UfKCLOFGtDgbOlu9v9iiuu'},
#                 {'name': 'Jig5voy', 'value': 'Pi4OA6hY21TeHlHyPMaMFHgY0BZRcQ9V0nXg'},
#                 {'name': '10wa7lhCoJXIzEYW5kQ', 'value': 'BFp4YeKWKVKXHTOesJLleaAelwYwPz51C95IYzd'},
#                 {'name': 'BqXt5D', 'value': 'n99ZSFFhseCs7aVjU31pYSJxqMgFYGfreFZl9ixb2NNHRBp'},
#                 {'name': 'GJunU5e1BEvfd', 'value': 'y5YFJ3hF9hG45G86MD9W9nRk61JMsh8rsmbFFrDoeJVUfyBvZ'},
#                 {'name': 'itFJBn79wksvZ15lc2', 'value': 'nXpdqpt0Po84uOuSU'},
#                 {'name': 'O5Q70eOB5ivJt5DZ', 'value': 'AZRr2ATREeF9HQR2opgF'},
#                 {'name': '6jBEUxI0a7x790m', 'value': 'comi8Mx5ig95NAiSO8'},
#                 {'name': 'KpVF7aIkav32LuqIDI', 'value': 'ik4furgLieyUawgJpttvHxWoXm2zO19'},
#                 {'name': 'OTRFyN', 'value': 'vlzV7Z97sWcJStZgDJiRjzIf'},
#                 {'name': 'hKLzMbgdIlUTAMYSEo', 'value': 'Tq2l0QJ3ekwxY3uaC8n2ln1nDMWhltFQm2TNaBefAAzk'},
#                 {'name': 'GJKNrAvRn', 'value': 'dByJXuSsAIz3Rnqa9BvU11okpnSydEZnkaqMQu9RoE'},
#                 {'name': 'AowB8Q3t74JHmXTGc1', 'value': '02JklRAtbsNNe'},
#                 {'name': 'xPpvKmo03bGBYrmqw', 'value': '7bf4FgaLKoj6YvGq4huLT5r9eCflo70QhI9gAPkMIuj4Bg'},
#                 {'name': '8UqFFBP3Dm0s6XM', 'value': 'kSZJPw6oTBwqG94q'},
#                 {'name': 'WeeXL7bKNWIZZkgX', 'value': 'ap3DPbBYqlfEOZ6'},
#                 {'name': 'fhdSevpxKUzledgGtbL4', 'value': 'v5I4A3PFOlN9zWPDkedlC2eLbMZ5cn3cf8'},
#                 {'name': '3H6lO', 'value': 'jxc9994fPQBKpnyr8aZBDZlMAolnxXh'},
#                 {'name': 'QVen8QnA1648g4Dm9p', 'value': 'RXNYpaUTJlD4xVIOm'},
#                 {'name': '3PxMnD9w', 'value': 'JC74xNLEc5ujZge7OmXj5EWk3hwdm4OH8FgF60D6pFl'},
#                 {'name': 'o8yY57CZSN', 'value': 'afO10rX663gaVttfSxeE70Gd22JKxwJAli7EhEdzkxxME'},
#                 {'name': 'UpAdf46rvxXW', 'value': 'Ft2FEQV71gLnG'},
#                 {'name': 'WRrpVIAkMKiZVxHt299', 'value': 'FC53hjqCGooNgV'},
#                 {'name': 'XHViH149aRl5', 'value': 'YbozZeoGCt3gO1kRMoLExcfCotBz'},
#                 {'name': 'yjNLzeR4k', 'value': 'Chd2mmuK7nxuVTi'},
#                 {'name': '5M4RGm', 'value': 'tj3HWN5mVpz9zgIie2ac2KHKIeABaou'},
#                 {'name': 'CcxIZZYgojDZpHnO9zJl', 'value': 'xLiql8yXUxULBG9w2snaMLI4FjSyX'},
#                 {'name': 'NScrEjcTmwo639PQqki', 'value': 'eOSFemtdjyphiPubTAzTICUhgw92By'},
#                 {'name': '9b5OpL5NrCpmtsE', 'value': 'VKdEIeX5ZNTghD6sq3qyjBHJaUuXfpQ7YnYb'},
#                 {'name': 'uyBoiSTHTtxV8Wszttb', 'value': 'SHEEfVcj1jNv3V1oqeT2wfEbWKZ0uJ2ljwv'},
#                 {'name': 'qR6AeEoEbQb1GYRj', 'value': 'mA66a177y8e6Nm7BlKBvpcUrM3fm6y4K'},
#                 {'name': 'l0Y9gn8MNtC', 'value': 'M1L2OUmAisn1c6DNB9mJfTHRM9V3HuXUAEGG8Zx'},
#                 {'name': 'L8m4GeWyECR', 'value': 'QuFfnWXebyrwwqXfVvAN2dbSisST8IgGyLggrVzTjaCeQ'},
#                 {'name': 'GxJSMQh9aZjFdhgjaAj', 'value': 'phOonlKiMt0xLDtvoB52TbATS1Ggm4Pv5lztk5vTNkXVqp'},
#                 {'name': 'GRE1eZ8D1bb', 'value': 'llpIP76V4S978YmQcfW'},
#                 {'name': 'dooT1cyS41bIWEB9c', 'value': 'ORu004k9aFl9FdS77Iz'},
#                 {'name': 'csjauyxnCpBySvkXTDzS', 'value': 'SJKqcIqWDbUJbxnHfD8jNJzYKb3Yp3TPIRDIpxCNB'},
#                 {'name': 'Y6CgAqWN8', 'value': 'qu0g6xEm0iJeTKM8NfOZUxP0XQaCtUfiTWHtQJ5soU5cpZ'},
#                 {'name': 'xxtL44KLbN60b5q', 'value': 'RSNFhhicL7pWpo3gvE3tJbHaIjU'},
#                 {'name': 'KcvqC30', 'value': '58IlGI646RMaGMYtL5XYqxFq8UaMwjPDNFNApAuDpUI9tMoM4t'},
#                 {'name': 'y761v6wZDo3V7O', 'value': '3i9iZjnZXdHlJxDz7ZrkPthYdI3PowS5yRomV0v8fR9WVco4'},
#                 {'name': 'Ixr7AetyC', 'value': 'lYRaNZAnoNHc9UZIoXI9E'},
#                 {'name': 'QIvvsr04T0JGVJE', 'value': 'tr6fE8moJI897w967QTmKojC730GdkKTUonevQbYsHQ71mi'},
#                 {'name': 'CBTq9zQjJx', 'value': 'z7BuIeFufYeZysVnrglrDJk8KW8UBWYt62'},
#                 {'name': '2ALhFQM7svECfgsSaiTa', 'value': 'VGMsulQVoobUe4m6w8dZGej8jFzSES3hzl9OG2csqpl'},
#                 {'name': '7VQixJTzu2H', 'value': 'jPnLpldHTFNgPCH1RUlmRQx7N58P7CQHajLYvGxho'},
#                 {'name': 'KdmUSh1SJH6M9', 'value': 'HPKIgmOBqq6Ln6QSPKedXuFpOoWhrOUzCxRMlcoJ2Gd0S7Hd'},
#                 {'name': 't6B9gl6QeGEDl1LW', 'value': 'kGs0hk4Pmeb83dBbuHTSzIVNcY0G4iucq73lkCMwt6Akv4w'},
#                 {'name': 'gcjmy3', 'value': 'QtB6duKOGc7eNc9MFwiOOaikXCYQg6dO4m66sJJxkRebKIKiR'},
#                 {'name': '2oBZU9j', 'value': '2U80qbFDpRElKTshedtaZ42OzYG48OQckEt2Zy9D7T'},
#                 {'name': 'g2tyy8erqS4E5pdSynCB', 'value': 'VN5zSYJpNHQC14FVl'},
#                 {'name': 'lLhLcbED3XAgAPaMp', 'value': 'tBUVWsfSNg0Iv4TLPAmBRm2m2nrWh'},
#                 {'name': 'iUfgKa7OX', 'value': 'GtyGoiA00RNiTgqvbXs78khbzQ7d0rh5xTk1aZK'},
#                 {'name': 'WQGGXKzZXvRXLC0', 'value': 'itGXA2mVtchzcqstP39BvfBvwh'},
#                 {'name': 'p37sYwX5mgtwXJl3yFBL', 'value': 'h20iY8XooVE'},
#                 {'name': 'tubsOLf', 'value': 'YGlaF0EEJrT1c5Z2HBAWnc1Q3an3Ob'},
#                 {'name': 'mg1Pr2NJJEnw2UkGFg', 'value': 'L48wovkYz32wa16iiswcgbA6JmyVoysUqjfm4i7'},
#                 {'name': 'V55E3ui8KHXybSDSSnoc', 'value': '7rhA8PSMZFy1aC8CQXbitOxY0qdUkDOUWijijIvlHhtB0q1'},
#                 {'name': 'AcWBQQy', 'value': 'zl1GXRHA3neBLCN8'},
#                 {'name': 'PtvgV4eJ21CrPE3xeH9', 'value': '1tU9KvLdq2uRNRKtA'},
#                 {'name': 'XjuSocgLwoMvFo8a', 'value': 'pvmx5A97Sad0U6d6i'},
#                 {'name': 'mMpdmPLcZEAZDzNyA8a2', 'value': 'WG6CrZ3zXfxN84hJXUKJq0ZroYditsADYplxwhkgXkUcZ'},
#                 {'name': 'tojhHp0ZlGrZ8Y3', 'value': 'fqpJvGkfQRT7ytNTU5KPum150MmcVR1nja0QIQRVEOPiNvT7Pg'},
#                 {'name': 'LDHgCR5PNoqYdffU5', 'value': '7a0tCBgGzylPTGUStOuNXORrRWwy03Upm2CvJX'},
#                 {'name': 'F4xcvPzuYYAvDrvDi', 'value': 'zQEpxlKpKprtwFbJyx0XYxFrlc8XP2RhRG'},
#                 {'name': 'fmnoi', 'value': 'yB9333KC4bP4SHUF90Kj7OC9QXz22WAZ3xtZxLi9'},
#                 {'name': 'TbGdmTkjcC52T7q', 'value': '2HCejTOfB98e30JMj3Pz9Ok9xLz5Y9lkaJaHoRF2vA5xq0i'},
#                 {'name': 'tg3vMrNIZHs', 'value': '2XRV99ShR8yc0bCe0QOuC9xd0A'},
#                 {'name': '8FaJo5TVO7TmoOI', 'value': 'bGYulAOS3ARzN3Rsyx9JJzu'},
#                 {'name': 'YLBwBAUCJ05p5fx2', 'value': 'Z8lGSb7AnZKVwlIqKgRIafpIfTVufj'},
#                 {'name': 'fpZCwfH', 'value': 'cqo4KOj8LSagd6VUhBrq6RJtUquwK7mJaDQsQb'},
#                 {'name': 'zjUiv081bH', 'value': 'LSJtgc56ylEJGMd1AhE9QcXudC8g'},
#                 {'name': 'yiWR1RtAnWH71I1', 'value': 'ruskXwdCQOfbfIgtKcetVb'},
#                 {'name': 'KMKvYURaBlIEmtyX', 'value': 'NFIzhI600J5QYN'},
#                 {'name': 'hbFS4sDwQh', 'value': 's4zWhushscPPDDFqT5tzPJqix0HMjjG'},
#                 {'name': 'b9wAAVSyw4V2LQ', 'value': 'SDkldbPnf6NjLZSxWZV7CpCW'},
#                 {'name': 'jFhFn0wPFRG', 'value': 'RYqOrD21ZN7aUeBXqISZ2afocnvvwd6hw3BXUj1wEm0mUO'}]
#
# # Используем контекстный менеджер для открытия браузера
# # with webdriver.Chrome(options=options_chrome) as browser:
# with webdriver.Chrome() as browser:
#     # Переходим на целевую страницу
#     browser.get('https://parsinger.ru/selenium/5.6/1/index.html')
#
#     # Инициализируем временные переменные для хранения информации о пользователе
#     temp_age_lang = {'name': '', 'age': 99, 'count_lang': 0}  # Максимально возможный возраст, чтобы проще сравнивать
#
#     # Проходим по каждому элементу из списка куков
#     for cookie in cookies_list:
#         browser.delete_all_cookies()  # Удаляем все куки перед добавлением новых
#         browser.add_cookie(cookie)  # Добавляем куки в браузер
#         browser.refresh()  # Обновляем страницу, чтобы применить куки
#
#         # Извлекаем информацию о пользователе с веб-страницы
#         name = browser.find_element(By.XPATH, '//span[@id="name"]').text[6:]  # Получаем имя
#         age = int(browser.find_element(By.XPATH, '//span[@id="age"]').text[5:])  # Получаем возраст и конвертируем в int
#         count_lang = len(
#             browser.find_element(By.XPATH, '//ul[@id="skillsList"]').text.split())  # Подсчитываем количество языков
#
#         # Сравниваем полученные данные с временными переменными
#         if age < temp_age_lang['age'] and count_lang > temp_age_lang['count_lang']:
#             temp_age_lang['name'] = name  # Сохраняем имя
#             temp_age_lang['age'] = age  # Сохраняем возраст
#             temp_age_lang['count_lang'] = count_lang  # Сохраняем количество языков
#             temp_age_lang['cookie_value'] = cookie['value']  # Сохраняем значение куки
#
#     # Выводим значение куки, соответствующее пользователю с наименьшим возрастом и наибольшим количеством языков
#     print(temp_age_lang['cookie_value'])


"""6. Скроллинг страниц"""

# import time
# from selenium import webdriver
#
# with webdriver.Chrome() as browser:
#     browser.get('http://parsinger.ru/scroll/1/')
#     browser.execute_script("window.scrollBy(0,50000)")
#     time.sleep(3)


#код, который прокрутит страницу в низ за 10 итераций.

# import time
# from selenium import webdriver
#
# with webdriver.Chrome() as browser:
#     browser.get('http://parsinger.ru/scroll/1/')
#     for i in range(10):
#         browser.execute_script("window.scrollBy(0,5000)")
#         time.sleep(2)


#Команда return document.body.scrollHeight вернёт значение высоты основного элемента на странице — body.

# import time
# from selenium import webdriver
#
# with webdriver.Chrome() as browser:
#     browser.get('http://parsinger.ru/scroll/1/')
#     height = browser.execute_script("return document.body.scrollHeight")
#     time.sleep(2)
#     print(height)


#Для вычисления высоты видимой области сайта используется скрипт.
# Код window.innerHeight используется для получения высоты, а window.innerWidth — для получения ширины видимой области.

# from selenium import webdriver
#
# with webdriver.Chrome() as browser:
#     browser.get('http://parsinger.ru/scroll/1/')
#     height = browser.execute_script("return window.innerHeight")
#     print(height)


# Если вам необходимо прокрутить страницу до самого низа, до последнего пикселя, одним из самых простых способов
# будет использование скрипта window.scrollTo(0, document.body.scrollHeight).

# import time
# from selenium import webdriver
#
# with webdriver.Chrome() as browser:
#     browser.get('http://parsinger.ru/scroll/1/')
#     browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#     time.sleep(2)


#симулируется нажатие клавиши TAB.

# import time
# from selenium.webdriver import Keys
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# with webdriver.Chrome() as browser:
#     browser.get('http://parsinger.ru/scroll/1/')
#     browser.find_element(By.TAG_NAME, 'input').send_keys(Keys.TAB)
#     time.sleep(3)


# import time
# from selenium.webdriver import Keys
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# with webdriver.Chrome() as browser:
#     browser.get('https://stepik.org/lesson/730646/step/1?unit=732177')
#     tags_input = browser.find_elements(By.TAG_NAME, 'input')
#
#     for input in tags_input:
#         input.send_keys(Keys.DOWN)
#         time.sleep(3)


#

# import time
# from selenium.webdriver import Keys
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# with webdriver.Chrome() as browser:
#     browser.get(r"https://parsinger.ru/selenium/5.7/3/index.html")
#
#     list_input = []      # Инициализируем пустой список для хранения обработанных элементов ввода
#     while True:          # Начинаем бесконечный цикл
#
#         # Ищем все элементы input на веб-странице и добавляем их в список input_tags
#         input_tags = [x for x in browser.find_elements(By.TAG_NAME, 'input')]
#
#         # Обходим каждый элемент input в списке
#         for tag_input in input_tags:
#             # Проверяем, не обрабатывали ли мы уже этот элемент ранее
#             if tag_input not in list_input:
#                 tag_input.send_keys(Keys.DOWN)     # Отправляем клавишу "Вниз"
#                 browser.execute_script("return arguments[0].scrollIntoView(true);", tag_input)
#                 tag_input.click()                  # Кликаем на элемент
#                 time.sleep(.3)
#                 list_input.append(tag_input)       # Добавляем элемент в список обработанных элементов


# Action Chains

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.action_chains import ActionChains
#
# # Инициализация драйвера
# driver = webdriver.Chrome()
#
# # Открыть веб-страницу (замените URL на ваш адрес)
# driver.get("https://parsinger.ru/selenium/5.7/2/index.html")
#
# # Найти элемент на странице с использованием локатора By
# draggable = driver.find_element(By.ID, "draggable")
#
# # Использование ActionChains для выполнения перетаскивания элемента
# actions = ActionChains(driver)
#
# # 1. Переместить блок влево на 100px
# actions.drag_and_drop_by_offset(draggable, -100, 0).perform()
#
# # 2. Переместить блок вниз на 100px
# actions.drag_and_drop_by_offset(draggable, 0, 100).perform()
#
# # 3. Переместить блок вправо на 100px
# actions.drag_and_drop_by_offset(draggable, 100, 0).perform()
#
# # 4. Переместить блок вверх на 100px
# actions.drag_and_drop_by_offset(draggable, 0, -100).perform()
#
# # Закрыть браузер после завершения
# driver.quit()


# Задача 6.5.1

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver import Keys
# import time
#
# # Создаем объект настроек для Chrome
# options_chrome = webdriver.ChromeOptions()
# # Добавляем аргумент для запуска браузера в фоновом режиме (без графического интерфейса)
# options_chrome.add_argument('--headless=new')
# #
# # Используем контекстный менеджер для открытия браузера
# with webdriver.Chrome() as browser:
#     # Переходим на целевую страницу
#     browser.get('https://parsinger.ru/scroll/2/index.html')
#     sum_num = 0
#
#     # Находим все блоки с классом 'item'
#     all_blocks = browser.find_elements(By.CLASS_NAME, 'item')
#     for block in all_blocks:
#         # Кликаем по чекбоксу внутри блока
#         # checkbox = block.find_element(By.CLASS_NAME, 'checkbox_class').click()
#         checkbox = block.find_element(By.CLASS_NAME, 'checkbox_class')
#         checkbox.send_keys(Keys.SPACE)
#         checkbox.send_keys(Keys.TAB)
#
#         # Получаем текст из <span> внутри блока и суммируем
#         span_text = block.find_element(By.TAG_NAME, 'span').text
#         if span_text:
#             sum_num += int(span_text)
#
#     print(sum_num)


# Задача 6.5.2

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver import Keys, ActionChains
# import time
#
# # options_chrome = webdriver.ChromeOptions()
# # options_chrome.add_argument('--headless=new')
# #
# # Используем контекстный менеджер для открытия браузера
# # with webdriver.Chrome(options=options_chrome) as browser:
# with webdriver.Chrome() as browser:
#     # Переходим на целевую страницу
#     browser.get('https://parsinger.ru/infiniti_scroll_1/')
#     time.sleep(3)
#
#     sum_num = 0
#     unique_numbers = set()  # Для хранения уникальных чисел
#
#     scroll_element = browser.find_element(By.ID, 'scroll-container')
#
#     while True:
#         actions = ActionChains(browser)
#         actions.click(scroll_element).key_down(Keys.PAGE_DOWN).perform()
#
#         # Ждем, чтобы дать странице время на подгруздку новых элементов
#         time.sleep(1)
#
#         nums_elements = scroll_element.find_elements(By.TAG_NAME, 'span')
#
#         for i in nums_elements:
#             num = i.text.strip() #Извлекается текст каждого элемента <span> и убираются лишние пробелы.
#             if num.isdigit() and num not in unique_numbers:  # Проверка на уникальность
#                 sum_num += int(num)
#                 unique_numbers.add(num)  # Добавление уникального числа в множество
#
#         # Проверяем, достигнут ли элемент с классом last-of-list
#         try:
#             last_of_list_element = scroll_element.find_element(By.CLASS_NAME, 'last-of-list')
#             if last_of_list_element.is_displayed():  # Если элемент виден, выходим из цикла
#                 print("Достигнут элемент 'last-of-list'. Завершение сбора данных.")
#                 break
#         except Exception:
#             pass  # Если элемент не найден, продолжаем
#
#     print("Сумма числовых значений:", sum_num)


#Задача 6.5.3

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver import Keys, ActionChains
# import time
#
# # options_chrome = webdriver.ChromeOptions()
# # options_chrome.add_argument('--headless=new')
# #
# # Используем контекстный менеджер для открытия браузера
# # with webdriver.Chrome(options=options_chrome) as browser:
# with webdriver.Chrome() as browser:
#     # Переходим на целевую страницу
#     browser.get('https://parsinger.ru/infiniti_scroll_2/')
#     time.sleep(1)
#
#     sum_num = 0
#     unique_numbers = set()
#
#     scroll_element = browser.find_element(By.ID, 'scroll-container')
#
#     while True:
#         actions = ActionChains(browser)
#         actions.click(scroll_element).key_down(Keys.PAGE_DOWN).perform()
#
#         # Ждем, чтобы дать странице время на подгруздку новых элементов
#         time.sleep(1)
#
#         nums_elements = scroll_element.find_elements(By.TAG_NAME, 'p')
#
#         new_elements = False
#
#         for i in nums_elements:
#             num = i.text.strip()
#             if num.isdigit() and num not in unique_numbers:  # Проверка на уникальность и числовое значение
#                 unique_numbers.add(num)  # Добавляем новое число в множество
#                 sum_num += int(num)  # Сразу добавляем к общей сумме
#                 new_elements = True
#
#             # Если новые элементы не были добавлены, выходим из цикла
#         if not new_elements:
#             print("Больше нет новых элементов для добавления.")
#             print("Сумма числовых значений:", sum_num)
#             break


#Задача 6.5.4

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver import Keys, ActionChains
# import time
#
# # options_chrome = webdriver.ChromeOptions()
# # options_chrome.add_argument('--headless=new')
# #
# # Используем контекстный менеджер для открытия браузера
# # with webdriver.Chrome(options=options_chrome) as browser:
# with webdriver.Chrome() as browser:
#     browser.get('https://parsinger.ru/infiniti_scroll_3/')
#     time.sleep(1)
#
#     for q in range(1, 6):
#         div = browser.find_element(By.XPATH, f'//*[@class="scroll-container_{q}"]/div')
#         time.sleep(3)
#
#         for x in range(8):
#             ActionChains(browser).move_to_element(div).scroll_by_amount(1, 500).perform()
#         span_list = browser.find_elements(By.TAG_NAME, 'span')
#
#         counter = 0
#         for i in span_list:
#             if i.text:
#                 counter += int(i.text)
#
#     print(counter)


#Задача 6.5.5

# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# import time
#
# with webdriver.Chrome() as browser:
#     # Переходим на целевую страницу
#     browser.get('https://parsinger.ru/selenium/5.7/1/index.html')
#     # Находим все кнопки на странице по тегу <button>
#     uran = browser.find_elements(By.TAG_NAME, 'button')
#
#     for u in uran:
#         # Прокручиваем страницу до кнопки, чтобы она стала видимой
#         browser.execute_script("return arguments[0].scrollIntoView(true);", u)
#         # Кликаем по кнопке
#         u.click()
#
#     # Получаем текст последнего всплывающего окна alert
#     alert = browser.switch_to.alert.text
#     time.sleep(2)
#     print(alert)


#Задача 6.5.6

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver import Keys, ActionChains
# import time
#
# # options_chrome = webdriver.ChromeOptions()
# # options_chrome.add_argument('--headless=new')
# #
# # Используем контекстный менеджер для открытия браузера
# # with webdriver.Chrome(options=options_chrome) as browser:
# with webdriver.Chrome() as browser:
#     browser.get('https://parsinger.ru/selenium/5.7/5/index.html')
#     time.sleep(1)
#     # Находим все кнопки на странице по тегу <button>
#     buttons = browser.find_elements(By.CLASS_NAME, 'timer_button')
#     for i in buttons:
#         actions = ActionChains(browser)
#         # actions.click_and_hold(i).perform()
#         # time.sleep(10)
#         # actions.release(i).perform()
#         # Нажимаем и удерживаем кнопку, затем паузим на время, равное тексту на кнопке
#         # 'button.text' это строка, которая представляет время задержки в секундах
#         actions.click_and_hold(i).pause(float(i.text)).release(i).perform()
#     alert = browser.switch_to.alert.text
#     time.sleep(2)
#     print(alert)


#Задача 6.5.6

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver import Keys, ActionChains
# import time
#
# # options_chrome = webdriver.ChromeOptions()
# # options_chrome.add_argument('--headless=new')
# #
# # Используем контекстный менеджер для открытия браузера
# # with webdriver.Chrome(options=options_chrome) as browser:
# with webdriver.Chrome() as browser:
#     browser.get('https://parsinger.ru/selenium/5.7/4/index.html')
#     time.sleep(1)
#
#     # for q in range(1, 6):
#     main_container = browser.find_element(By.ID, 'main_container')
#
#     for x in range(10):
#
#         ActionChains(browser).move_to_element(main_container).scroll_by_amount(1, 602).perform()
#     span_list = browser.find_elements(By.TAG_NAME, 'span')
#
#     counter = 0
#         # for i in span_list:
#         #     if i.text:
#         #         counter += int(i.text)
#         #
#         # print(counter)


# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.alert import Alert
#
# # Запускаем браузер с помощью WebDriver
# with webdriver.Chrome() as browser:
#     # Переходим на указанную страницу
#     browser.get('https://parsinger.ru/selenium/5.7/4/index.html')
#
#     # Находим контейнер, в котором происходит прокрутка
#     main_container = browser.find_element(By.ID, 'main_container')
#
#     # Получаем начальную высоту прокручиваемого контейнера
#     last_height = browser.execute_script("return arguments[0].scrollHeight", main_container)
#     print(f'Начальная высота прокручиваемого контейнера: {last_height}')
#     while True:
#         # Прокручиваем элемент до конца, устанавливая scrollTop в значение scrollHeight
#         browser.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", main_container)
#
#         # Ждем немного времени, чтобы дать браузеру время на подгрузку контента
#         time.sleep(1)  # Увеличьте время ожидания, если контент подгружается медленно
#
#         # Получаем новую высоту прокручиваемого контейнера
#         new_height = browser.execute_script("return arguments[0].scrollHeight", main_container)
#         print(f"новая высота: {new_height}")
#         # time.sleep(3)
#         # Если высота не изменилась, значит, больше нет новых элементов, которые подгружаются
#         if new_height == last_height:
#             print("Достигнут конец прокрутки.")
#             time.sleep(2)
#             # Находим все чекбоксы в контейнере
#             checkboxes = main_container.find_elements(By.CSS_SELECTOR, "div.child_container input[type='checkbox']")
#
#             # Кликаем по всем чекбоксам, чьи значения четные
#             for box in checkboxes:
#                 if int(box.get_attribute('value')) % 2 == 0:
#                     box.click()
#
#             # Находим кнопку для подтверждения действия (например, кнопка "alert")
#             main_container.find_element(By.CLASS_NAME, 'alert_button').click()
#
#             # Переходим к всплывающему окну с алертом и получаем текст из этого окна
#             alert_text = Alert(browser).text
#             print(alert_text)  # Выводим текст алерта
#
#             # Завершаем выполнение цикла
#             break
#
#         # Обновляем переменную last_height для следующей итерации
#         last_height = new_height


"""Окна и вкладки"""


# Вкладки в браузере

# import time
# from selenium import webdriver
#
#
# with webdriver.Chrome() as browser:
#     result = []
#     browser.get('http://parsinger.ru/blank/2/1.html')
#     time.sleep(1)
#     browser.execute_script('window.open("http://parsinger.ru/blank/2/2.html", "_blank1");')
#     browser.execute_script('window.open("http://parsinger.ru/blank/2/3.html", "_blank2");')
#     browser.execute_script('window.open("http://parsinger.ru/blank/2/4.html", "_blank3");')
#     time.sleep(2)
#     print(browser.window_handles)


# from selenium import webdriver
# from selenium.webdriver.common.by import By
# with webdriver.Chrome() as browser:
#     browser.get("https://stepik.org/course/104774/promo") # Вместо вкладки data; будет вкладка в которой будет загружен степик
#     browser.execute_script('window.open("http://parsinger.ru/blank/2/1.html", "_blank1");')
#     browser.execute_script('window.open("http://parsinger.ru/blank/2/2.html", "_blank2");')
#     browser.execute_script('window.open("http://parsinger.ru/blank/2/3.html", "_blank3");')
#     browser.execute_script('window.open("http://parsinger.ru/blank/2/4.html", "_blank4");')
#
#     for x in reversed(range(len(browser.window_handles))):  #reversed(range(len(browser.window_handles))) Для итерирования по порядку
#         browser.switch_to.window(browser.window_handles[x])
#         for y in browser.find_elements(By.CLASS_NAME, 'check'):
#             y.click()


# import time
# from selenium import webdriver
# with webdriver.Chrome() as browser:
#     time.sleep(1)
#     browser.execute_script('window.open("http://parsinger.ru/blank/0/1.html", "_blank1");')
#     browser.execute_script('window.open("http://parsinger.ru/blank/0/2.html", "_blank2");')
#     browser.execute_script('window.open("http://parsinger.ru/blank/0/3.html", "_blank3");')
#     browser.execute_script('window.open("http://parsinger.ru/blank/0/4.html", "_blank4");')
#     browser.execute_script('window.open("http://parsinger.ru/blank/0/5.html", "_blank5");')
#     browser.execute_script('window.open("http://parsinger.ru/blank/0/6.html", "_blank6");')
#
#     for x in range(len(browser.window_handles)):
#         browser.switch_to.window(browser.window_handles[x])
#         time.sleep(1)
#         print(browser.execute_script("return document.title;"), browser.window_handles[x])


# from selenium import webdriver
# with webdriver.Chrome() as browser:
#     browser.get("https://stepik.org/course/104774/promo")
#     print(browser.execute_script("return document.title;"))
#     time.sleep(3)


# Размеры окна браузера

# import time
# from selenium import webdriver
# with webdriver.Chrome() as browser:
#     browser.get('http://parsinger.ru/window_size/1/')
#     browser.set_window_size(1200, 720)
#     time.sleep(5)


# from selenium import webdriver
#
# with webdriver.Chrome() as browser:
#     # Открываем указанный URL в браузере.
#     browser.get('http://parsinger.ru/window_size/1/')
#
#     # Устанавливаем размер окна браузера на 1200 пикселей в ширину и 720 пикселей в высоту.
#     browser.set_window_size(1200, 720)
#
#     # Получаем текущий размер окна браузера в виде словаря, где 'height' - высота окна,
#     # 'width' - ширина окна. И затем печатаем значение высоты окна.
#     print(browser.get_window_size())
#
#     # Аналогично печатаем значение ширины окна.
#     print(browser.get_window_size().get('width'))


#Модальные окна

# import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# with webdriver.Chrome() as browser:
#     browser.get('https://staging.tourpartnergroup.estr.xyz/')
#     browser.find_element(By.ID, 'alert')
#     time.sleep(1)
#     alert = browser.switch_to.alert # Если вы планируете что-то делать с этим событием, можно добавить его в переменную
#     print(alert.text)


# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# with webdriver.Chrome() as browser:
#     browser.get('http://parsinger.ru/blank/modal/1/index.html')
#     browser.find_element(By.ID, 'prompt').click()
#     time.sleep(2)
#     prompt = browser.switch_to.alert
#     prompt.send_keys('Введёный текст')
#     prompt.accept()
#     time.sleep(.5)
#     print(browser.find_element(By.ID, 'result').text)
#     time.sleep(1)


# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# with webdriver.Chrome() as browser:
#     browser.get('http://parsinger.ru/blank/modal/1/index.html')
#     browser.find_element(By.ID, 'confirm').click()
#     time.sleep(2)
#     prompt = browser.switch_to.alert
#     prompt.accept() #Замените на .dismiss() чтобы нажать на кнопку "Отмена"
#     time.sleep(3)


# Работа с фреймами

# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# with webdriver.Chrome() as driver:
#     driver.get('https://parsinger.ru/selenium/5.8/4/index.html')
#
#     # Переключаемся на iframe
#     iframe_element = driver.find_element(By.TAG_NAME, 'iframe')
#     driver.switch_to.frame(iframe_element)
#
#     # Извлекаем HTML содержимое из iframe
#     iframe_content = driver.page_source
#
#     print(iframe_content)


# Задача 7.5.1

# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.alert import Alert
#
# # Запускаем браузер с помощью WebDriver
# with webdriver.Chrome() as browser:
#     # Переходим на указанную страницу
#     browser.get('https://parsinger.ru/selenium/5.8/1/index.html')
#     buttons = browser.find_elements(By.CLASS_NAME, 'buttons')
#     for i in buttons:
#         i.click()
#         alert = browser.switch_to.alert
#         alert.accept()
#         code = browser.find_element(By.ID, 'result').text
#         if code:
#             print(code)


# Задача 7.5.2

# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.alert import Alert
#
# # Запускаем браузер с помощью WebDriver
# with webdriver.Chrome() as browser:
#     # Переходим на указанную страницу
#     browser.get('https://parsinger.ru/selenium/5.8/2/index.html')
#     buttons = browser.find_elements(By.CLASS_NAME, 'buttons')
#     enter_code = browser.find_element(By.ID, 'input')
#     check = browser.find_element(By.ID, 'check')
#     for i in buttons:
#         i.click()
#         alert = browser.switch_to.alert
#         num_alert = alert.text
#         alert.accept()
#         enter_code.send_keys(num_alert)
#         check.click()
#         code = browser.find_element(By.ID, 'result').text
#
#         if code:
#             print(code)
#         break


# Задача 7.5.3

# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.alert import Alert
#
# # Запускаем браузер с помощью WebDriver
# with webdriver.Chrome() as browser:
#     # Переходим на указанную страницу
#     browser.get('https://parsinger.ru/selenium/5.8/3/index.html')
#     buttons = browser.find_elements(By.CLASS_NAME, 'pin')
#     verify_code = browser.find_element(By.ID, 'check')
#     # check = browser.find_element(By.ID, 'check')
#     for i in buttons:
#         extract_text = i.text
#         verify_code.click()
#         alert = browser.switch_to.alert
#         alert.send_keys(extract_text)
#         # browser.send_keys(extract_text)
#         alert.accept()
#
#         result = browser.find_element(By.ID, 'result').text
#         if result != 'Неверный пин-код':
#             print(result)


# Задача 7.5.4

# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.alert import Alert
#
# # Запускаем браузер с помощью WebDriver
# with webdriver.Chrome() as browser:
#     # Переходим на указанную страницу
#     browser.get('https://parsinger.ru/window_size/1/')
#     browser.set_window_size(571, 702)
#     time.sleep(2)
#     result = browser.find_element(By.ID, 'result').text
#     print(result)


# Задача 7.5.5

# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.alert import Alert
#
# # Запускаем браузер с помощью WebDriver
# with webdriver.Chrome() as browser:
#     # Переходим на указанную страницу
#     browser.get('https://parsinger.ru/window_size/2/index.html')
#     # browser.set_window_size(571, 702)
#     window_size_x = [616, 648, 680, 701, 730, 750, 805, 820, 855, 890, 955, 1000]
#     window_size_y = [300, 330, 340, 388, 400, 421, 474, 505, 557, 600, 653, 1000]
#
#     # for x, y in zip(window_size_x, window_size_y):
#     #     browser.set_window_size(x, y)
#     #     result = browser.find_element(By.ID, 'result').text
#     #
#     #     print(result)
#     for width in window_size_x:
#         for height in window_size_y:
#             browser.set_window_size(width + 16, height + 147)
#             # print(f"Размер окна установлен на: {width}x{height}")
#             time.sleep(1)
#             result = browser.find_element(By.ID, 'result').text


# Задача 7.5.6

# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.alert import Alert
#
# # Запускаем браузер с помощью WebDriver
# with webdriver.Chrome() as browser:
#     # Переходим на указанную страницу
#     browser.get('https://parsinger.ru/window_size/2/index.html')
#     # browser.set_window_size(571, 702)
#     window_size_x = [516, 648, 680, 701, 730, 750, 805, 820, 855, 890, 955, 1000]
#     window_size_y = [270, 300, 340, 388, 400, 421, 474, 505, 557, 600, 653, 1000]
#
#     # for x, y in zip(window_size_x, window_size_y):
#     #     browser.set_window_size(x, y)
#     #     result = browser.find_element(By.ID, 'result').text
#     #
#     #     print(result)
#     for width in window_size_x:
#         for height in window_size_y:
#             browser.set_window_size(width + 16, height + 147)
#             if browser.find_element(By.ID, 'result').text.isdigit():
#                 print('{'  f"'width': {width}, 'height': {height}"  '}')


# Задача 7.5.7

# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.alert import Alert
#
# # Запускаем браузер с помощью WebDriver
# with webdriver.Chrome() as browser:
#     # Переходим на указанную страницу
#     browser.get('https://parsinger.ru/blank/3/index.html')
#     buttons = browser.find_elements(By.CLASS_NAME, 'buttons')
#     sum = 0
#     for i in buttons:
#         i.click()
#     for i in reversed(range(len(browser.window_handles))[1:]):
#         browser.switch_to.window(browser.window_handles[i])
#         title = browser.execute_script("return document.title;")
#         sum += int(title)
#     print(title)

#Второй вариант решения
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# with webdriver.Chrome() as browser:
#     browser.get('http://parsinger.ru/blank/3/index.html')
#     button = browser.find_elements(By.CLASS_NAME, 'buttons')
#     summa = []
#     for x in button:
#         x.click()
#
#     for x in reversed(range(len(browser.window_handles))[1:]):
#         browser.switch_to.window(browser.window_handles[x])
#         dig = browser.execute_script("return document.title;")
#         summa.append(int(dig))
#     print(sum(summa))


# Задача 7.5.8

# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.alert import Alert
#
# # Запускаем браузер с помощью WebDriver
# with webdriver.Chrome() as browser:
#     sites = ['http://parsinger.ru/blank/1/1.html', 'http://parsinger.ru/blank/1/2.html',
#              'http://parsinger.ru/blank/1/3.html', 'http://parsinger.ru/blank/1/4.html',
#              'http://parsinger.ru/blank/1/5.html', 'http://parsinger.ru/blank/1/6.html']
#
#     sum_nums = 0  # Переменная для хранения суммы чисел
#
#     for i in sites:
#         browser.execute_script("window.open('{i}')")
#         browser.get(i)
#         browser.find_element(By.CLASS_NAME, 'checkbox_class').click()
#         # time.sleep(2)
#         num = int(browser.find_element(By.ID, 'result').text) ** 0.5
#         sum_nums += num
#     print(round(sum_nums, 9))


# Задача 7.5.9

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.common.exceptions import NoAlertPresentException
#
# with webdriver.Chrome() as browser:
#     browser.get('https://parsinger.ru/selenium/5.8/5/index.html')
#     guess_input = browser.find_element(By.ID, 'guessInput')
#     check_btn = browser.find_element(By.ID, 'checkBtn')
#     frame = browser.find_elements(By.TAG_NAME, 'iframe')
#
#     for x in frame:
#         browser.switch_to.frame(x.get_attribute('id'))
#         browser.find_element(By.TAG_NAME, 'button').click()
#         val = browser.find_element(By.ID, 'numberDisplay').text
#         browser.switch_to.default_content()
#         guess_input.clear()
#         guess_input.send_keys(val)
#         check_btn.click()
#         try:
#             print(browser.switch_to.alert.text)
#         except NoAlertPresentException:
#             pass



""" Ожидания явные и неявные"""

# 8.1 Явное ожидание
# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# with webdriver.Chrome() as browser:
#     browser.get('http://parsinger.ru/expectations/1/index.html')
#     time.sleep(3)
#     browser.find_element(By.ID, 'btn').click()
#     time.sleep(2)


# import time
#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import WebDriverWait
#
# with webdriver.Chrome() as browser:
#     browser.get('http://parsinger.ru/expectations/1/index.html')
#     element = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.ID, "btn"))).click()
#     time.sleep(3)
#     print(browser.find_element(By.ID, 'result').text)


# from selenium import webdriver
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import WebDriverWait
# with webdriver.Chrome() as browser:
#     browser.get('http://parsinger.ru/expectations/2/index.html')
#     element = WebDriverWait(browser, 10).until(EC.title_is('title changed'))
#     print(element)


# from selenium import webdriver
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.common.by import By
# with webdriver.Chrome() as browser:
#     browser.get('http://parsinger.ru/expectations/2/index.html')
#     browser.find_element(By.ID, "btn").click()
#     element = WebDriverWait(browser, 10).until(EC.title_is('title changed'))
#     print(element)

# with webdriver.Chrome() as browser:
#     browser.get('http://parsinger.ru/expectations/2/index.html')
#     browser.find_element(By.ID, "btn").click()
#     element = WebDriverWait(browser, 10).until(EC.title_contains('tle'))
#     print(element)



# Задача 8.8.1

# from selenium import webdriver
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.common.by import By
# with webdriver.Chrome() as browser:
#     browser.get('https://parsinger.ru/expectations/3/index.html')
#     WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.ID, 'btn'))).click()
#
#     # Ожидаем изменения заголовка страницы на '345FDG3245SFD' (максимум 30 секунд)
#     WebDriverWait(browser, 30).until(EC.title_is('345FDG3245SFD'))
#
#     # Извлекаем текст элемента с ID 'result' и выводим его в консоль
#     print(browser.find_element(By.ID, 'result').text)


# Задача 8.8.2

# from selenium import webdriver
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.common.by import By
# with webdriver.Chrome() as browser:
#     browser.get('https://parsinger.ru/expectations/4/index.html')
#
#     WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.ID, 'btn'))).click()
#
#     # Ожидаем изменения заголовка страницы на '345FDG3245SFD' (максимум 30 секунд)
#     is_title = WebDriverWait(browser, 30, poll_frequency=0.1).until(EC.title_contains('JK8HQ'))
#
#     if is_title:
#         print(browser.title)


# Задача 8.8.3

# from selenium import webdriver
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.common.by import By
# with webdriver.Chrome() as browser:
#     # Открываем заданный URL
#     browser.get('https://parsinger.ru/expectations/6/index.html')
#
#     # Явное ожидание: ждем, пока кнопка с ID 'btn' станет кликабельной, затем кликаем по ней
#     WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.ID, 'btn'))).click()
#
#     # Явное ожидание: ждем, пока элемент с классом 'BMH21YY' появится в DOM,
#     # и получаем текст из этого элемента
#     key = WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.CLASS_NAME, 'BMH21YY'))).text
#
#     print(key)


# Задача 8.8.4

# from selenium import webdriver
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.common.by import By
# with webdriver.Chrome() as browser:
#     # Открываем заданный URL
#     browser.get('https://parsinger.ru/selenium/5.9/2/index.html')
#
#     WebDriverWait(browser, 120, poll_frequency=0.1).until(EC.presence_of_element_located((By.ID, 'qQm9y1rk'))).click()
#
#     print(browser.switch_to.alert.text)


# Задача 8.8.5

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
with webdriver.Chrome() as browser:
    # Открываем заданный URL
    browser.get('https://parsinger.ru/selenium/5.9/3/index.html')

    ids_to_find = ['xhkVEkgm', 'QCg2vOX7', '8KvuO5ja', 'CFoCZ3Ze', '8CiPCnNB', 'XuEMunrz', 'vmlzQ3gH', 'axhUiw2I',
                   'jolHZqD1', 'ZM6Ms3tw', '25a2X14r', 'aOSMX9tb', 'YySk7Ze3', 'QQK13iyY', 'j7kD7uIR']

    for i in ids_to_find:
        WebDriverWait(browser, 120, poll_frequency=0.1).until(EC.visibility_of_element_located((By.ID, i))).click()

    print(browser.switch_to.alert.text)