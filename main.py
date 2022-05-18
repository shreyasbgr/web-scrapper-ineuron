# Import beautifoul soup
from bs4 import BeautifulSoup as bs
from mongo_util import mongodb_util
from selenium_util import selenium_util

def initialize_mongo_db():
    global my_mongo_util_obj

    connection_url = "mongodb+srv://root:root@myatlascluster.5nfni.mongodb.net/reviews_scrapper_db?retryWrites=true&w=majority"
    db_name = 'reviews_scrapper_db'
    col_name = 'crawlerDb'
    logfile = 'output.log'
    my_mongo_util_obj = mongodb_util(connection_url,db_name,col_name,logfile)

def initialize_selenium_obj():
    global selenium_obj
    selenium_obj = selenium_util()

# Function to web scrape all the courses from https://courses.ineuron.ai/ and store it in mongodb
def web_scraping_code():
    selenium_obj.driver.get("https://courses.ineuron.ai/")
    selenium_obj.infinite_scroll()

    ineuronPage = selenium_obj.driver.page_source
    ineuron_html = bs(ineuronPage, "html.parser")
    courses_found = ineuron_html.findAll(class_="Course_course-card__1_V8S Course_card__2uWBu card")
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
        selenium_obj.driver.close()

def fetch_images():
    selenium_obj.driver.get("https://courses.ineuron.ai/")
    selenium_obj.driver.page_source
    ineuronPage = selenium_obj.driver.page_source
    ineuron_html = bs(ineuronPage, "html.parser")

    images_found = ineuron_html.findAll(class_="Course_left-area__QeYpw")
    for image_container in images_found:
        image_source = image_container.img['src']
        print(image_source)
    selenium_obj.driver.close()

if __name__ == '__main__':
    initialize_mongo_db()
    initialize_selenium_obj()
    #my_mongo_util_obj.delete_all_records()
    #web_scraping_code()
    fetch_images()