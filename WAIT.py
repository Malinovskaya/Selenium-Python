from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

link = "http://suninjuly.github.io/explicit_wait2.html"

def calc(number):
    return str(math.log(abs(12*math.sin(int(number)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)
    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), '100')
    )
    browser.find_element_by_id("book").click()
    number = browser.find_element_by_id("input_value").text
    x = calc(number)
    browser.find_element_by_id("answer").send_keys(x)
    browser.find_element_by_id("solve").click()
    time.sleep(30)

finally:
    browser.quit()



