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

def answerQuestions(driver):
    driver.find_element_by_partial_link_text("Continue").click()
    driver.implicitly_wait(10)
    elements = driver.find_elements_by_class_name("col-xs-6")
    for i in range(2, 17, 2):
        elements[i].click()
    driver.find_element_by_tag_name("input").click()
    

driver = webdriver.Firefox()
login(driver)
answerQuestions(driver)
driver.close()