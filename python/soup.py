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
        """Returns a list of links from anchor tags within this Soup object"""
        # The list to be returned
        ret_list = []
        # Loop through the anchors in this Soup
        for anchor in self.get_anchors():
            # Get the href attribute within the current anchor
            href = anchor.get('href')
            # Sometimes getting the href will return a None object. Just
            # continue the loop like nothing ever happened...
            if href == None:
                continue
            # Otherwise, create an empty link string to return
            link = ''
            if href[0] == '/':
                # If the link is a local link, prepend it with the domain etc
                link = self.domain + href[1:len(href)]
            else :
                link = href
            # After prepending the domain etc, filter out anything that's not
            # an http link, or that is a file. The links we want to deal with
            # will all be http links.
            pat_http = re.compile('http')
            pat_png = re.compile('\.png')
            pat_img = re.compile('\.img')
            if (not pat_http.search(link) or pat_png.search(link) or pat_img.search(link)):
                continue
            # Add the formatted and filtered link to the return list
            ret_list.append(link)
        # We don't care about order, but we do care about
        return set(ret_list)
