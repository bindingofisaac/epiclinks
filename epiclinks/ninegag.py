import requests
from lxml import html

www = "http://9gag.tv/"

def get_link():
    page = requests.get(www)
    tree = html.fromstring(page.text)
    elem = tree.cssselect('div.col-md-3 div.item a.img-container')[0]
    return elem.get('href')
