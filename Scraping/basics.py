from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as ureq


class Test(object):

    def __init__(self):
        pass

    def get_content(self, url):
        response = ureq(url)
        return response

    def get_page_content(self, response):
        page_html = response.read()
        return page_html

    def parse(self, html_content, parser):
        return soup(html_content, parser)


def run():
    url = 'https://www.newegg.com/CPUs-Processors/Category/ID-34'
    test = Test()

    response = test.get_content(url)
    page_html = test.get_page_content(response)
    # print(page_html)
    response.close()

    page_soup = test.parse(page_html, 'html.parser')
    # print(page_soup)

    # containers = page_soup.findAll('div', {'class': 'item-container'})
    containers = page_soup.findAll('a', {'class': 'item-title'})

    count = 0
    print("Listing product titles on the page: ", url)
    for container in containers:
        count += 1
        # brand = container.div.div.a.img['title']
        product = container.text
        print('Product %s: ' % str(count), product)

        print('\n')


if __name__ == '__main__':
    run()
