import requests
from lxml import html

www = "http://kukuruku.co/index/newall/"

def get_link():
    page = requests.get(www)
    tree = html.fromstring(page.text)
    elem = tree.cssselect('article.item header.head a.link')[0]
    return elem.get('href')
