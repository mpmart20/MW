from selenium import webdriver
from selenium.webdriver.support.ui import Select

import time

link = "http://www.footlocker.com/product/model:281962/sku:BA7259/adidas-originals-nmd-runner-2-womens/"
driver = webdriver.Chrome()
driver.get(link)

#give the page time to load with sleep
time.sleep(5)
driver.find_element_by_class_name('select_size').click()

#pause action to prevent being blocked
time.sleep(2)

#chooses random size; issue: button is hidden and cannot be selected
#TODO: support for X size
driver.find_element_by_xpath("//span[@id='size_selection_list']").click()
time.sleep(1)
driver.find_element_by_class_name('add_to_cart ').click()
time.sleep(1)
driver.find_element_by_id('header_cart_button').click()
time.sleep(4)
driver.find_element_by_id('cart_checkout_button_bottom').click()
