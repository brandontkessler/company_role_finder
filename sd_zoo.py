import requests
from bs4 import BeautifulSoup

URL = 'https://zoo.sandiegozoo.org/jobs/job-openings'

class SDZoo():
    def __init__(self, today, yesterday):
        self.today = today.strftime('%A, %B %d, %Y')
        self.yesterday = yesterday.strftime('%A, %B %d, %Y')
        self.source = requests.get(URL)
        self.soup = BeautifulSoup(self.source.content, 'lxml')
        self.iframe_soup = self.iframe_soup()
        self.job_dates = self.iframe_soup.find_all(class_="posting-date")
        self.jobs = {
            'SD Zoo': {
            }
        }

    def iframe_soup(self):
        iframes = self.soup.find_all('iframe')
        for iframe in iframes:
            iframe_source = iframe.attrs['src']
            if 'dayforcehcm' in iframe_source:
                response = requests.get(iframe_source)
                iframe_soup = BeautifulSoup(response.content, 'lxml')
                return iframe_soup


    def get_jobs(self):
        for date in self.job_dates:
            if (date.text.strip() == self.today) | (date.text.strip() == self.yesterday):
                posting = date.parent.find(class_="posting-title").a
                job = posting.text
                link = f"https://dayforcehcm.com{posting['href']}"
                self.jobs['SD Zoo'][job] = link
        return

if __name__ == '__main__':
    from datetime import datetime, timedelta
    today = datetime.today()
    yesterday = datetime.today() - timedelta(1)
    z = SDZoo(today, yesterday)
    z.get_jobs()
    print(z.jobs)
