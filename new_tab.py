from selenium import webdriver
import math

link = "http://suninjuly.github.io/redirect_accept.html"

def calc(number):
    return str(math.log(abs(12*math.sin(int(number)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)
    browser.find_element_by_tag_name("button").click()

    new_tab = browser.window_handles[1]
    browser.switch_to.window(new_tab)

    number = browser.find_element_by_id("input_value").text
    x = calc(number)
    browser.find_element_by_id("answer").send_keys(x)
    browser.find_element_by_tag_name("button").click()
    print(browser.switch_to.alert.text)

finally:
    browser.quit()