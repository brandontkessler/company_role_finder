import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_mail(job_dict):
    sender_email = 'brandontkessler@gmail.com'
    receiver_email = 'brandontkessler@gmail.com'

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('brandontkessler@gmail.com', 'hklooqkdrnxmoych')

    subject = 'Jobs at companies you like'

    msg = MIMEMultipart("alternative")
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = receiver_email

    plain_msg = MIMEText(text_version(job_dict), "plain")
    html_msg = MIMEText(html_version(job_dict), "html")

    msg.attach(plain_msg)
    msg.attach(html_msg)

    server.sendmail(
        sender_email,
        receiver_email,
        msg.as_string()
    )

    server.quit()



def html_version(job_dict):
    body = ""
    for company, jobs in job_dict.items():
        company_html = f"<h2>{company}</h2>"
        job_html = ""
        for job, link in jobs.items():
            result = f"<li>{job}: <a href={link}>link</a></li>"
            job_html += result

        body += company_html
        body += "<ul>"
        body += job_html
        body += "</ul>"
        body += "<br>"
    return body


def text_version(job_dict):
    body = ""
    for company, jobs in job_dict.items():
        body += f"{company}:\n"
        job_text = ""
        for job, link in jobs.items():
            result = f"{job}: {link}\n"
            job_text += result
        body += job_text
    return body
