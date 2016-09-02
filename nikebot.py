import csv
import json
import re
import requests
from selenium import webdriver
import sys
import time

driver = webdriver.Firefox()

driver.get("https://www.google.com")
time.sleep(2)

#driver.find_element_by_xpath("//class[@title='Choose Size 10.5']").click()
#driver.find_element_by_xpath("//label[@id='addToCart']").click()


#driver.delete_all_cookies()
#driver.close()
