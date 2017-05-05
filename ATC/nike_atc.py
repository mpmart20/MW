from selenium import webdriver



driver = webdriver.Chrome()
driver.get("http://store.nike.com/us/en_us/pd/flyknit-racer-unisex-running-shoe/pid-10284845/pgid-11410871")
driver.implicitly_wait(5)
driver.find_element_by_class_name('exp-pdp-size-dropdown-container').click()
p = driver.find_elements_by_xpath("//li[@class='nsg-form--drop-down--option']")#[0].click()
print p
driver.quit()
