from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import config
import time

def login(driver):
    driver.get("http://patientconnect.bu.edu")
    element = driver.find_element_by_id("j_username")
    element.send_keys(config.username)
    element = driver.find_element_by_id("j_password")
    element.send_keys(config.password)
    element.send_keys(Keys.ENTER)
    time.sleep(3)
    if "Home" not in driver.title:
        raise Exception
    driver.find_element_by_partial_link_text("Complete Survey").click()


driver = webdriver.Firefox()
login(driver)
driver.close()