import requests
from lxml import html

www = "http://techcrunch.com/startups/"

def get_link():
    page = requests.get(www)
    tree = html.fromstring(page.text)
    elem = tree.cssselect('div.plain-feature a')[0]
    return elem.get('href')
