import requests
from lxml import html

www = "https://news.ycombinator.com/"

def get_link():
    page = requests.get(www)
    tree = html.fromstring(page.text)
    elem = tree.cssselect('tr td.title a')[0]
    return elem.get('href')
