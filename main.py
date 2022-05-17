# Import beautifoul soup
from bs4 import BeautifulSoup as bs

from mongo_util import mongodb_util
import time

# Imports for selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

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
    courses_found = ineuron_html.findAll(class_="Course_course-card__1_V8S Course_card__2uWBu card")
    titles = []
    descriptions = []
    instructors = []
    prices = []
    for course in courses_found:
        title = course.find(class_="Course_course-title__2rA2S")
        description = course.find(class_="Course_course-desc__2G4h9")
        instructor = course.find(class_="Course_course-instructor__1bsVq")
        price = course.find(class_="Course_course-price__3-3_U")
        record = {
            "title": title.text if title else '',
            "description": description.text if description else '',
            "instructor": instructor.text if instructor else '',
            "price": price.text if price else ''
        }
        my_mongo_util_obj.insert_one_record(record)
        titles.append(title.text if title else '')
        descriptions.append(description.text if description else '')
        instructors.append(instructor.text if instructor else '')
        prices.append(price.text if price else '')

    print(titles)
    print(prices)
    print(instructors)
    print(len(titles))
    print(len(descriptions))
    print(len(instructors))
    print(len(prices))

if __name__ == '__main__':
    global my_mongo_util_obj

    connection_url = "mongodb+srv://root:root@myatlascluster.5nfni.mongodb.net/reviews_scrapper_db?retryWrites=true&w=majority"
    db_name = 'reviews_scrapper_db'
    col_name = 'crawlerDb'
    logfile = 'output.log'
    my_mongo_util_obj = mongodb_util(connection_url,db_name,col_name,logfile)
    testing_selenium_code()