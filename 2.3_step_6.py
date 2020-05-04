from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math
import os

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link="http://suninjuly.github.io/redirect_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    first_window = browser.window_handles[0]
    but = browser.find_element_by_css_selector('button.trollface')
    but.click()
    second_window = browser.window_handles[1]
    browser.switch_to_window(second_window)
    number = browser.find_element_by_id('input_value')
    x = number.text
    y = calc(x)
    answer = browser.find_element_by_id('answer')
    answer.send_keys(str(y))
    submit = browser.find_element_by_class_name('btn.btn-primary')
    submit.click()

finally:
    time.sleep(10)
    browser.quit()

