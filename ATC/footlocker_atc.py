from selenium import webdriver
from selenium.webdriver.support.ui import Select

import time

link = "http://www.footlocker.com/product/model:281962/sku:BA7259/adidas-originals-nmd-runner-2-womens/"
size = "10.0" #must be in format ##.#
driver = webdriver.Chrome()


driver.get(link)
#give the page time to load with sleep
time.sleep(5)
driver.find_element_by_class_name('select_size').click()

#pause action to prevent being blocked
time.sleep(2)
#chooses random size; issue: button is hidden and cannot be selected
#TODO: support for X size
driver.find_element_by_xpath("//span[@id='size_selection_list']/a[@value=\'"+size+"\']").click()
time.sleep(3)
driver.find_element_by_class_name('add_to_cart').click()
time.sleep(4)
driver.find_element_by_id('order_summary').click()
time.sleep(4)
driver.find_element_by_id('cart_checkout_button_bottom').click()
time.sleep(2)
