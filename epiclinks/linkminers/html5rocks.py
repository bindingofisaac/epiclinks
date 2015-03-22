import requests
from lxml import html

www = "http://www.html5rocks.com/en/"

def get_link():
    page = requests.get(www)
    tree = html.fromstring(page.text)
    elem = tree.cssselect('div.container ul li a')[0]
    return elem.get('href')
