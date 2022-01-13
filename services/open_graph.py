import urllib.request
from bs4 import BeautifulSoup


def get_open_graph(url: str):
    page = get_page(url)
    ogMap = {}
    og_tags = ['title', 'description', 'image', 'locale', "site_name", "url"]
    for tag in og_tags:
        ogMap[tag] = get_og(page, tag)
    title = get_title(page)
    if title != '':
        ogMap["title"] = title
    return ogMap


def get_page(url: str):
    response = urllib.request.urlopen(url)
    soup = BeautifulSoup(response,
                         'html.parser',
                         from_encoding=response.info().get_param('charset'))

    return soup


def get_og(soup, og_tag):
    if soup.findAll("meta", property=f"og:{og_tag}"):
        return soup.find("meta", property=f"og:{og_tag}")["content"]
    return


def get_title(soup):
    return soup.find('title').string.__str__()
