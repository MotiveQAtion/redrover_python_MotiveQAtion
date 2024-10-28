from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get("http://195.133.27.184/")


element = browser.find_element(By.XPATH, "//a[@href='/2/']")
element.is_displayed()
element.click()
assert browser.current_url == "http://195.133.27.184/2/", "Wrong URL"
