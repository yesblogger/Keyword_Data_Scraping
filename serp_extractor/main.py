from requests import Session
from urllib.parse import urlparse, parse_qs, urlsplit
from fake_useragent import UserAgent
from collections import defaultdict
from lxml import html
import csv


'''
Header design: Est Rank, Page Title, Domain, URL 

parse_qs(urlparse(url).query)['q']
//a/child::div[@class="BNeawe vvjwJb AP7Wnd"]
//a[div[@class="BNeawe vvjwJb AP7Wnd"]]/div[1]/text()

'''
# instance to create a fake user agent
UA = UserAgent()

# Dataset to capture the scraped data.
dataset = defaultdict(dict)


def url_parse(keyword):
    output = keyword.split()
    if len(output) > 1:
        return output[0]
    else:
        return "%20".join(output)


def get():
    pass


def extractor():
    """Main function to execute the data extraction process
    """
    # creating a requests Session instance
    session = Session()
    session.headers.update({'User-Agent': UA.random})
    # fetching the inputs from the user
    keyword = url_parse(input("please enter the keyword: "))
    # making the get request to google.
    resp = session.get(f"https://www.google.com/search?q={keyword}")
    # parsing the html content of the page
    parsed_content = html.fromstring(resp.text)
    # setting the counter for the index
    index_counter = 1
    for item in parsed_content.xpath('//a[div[@class="BNeawe vvjwJb AP7Wnd"]]/'):
        url_raw = item.xpath('./@href')
        title = item.xpath(
            '//a[div[@class="BNeawe vvjwJb AP7Wnd"]]/div[1]/text()').strip()
        # dataset[index_counter][]
    pass


def write_to_csv():
    with open("serp.csv", mode="w", newline="", encoding="utf-8") as w_file:
        # creating header of the new csv file
        header = ['Est Rank', 'Page Title', 'Domain', 'URL']
        # setting csv instance with the header
        writer = csv.DictWriter(w_file, fieldnames=header)
        writer.writeheader()
        pass


if __name__ == "__main__":
    extractor()
