from bs4 import BeautifulSoup
from urlparse import urlparse
import urllib2

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
        ret_array = []
        for anchor in self.get_anchors():
            ret_array.append(anchor.get('href'))
        return ret_array

ex = Soup('http://www.google.com')
for link in ex.get_links():
    print link
    
print ex.domain
