from selenium import webdriver
from selenium.webdriver.support.ui import Select
import schedule
import time

links = [{"url":"https://www.amazon.com/dp/B004FGA5AA/ref=wl_it_dp_o_pC_nS_ttl?_encoding=UTF8&colid=27YIY6O8DQZK1&coliid=I310KTBULRG23P" ,"budget":100}]
driver = webdriver.Chrome()


#checks if item is within budget
def checkPrice(budget, price):
    price = price.replace("$","")
    if float(price) <= budget:
        return True
    return False

#Drives the amazon web crawler ||| Designed for items without sizing
def driveAmazon(url,budget):
    driver.refresh()
    driver.get(url)
    #apparently text not text() since the update made it an attribute instead of a func
    itemName = driver.find_element_by_xpath("//span[@id='productTitle']").text
    currPrice = driver.find_element_by_xpath("//span[@id='priceblock_ourprice']").text
    time.sleep(1)
    if checkPrice(budget, currPrice):
        time.sleep(5)
        driver.find_element_by_xpath("//input[@id='add-to-cart-button']").click()
        time.sleep(5)
        #some items may have a warranty box open
        try:
            driver.find_element_by_xpath("//span[@id='warrantyModalBtnAtc']").click()
            print "Skipped Warranty and added to cart!"
        except:
            print "No warranty option"

        time.sleep(1)
        print "Added item: " + itemName + " to cart!"
        return itemName, float(currPrice.replace("$",""))
    return "None", 0.0

def job(linksCol):
    items = []
    total = 0.0
    for x in linksCol:
        curr = driveAmazon(x["url"],x["budget"])
        items.append(curr[0])
        total += curr[1]
    print items,total


#runs the links once
job(links)


#Uncomment the code below to make is scheduled to military time

# schedule.every().day.at('23:39').do(job,links)
# while True:
#     schedule.run_pending()
#     time.sleep(1)
