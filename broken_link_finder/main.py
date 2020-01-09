import csv
from collections import deque
from crawler import Crawler

# a queue of urls to be crawled next
urls = deque()
# list of urls that have been processed
processed_urls = set()

if __name__ == "__main__":
    # print a welcome message for the user
    print("""Welcome to the Crawler script.
Please enter the root domain of your website. Once started
the script will crawl all internal links and list status codes of external links in
separate csv file called output."""
          )
    # new line
    print()
    # ask for the root domain
    while True:  # continuos loop still we get a valid domain name
        root_domain = input("Please enter the root domain: ")
        # check whether it is a valid domain
        if 'http://' in root_domain or 'https://' in root_domain:
            # add valid url to the list
            urls.append(root_domain)
            break
    # create a crawler instance
    crawler = Crawler(root_domain)
    # open a csv file with the header Page, URL, Status
    with open('broken_links.csv', mode='w', newline='', encoding='utf-8') as w_file:
        # create header for csv file
        header = ['Location', 'Broken_URL', 'Error']
        # create a csv object
        writer = csv.DictWriter(w_file, fieldnames=header)
        # write the header of the file
        writer.writeheader()
        # begin iteration to crawl pages
        while len(urls):  # loop stops when list has no url left
            # remove url from list to be processed
            url = urls.popleft()
            # crawl URL and fetch all URLs.
            for u in crawler.fetch(url, writer):
                if u not in urls and u not in processed_urls and u != "":
                    urls.append(u)
            # once URL is process, add it to the processed list
            processed_urls.add(url)
            print(len(urls))
            print(len(processed_urls))
