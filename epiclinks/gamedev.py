import requests
from lxml import html

www = "http://www.gamedev.net/page/index.html"

def get_link():
    page = requests.get(www)
    tree = html.fromstring(page.text)
    elem = tree.cssselect('div.article_content div.article_content_inner h2 strong a')[0]
    return elem.get('href')
