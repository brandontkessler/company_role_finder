import requests
from bs4 import BeautifulSoup

URL = 'https://www.laphil.com/about/careers/'

class LAPhil():
    def __init__(self):
        self.source = requests.get(URL)
        self.soup = BeautifulSoup(self.source.content, 'lxml')
        self.listings = self.soup.find(name='p', text='Full-time Staff').nextSibling.find_all('a')
        self.jobs = {
            'LA Phil': {
            }
        }

    def get_jobs(self):
        for listing in self.listings:
            job = listing.text
            link = listing['href']
            self.jobs['LA Phil'][job] = link
        return


if __name__ == '__main__':
    z = LAPhil()
    z.get_jobs()
    print(z.jobs)
