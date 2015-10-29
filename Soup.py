from bs4 import BeautifulSoup
from urlparse import urlparse
import urllib2
import re

class Soup:

    def __init__(self, url, parser = 'html.parser'):
        self.url = url
        request = urllib2.Request(self.url)
        request.add_header('User-agent', 'Mozilla/5.0')
        response = urllib2.urlopen(request)
        self.soup = BeautifulSoup(response, parser)

        prs = urlparse(url)
        self.domain = '{uri.scheme}://{uri.netloc}/'.format(uri=prs)

    def get_anchors(self):
        return self.soup.find_all('a')

    def get_links(self):
        """
        """
        ret_list = []
        for anchor in self.get_anchors():
            href = anchor.get('href')
            if href == None:
                continue

            link = ''
            if href[0] == '/':
                link = self.domain + href[1:len(href)]
            else :
                link = href

            pattern = re.compile('http')
            if (not pattern.search(link)):
                continue

            ret_list.append(link)
        return set(ret_list)
