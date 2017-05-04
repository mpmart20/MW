from selenium import webdriver
from selenium.webdriver.support.ui import Select
import schedule
import time

links = ["http://www.champssports.com/product/model:258371/sku:BB2885/adidas-originals-nmd-r1-mens/red/black/"]
driver = webdriver.Chrome()

#Drives the amazon web crawler ||| Designed for items without sizing
def driveChamps(url):
    driver.get(url)
    time.sleep(5)

    #work around surveys and other popups
    driver.refresh()
    time.sleep(5)
    driver.refresh()
    time.sleep(5)
    driver.find_element_by_xpath("//a[@id='pdp_size_select']").click()
    time.sleep(5)
    try:
        driver.find_element_by_xpath("//a[@data-value='10.0']").click()
        print "Size 10 is available, atempting to add to cart!"
    except:
        try:
            driver.find_element_by_xpath("//a[@data-value='10.5']").click()
            print "Size 10.5 is available, atempting to add to cart!"
        except:
            print "You took an L this week"
    time.sleep(5)
    driver.find_element_by_xpath("//button[@name='pdp_addtocart']").click()
    time.sleep(5)



def job(linksCol):
    for x in linksCol:
        curr = driveChamps(x)


#runs the links once
job(links)


#Uncomment the code below to make is scheduled to military time

# schedule.every().day.at('23:39').do(job,links)
# while True:
#     schedule.run_pending()
#     time.sleep(1)
