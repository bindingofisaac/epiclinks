import requests
from lxml import html

www = "http://github.com/explore"

def get_link():
    page = requests.get(www)
    tree = html.fromstring(page.text)
    elem = tree.cssselect('div.repo-collection ul.clearfix li.collection-item a.repo-name')[0]
    return "https://github.com"+elem.get('href')
