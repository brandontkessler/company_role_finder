from disney import Disney
from sd_zoo import SDZoo
from la_phil import LAPhil

from mail import send_mail
from datetime import datetime, timedelta

if __name__=='__main__':
    today = datetime.today()
    yesterday = datetime.today() - timedelta(1)
    all = {}

    disney = Disney(today=today, yesterday=yesterday)
    disney.get_jobs()

    sdzoo = SDZoo(today=today, yesterday=yesterday)
    sdzoo.get_jobs()

    laphil = LAPhil()
    laphil.get_jobs()

    all.update(disney.jobs)
    all.update(sdzoo.jobs)
    all.update(laphil.jobs)

    send_mail(all)
