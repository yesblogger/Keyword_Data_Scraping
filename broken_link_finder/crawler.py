from requests_html import HTMLSession
from urllib.parse import urlsplit


class Crawler(HTMLSession):
    """
    Create an instance that takes a url. Provides crawling methods and fetching of URLS from pages.  
    """

    def __init__(self, root_url):
        """[creates an crawler instance that takes an root url]

        Arguments:
            root_url {string} -- [starting point of the crawl process]
        """
        super(Crawler, self).__init__()
        self.root_url = root_url
        self.url_object = urlsplit(root_url)
        self.base = self.url_object.netloc  # www.example.com
        self.strip_base = self.base.replace('www.', '')  # example.com
        # http://www.example.com
        self.base_url = "{0.scheme}: // {0.netloc}".format(self.url_object)

    def fetch(self, url, file):
        """Fetched all the urls from a page and returns a list

        Arguments:
            url {[string]} -- [url to start the crawl]
            file {[CSV Dictwriter object]} -- [write all broken links]
        """
        try:
            # crawl url
            source = self.get(url)
        except Exception as e:
            file.writerow(
                {'Location': 'main', 'Broken_URL': url, 'Error': str(e).split(' ', 1)[0]})
            return [""]

        # fetch all on page urls in a loop
        for i, u in enumerate(source.html.links):
            # convert url into a crawlable url
            complete_url = self._build_url(u)
            # create operations for local and foreign urls
            if self.base in complete_url:
                yield complete_url
            else:
                try:
                    # crawl url to check error.
                    self.get(complete_url)
                except Exception as e:
                    if i > 0:
                        file.writerow(
                            {'Location': '', 'Broken_URL': complete_url, 'Error': str(e).split(' ', 1)[0]})
                        yield ""
                    else:
                        file.writerow(
                            {'Location': url, 'Broken_URL': complete_url, 'Error': str(e).split(' ', 1)[0]})
                        yield ""

    def _build_url(self, url):
        """returns a proper formated url

        Arguments:
            url {string} -- url from the main list
        """
        if url.startswith('/'):
            return self.base_url + url
        elif not url.startswith('http'):
            return 'not a http link'
        else:
            return url
