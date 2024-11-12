from selenium.webdriver.common.by import By

add_delete_menu_btn = (By.XPATH, "//a[@href='/add_remove_elements/']")
add_btn = (By.XPATH, "//button[@onclick='addElement()']")
delete_btn = (By.XPATH, "//button[@onclick='deleteElement()']")

btn_auth = (By.XPATH, "//a[@href='/basic_auth']")
mms_registration = (By.CSS_SELECTOR, ".example p")

broken_btn_menu = (By.XPATH, "//a[@href='/broken_images']")

checkbox_menu = (By.XPATH, "//a[@href='/checkboxes']")
check_box_btn_1 = (By.CSS_SELECTOR, "input[type='checkbox']")
# checkbox_btn_1 = (By.XPATH, "//input[@type='checkbox'][1]")
# checkbox_btn_2 = (By.XPATH, "//input[@type='checkbox'][2]")