import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 1 Мастер заполнения форм

# with webdriver.Chrome() as browser:
#     browser.get('https://parsinger.ru/selenium/1/1.html')
# input_form = browser.find_elements(By.CLASS_NAME, 'form')
# for field in input_form:
#     field.send_keys("Текст")
#
# browser.find_element(By.ID, 'btn').click()
# time.sleep(5)
# result = browser.find_element(By.ID, 'result').text
#
# print(result)

# 2 Охотник за Сокровищами

# with webdriver.Chrome() as browser:
#     browser.get('https://parsinger.ru/selenium/2/2.html')
#     find_link = browser.find_element(By.PARTIAL_LINK_TEXT, '16243162441624')
#     find_link.click()
#     time.sleep(5)
#
#     result = browser.find_element(By.ID, 'result').text
#     print(result)

# 3 Кодекс Охотников за Цифрами

# with webdriver.Chrome() as browser:
#     browser.get('https://parsinger.ru/selenium/3/3.html')
#     find_text = browser.find_elements(By.TAG_NAME, 'p')
#     counter = 0
#     for i in find_text:
#         counter += int(i.text)
#
#     print(counter)

# 4  Поход за сокровищами в Цифровом Лабиринте

# with webdriver.Chrome() as browser:
#     browser.get('https://parsinger.ru/selenium/3/3.html')
#     time.sleep(5)
#     find_elements = browser.find_elements(By.XPATH, "//div[@class='text']/p[2]")
#
#     counter = 0
#     for i in find_elements:
#         text = i.text
#         counter = counter + int(text)
#
#     print(counter)

# 5 Операция 'Кодовый Замок

# with webdriver.Chrome() as browser:
#     browser.get('https://parsinger.ru/selenium/4/4.html')
#     check_boxes = browser.find_elements(By.CLASS_NAME, 'check')
#     for i in check_boxes:
#         i.click()
#
#     browser.find_element(By.CLASS_NAME, 'btn').click()
#     result = browser.find_element(By.ID, 'result').text
#
#     print(result)

# 6  Кодовая Одиссея

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
#     check_boxes = browser.find_elements(By.CLASS_NAME, 'check')
#     for i in check_boxes:
#         if int(i.get_attribute('value')) in numbers:
#             i.click()
#
#     browser.find_element(By.CLASS_NAME, 'btn').click()
#     result = browser.find_element(By.ID, 'result').text
#
#     print(result)

# 7 Операция "Выпадающие списки"
# with webdriver.Chrome() as browser:
#     browser.get('https://parsinger.ru/selenium/7/7.html')
#     find_elements = browser.find_elements(By.TAG_NAME, 'option')
#     counter = 0
#     for i in find_elements:
#         counter += int(i.text)
#
#     browser.find_element(By.ID, 'input_result').send_keys(str(counter))
#     browser.find_element(By.ID, 'sendbutton').click()
#     result = browser.find_element(By.ID, 'result').text
#     print(result)

# 8  Миссия "Загадочный След"

# with webdriver.Chrome() as browser:
#     browser.get('https://parsinger.ru/selenium/6/6.html')
#     time.sleep(5)
#     text = browser.find_element(By.ID, 'text_box').text
#     text1 = eval(text)
#
#     options = browser.find_elements(By.TAG_NAME, 'option')
#     x = 0
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
#     print(result)

# Раздел 8.8

# 1
# with webdriver.Chrome() as browser:
#     browser.get('https://parsinger.ru/expectations/3/index.html')
#     btn = WebDriverWait(browser, timeout=10).until(EC.element_to_be_clickable((By.ID, 'btn')))
#     btn.click()
#     title = WebDriverWait(browser, timeout=0).until(EC.title_is('345FDG3245SFD'))
#     text = browser.find_element(By.ID, 'result').text
#
#     print(text)

# 2
# with webdriver.Chrome() as browser:
#     browser.get('https://parsinger.ru/expectations/4/index.html')
#     btn = WebDriverWait(browser, timeout=10).until(EC.element_to_be_clickable((By.ID, 'btn')))
#     btn.click()
#     if WebDriverWait(browser, timeout=35).until(EC.title_contains('JK8HQ')):
#         text = browser.title
#
#     print(text)

# 3
# with webdriver.Chrome() as browser:
#     browser.get('https://parsinger.ru/expectations/6/index.html')
#     btn = WebDriverWait(browser, timeout=10).until(EC.element_to_be_clickable((By.ID, 'btn')))
#     btn.click()
#     # locator = browser.find_element((By.CLASS_NAME, 'BMH21YY'))
#     element = WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.CLASS_NAME, 'BMH21YY')))
#     text = element.text
#
#     print(text)

# 4
# with webdriver.Chrome() as browser:
#     browser.get('https://parsinger.ru/selenium/5.9/2/index.html')
#     block = WebDriverWait(browser, timeout=100).until(EC.presence_of_element_located((By.ID, 'qQm9y1rk')))
#     block.click()
#     text1 = browser.switch_to.alert
#     text2 = text1.text
#
#     print(text2)

# 5
# with webdriver.Chrome() as browser:
#     browser.implicitly_wait(60)
#     browser.get('https://parsinger.ru/selenium/5.9/3/index.html')
#     ids_to_find = ['xhkVEkgm', 'QCg2vOX7', '8KvuO5ja', 'CFoCZ3Ze', '8CiPCnNB', 'XuEMunrz', 'vmlzQ3gH', 'axhUiw2I',
#                    'jolHZqD1', 'ZM6Ms3tw', '25a2X14r', 'aOSMX9tb', 'YySk7Ze3', 'QQK13iyY', 'j7kD7uIR']
#
#     # boxes = browser.find_elements(By.XPATH, '//div[@id="display: block;"]')
#     for i in ids_to_find:
#         box = WebDriverWait(browser, timeout=100).until(EC.visibility_of_element_located((By.ID, i)))
#         box.click()
#
#     text1 = browser.switch_to.alert
#     text2 = text1.text
#
#     print(text2)


