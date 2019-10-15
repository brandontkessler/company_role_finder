import requests
from bs4 import BeautifulSoup

URL = 'https://jobs.disneycareers.com/search-jobs?k=&alp=6252001-5332921-5331835&alt=4'

class Disney():
    def __init__(self, today, yesterday):
        self.today = today.strftime('%b. %d, %Y')
        self.yesterday = yesterday.strftime('%b. %d, %Y')
        self.source = requests.get(URL)
        self.soup = BeautifulSoup(self.source.content, 'lxml')
        self.job_dates = self.soup.find_all(class_='job-date-posted')
        self.jobs = {
            'Disney': {
            }
        }

    def get_jobs(self):
        for date in self.job_dates:
            if (date.text.strip() == self.today) | (date.text.strip() == self.yesterday):
                job = date.parent.parent.h2.text
                link = f"https://jobs.disneycareers.com{date.parent.parent.a['href']}"
                self.jobs['Disney'][job] = link
        return
