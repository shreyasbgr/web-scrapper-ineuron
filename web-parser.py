import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':
    page = requests.get('https://courses.ineuron.ai/')
    soup = BeautifulSoup(page.content,'html.parser')
    course_right_content = soup.find_all('div',class_="Course_right-area__1XUfi")
    print(course_right_content)

    with open('html_content.html','w') as f:
        f.write(soup.prettify()) 