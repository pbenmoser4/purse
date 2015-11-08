from soup import Soup

class Website:

    def __init__(self, url):
        self.url = url
        self.soup = Soup(url)

ws = Website('http://www.reddit.com')

for link in ws.soup.get_links():
    print link

print ws.soup
