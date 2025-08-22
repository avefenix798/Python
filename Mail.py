from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from smtplib import SMTP
import smtplib
import sys


recipients = ['ToEmail@domain.com'] 
emaillist = [elem.strip().split(',') for elem in recipients]
msg = MIMEMultipart()
msg['Subject'] = "Your Subject"
msg['From'] = 'from@domain.com'


html = """\
<html>
  <head></head>
  <body>
    {0}
  </body>
</html>
""".format(df_test.to_html())

part1 = MIMEText(html, 'html')
msg.attach(part1)

server = smtplib.SMTP('smtp.gmail.com', 587)
server.sendmail(msg['From'], emaillist , msg.as_string())