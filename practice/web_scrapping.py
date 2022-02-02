"""
Using the requests and BeautifulSoup Python libraries, print to the screen the full text of the
article on this website: http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture.
http://www.practicepython.org/exercise/2014/07/14/19-decode-a-web-page-two.html
"""

import requests
from bs4 import BeautifulSoup

def print_to_text(base_url):
    """
    :param base_url: URL of article to scrape
    :return: naked content to text file
    """
    r = requests.get(base_url)
    soup = BeautifulSoup(r.text)
    with open("work less.txt", "w") as textfile:
        for paragraph in soup.find_all(dir="ltr"):
            textfile.write(paragraph.text.replace("<span>",""))

if __name__ == "__main__":
    #Chose my own article
    base_url = "http://www.theatlantic.com/business/archive/2014/08/to-work-better-work-less/375763/"
    base_url2 = "http://www.theatlantic.com/business/archive/2014/08/to-work-better-work-less/375763/2/"
    print_to_text(base_url)
    print_to_text(base_url2)
