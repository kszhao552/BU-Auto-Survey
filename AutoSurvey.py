from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import config

def login(driver):
    driver.get("http://patientconnect.bu.edu")
    element = driver.find_element_by_id("j_username")
    element.send_keys(config.username)
    element = driver.find_element_by_id("j_password")
    element.send_keys(config.password)
    element.send_keys(Keys.ENTER)

driver = webdriver.Firefox()
login(driver)
driver.close()