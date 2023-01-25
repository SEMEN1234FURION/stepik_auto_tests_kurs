from selenium import webdriver
from selenium.webdriver.common.by import By
import time 

link = " http://suninjuly.github.io/find_xpath_form"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.TAG_NAME, "input")
    input1.send_keys("Semen")
    input2 = browser.find_element(By.NAME, "last_name")
    input2.send_keys("Kohk")
    input3 = browser.find_element(By.CLASS_NAME, "form-control.city")
    input3.send_keys("VL")
    input4 = browser.find_element(By.ID, "country")
    input4.send_keys("Russia")
    button = browser.find_element(By.XPATH,"/html/body/div/form/div[6]/button[3]")
    button.click()

finally:
    
    time.sleep(15)
    
    browser.quit()