import requests
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen as uReq
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

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
    driver= webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://courses.ineuron.ai/")
    
    def infinite_scroll(driver):
        last_height = driver.execute_script("return document.body.scrollHeight")
        while True:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(1)
            new_height = driver.execute_script("return document.body.scrollHeight")
            
            if new_height == last_height:
                break
            last_height = new_height
    infinite_scroll(driver)
    ineuronPage = driver.page_source
    ineuron_html = bs(ineuronPage, "html.parser")
    titles_found = ineuron_html.findAll(class_="Course_course-title__2rA2S")
    prices_found = ineuron_html.findAll(class_="Course_course-price__3-3_U")
    desc_found = ineuron_html.findAll(class_="Course_course-desc__2G4h9")
    count=0
    titles = []
    prices = []
    descriptions = []
    for title,price,description in zip(titles_found,prices_found,desc_found):
        count+=1
        titles.append(title.text)
        prices.append(price.text)
        descriptions.append(description.text)
    print(titles)
    print(prices)
    print(len(prices_found))
    print(len(titles))
    print(len(descriptions))
#testing_web_scrapper_code()
#testing_web_scrapper_code_ineuron()
testing_selenium_code()