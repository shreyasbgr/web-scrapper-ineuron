import requests
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen as uReq
from selenium import webdriver
import time

def testing_web_scrapper_code():
    searchString = "tablets"
    flipkart_url = "https://www.flipkart.com/search?q=" + searchString
    uClient = uReq(flipkart_url)
    flipkartPage = uClient.read()
    uClient.close()
    flipkart_html = bs(flipkartPage, "html.parser")
    bigboxes = flipkart_html.findAll("div", {"class": "_1AtVbE col-12-12"})
    print(flipkart_html)

def testing_web_scrapper_code_ineuron():
    ineuron_url = "https://courses.ineuron.ai/"
    uClient = uReq(ineuron_url)
    ineuronPage = uClient.read()
    uClient.close()
    ineuron_html = bs(ineuronPage, "html.parser")
    bigboxes = ineuron_html.findAll("div", {"class": "Course_course-card__1_V8S Course_card__2uWBu card"})
    with open('testfile','w') as f:
        f.write(ineuron_html.get_text())

def testing_selenium_code():
    with webdriver.Chrome(executable_path=driver_path) as driver:
        driver.get("https://courses.ineuron.ai/")
        def scroll_to_end(wd):
            wd.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(1)
        
        scroll_to_end(driver)
        print(driver.title)
driver_path = "chromedriver.exe"
#testing_web_scrapper_code()
#testing_web_scrapper_code_ineuron()
testing_selenium_code()